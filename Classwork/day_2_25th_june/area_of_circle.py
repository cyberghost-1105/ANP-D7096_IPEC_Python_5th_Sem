'''to calculate area of circle '''

#input of radius from the user
radius = float(input("Enter the radius of the circle (in cm): "))
#validating the radius
if radius < 0:
    print("Radius cannot be negative.")
    exit()

pi = 3.14159
print("-------------------------------------")

#displaying data to the user
print("Radius of the circle: ", radius, "cm")
print("Value of pi used: ", pi)

print("-------------------------------------")

#displaying area of the circle
print("Area of the circle: ", pi * radius**2, "cm²")

'''Output:
Enter the radius of the circle (in cm): 5
Radius of the circle:  5.0 cm
Value of pi used:  3.14159
Area of the circle:  78.53975 cm²'''
