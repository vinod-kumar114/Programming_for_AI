"""Q1 You've been hired as a junior developer for "Karachi Cabs," a ride-hailing startup. A
dispatcher needs a simple tool to find the nearest available driver to a passenger's pickup point.
The drivers are all mapped on a simple 2D grid.
Driver locations (x, y): (3, 4), (10, 2), (6, 9), (1, 7), (8, 5)
Write a Python script to help with the following:
1. Store the driver locations.
2. Repeatedly ask the passenger for their pickup X and Y coordinates.
3. Using the Euclidean distance formula, calculate the distance to each driver.
4. Display which driver is nearest and the distance to them.
5. Let the passenger type 'quit' to exit the tool.

"""

driver_locations=[(3,4),(10,2),(6,9),(1,7),(8,5)]

while True:
    op = input("Type option: \n\t1. Continue\n\t2. Quit\n")

    if op.lower()=="quit" or op.lower()=='q':
        print("Quiting...")
        break
    elif op.lower()=="continue" or op.lower()=='c' or op.lower()=='cont':
        x_cod = int(input("Enter your x-corrdinate: "))
        y_cod = int(input("Enter your y-corrdinate: "))

        dist_with_driver = []

        for i in driver_locations:
            dist_with_driver.append(((x_cod-i[0])**2+(y_cod-i[1])**2)**0.5)

        least_dist = min(dist_with_driver)

        for i,j in zip(dist_with_driver,driver_locations):
            if i==least_dist:
                print("Closest driver is: ", j)
                print("Least distance is: ", round(least_dist,2))

    else:
        print("Choose valid option...")
