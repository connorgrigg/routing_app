from hash import HashTable
import csv

#   setup for address object
class Address:
    #   O(1)
    def __init__(self, id, name, street):
        self.id = id
        self.name = name
        self.street = street


ht = HashTable()
address_list = []

# O(N) - populates tables with addresses
def load_addresses():
    with open('AddressList.csv') as csv_file:
        address_reader = csv.reader(csv_file, delimiter=',')
        for i in address_reader:
            id = i[0]
            name = i[1]
            street = i[2]
            address = Address(id, name, street)
            ht.insert(address.id, address)
            address_list.append(address)


load_addresses()


#   O(1) - returns populated address hashtable
def return_address_hashtable():
    return ht


#   O(1) - returns populated address list
def return_address_list():
    return address_list
