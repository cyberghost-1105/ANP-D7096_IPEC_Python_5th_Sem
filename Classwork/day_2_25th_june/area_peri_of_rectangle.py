'''to calculate area and perimeter of rectangle'''

#input the data of rectangle from the user
length = float(input("Enter the length of the rectangle (in cm): "))  
width = float(input("Enter the width of the rectangle (in cm): "))
#validating the length and width
if length < 0 or width < 0:
    print("Length and width cannot be negative.")
    exit()
    
#calculating area and perimeter
area = length * width
perimeter = 2 * (length + width)

print("-------------------------------------")

#displaying the results
print("Area of the rectangle: ", area, "cm²")
print("Perimeter of the rectangle: ", perimeter, "cm")
print("-------------------------------------")
