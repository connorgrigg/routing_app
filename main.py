#   Connor Grigg ID# 001187350
import routing
import math

time = routing.get_time()
mileage = routing.get_mileage()
time_dec, time_int = math.modf(time)
time_dec *= 60
#   O(1) - sets up menu for program, and looks up user input
print("\nWGUPS Tracking System\nRoute was completed in: ", int(time_int), " hours and ", int(time_dec),
      " minutes\nRoute was completed in: ", routing.get_mileage(), " miles")
sel = -1
sel2 = -1
sel3 = -1
sel4 = -1
#   O(N)
while sel != 3:
    output = routing.get_delivered_packages()
    sel = -1
    sel2 = -1
    sel3 = -1
    sel4 = -1
    sel = int(input("\n1. Get Information on all packages\n2. Get Information on a particular "
                    "package\n3. Exit\n"))
    if sel == 1:  # for all packages
        sel2 = float(input("At which time would you life this information? Please use format 6.5 = 6:30am, "
                           "18.5 = 6:30pm\n"))
        for i in range(len(output)):
            if output[i].delivery_time <= sel2:  # if package has already been delivered, print it as delivered
                print(output[i].__dict__)
            else:  # otherwise if it hasnt been delivered
                output[i].status = 'En Route'
                print(output[i].__dict__)

    elif sel == 2:  # for a specific package
        sel2 = int(input("Which package ID would you like to lookup?\n"))
        sel3 = int(input("At what time would you like this information? Please use format 6.5 = 6:30am, 18.5 = 6:30pm"))
        for i in range(len(output)):
            if output[i].id == sel2:  # if package id = objects id
                if output[i].delivery_time <= sel3:  # if package has been delivered
                    print(output[i].__dict__)
                else:  # if package has not been delivered
                    output[i].status = 'En Route'
                    print(output[i].__dict__)
    elif sel == 3:  # exit program
        quit()
