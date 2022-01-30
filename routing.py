import csv
import address
import loading

temp_truck = loading.get_first()
truck_load = len(temp_truck)
cur_address_id = 0
addresses = address.return_address_list()
delivered_packages = []
undelivered_packages = []


#  O(N) calculate distance to return to hub
def distance_between_two(current_location_id, destination_location_id):
    retvar = get_distance_in_column(current_location_id)[destination_location_id]
    return retvar


#   O(N) - removes packages from the algorithm list and marks them delivered
def update_package_list(truck, dest, miles):
    retlist = []
    for i in range(len(truck)):
        if int(dest) != int(truck[i].dest):
            retlist.append(truck[i])
        else:
            truck[i].status = 'Delivered'
            truck[i].delivery_time = float(miles / 18 + truck[i].start)
            delivered_packages.append(truck[i])
    return retlist


#   O(N) - sets up the distance from current position
def get_distance_in_column(column):
    retlist = []
    with open('DistanceTable.csv', 'r') as csv_file:
        distance_table = csv.reader(csv_file, delimiter=',')
        for i in distance_table:
            retlist.append(float(i[column]))
        return retlist


#   O(N) - gets ID of destination based on street
def get_destination_id(address_list, dest_street):
    for i in range(len(address_list)):
        if dest_street == address_list[i].street:
            return address_list[i].id


#   O(N) - generates list of IDs from all packages in truck
def get_list_of_ids(truck):
    retlist = []
    for i in range(len(truck)):
        retlist.append(truck[i].dest)
    return retlist


'''
For the delivery algorithm, I selected the nearest neighbor algorithm; algorithm takes in just the truck, everything 
else is held within the objects; first we start with the trucks daily mileage being 0, starting at address ID 0 (hub)
and pulling up a list of address IDs for all packages on the truck; then for every ID in the ID list, we generate a
tuple in the format (distance to nearest package point, address ID). Then we put the tuple in a list, sort the list,
and select the closest element in the list (IE nearest location) and then removes the relevant package or packages, 
in case of multiple packages, from the list. The ID list is cleared after each iteration so that the delivered IDs dont
create false destinations. We iterate over that until there are zero elements in the truck; before finishing the final 
loop, we calculate the distance from the final package back to the depot and add that to the final mileage that is 
returned at the end of the method

O(N^2)
'''


def calc_mileage(truck):
    daily_mileage = 0
    cur_address_id = 0
    id_list = []
    list_of_remaining_addresses = []
    col = get_distance_in_column(cur_address_id)
    for j in range(len(truck)):
        id_list = get_list_of_ids(truck)
        for i in range(len(id_list)):
            temp_id = int(id_list[i])
            temp_tuple = (col[temp_id], temp_id)
            list_of_remaining_addresses.append(temp_tuple)
        list_of_remaining_addresses.sort()
        if len(list_of_remaining_addresses) != 0:
            temp_mileage, dest_id = list_of_remaining_addresses[0]
            daily_mileage += float(temp_mileage)
        cur_address_id = dest_id
        col = get_distance_in_column(cur_address_id)
        truck = update_package_list(truck, cur_address_id, daily_mileage)
        if j == len(truck) - 1:
            daily_mileage += distance_between_two(cur_address_id, 0)
        list_of_remaining_addresses.clear()
        id_list.clear()
    return daily_mileage


with open('DistanceTable.csv') as csv_file:
    distance_table = list(csv.reader(csv_file, delimiter=','))
    mileage = 0
    mileage += calc_mileage(loading.get_first())
    mileage += calc_mileage(loading.get_second())
    mileage += calc_mileage(loading.get_third())


#   O(1) - formats mileage
def get_mileage():
    return round(mileage, 2)


#   O(1) - converts mileage to road time, formats
def get_time():
    hours = get_mileage()
    clean_hour = round(hours / 18, 2)
    return clean_hour


#   O(1) - returns delivered packages
def get_delivered_packages():
    return delivered_packages
