'''to calculate the speed'''
#input the distance and time from the user
distance = float(input("Enter the distance (in km): "))
time = int(input("Enter the time (in hours): "))

#validating the inputs
if distance < 0 or time < 0:
    print("Distance and time cannot be negative.")
    exit()

#calculating the speed
speed = distance / time if time != 0 else 0

#displaying the result
print("Speed: ", speed, "km/h")

'''Output:
Enter the distance (in km): 100
Enter the time (in hours): 2
Speed:  50.0 km/h
'''