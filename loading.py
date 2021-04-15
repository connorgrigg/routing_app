import csv
from hash import HashTable


#   setup for package object
class Package:
    def __init__(self, id, street, city, state, zip, dest, due, mass, note, start, delivery_time, status):
        self.id = id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.dest = dest
        self.due = due
        self.mass = mass
        self.note = note
        self.start = start
        self.delivery_time = delivery_time
        self.status = status


#   O(N) - converts street address (eg 123 Street St) to address id (eg 12)
def convert_street_id(street):
    with open('AddressList.csv') as csv_file:
        address_reader = list(csv.reader(csv_file, delimiter=','))
        for i in address_reader:
            if i[2] == street:
                return i[0]


#   O(N) - organizes and sorts packages between the three trucks
def load_trucks():
    with open('PackageList.csv') as csv_file:
        package_reader = csv.reader(csv_file, delimiter=',')

        for i in package_reader:
            id = i[0]
            street = i[1]
            city = i[2]
            state = i[3]
            zip = i[4]
            dest = convert_street_id(street)
            due = i[5]
            mass = i[6]
            note = i[7]
            start = 0.0
            delivery_time = ''
            status = 'En route'
            package = Package(id, street, city, state, zip, dest, due, mass, note, start, delivery_time, status)
            table.insert(package.id, package)

            if 'Wrong address' in package.note:
                package.start = 10.35
                third.append(package)

            if 'truck 2' in package.note or 'Delayed on flight' in package.note:
                package.start = 9.1
                second.append(package)

            if package.due != 'EOD':
                if 'None' in package.note or 'Must be delivered with' in package.note:
                    package.start = 8.0
                    first.append(package)

            if package not in first and package not in second and package not in third:
                if len(second) < len(third):
                    package.start = 9.1
                    second.append(package)
                else:
                    package.start = 10.35
                    third.append(package)


first = []
second = []
third = []
table = HashTable()
load_trucks()


#   O(1) - returns populated first truck
def get_first():
    return first


#   O(1) - returns populated second truck
def get_second():
    return second


#   O(1) - returns populated third truck
def get_third():
    return third


#   O(1) - returns populated hashtable
def get_table():
    return table
