''' --------------Greatest Number----------------
Write a program to check whether the  two given numbers are greater than other or not.
---------------------------
Sample Input 1: 5, 10
Sample Output 1: 10 is the greatest number.
---------------------------'''

#coding starts here
#taking input from the user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("----------------------------------------------------------")
#checking which number is greater
if num1 > num2:
    print(num1, "is the greatest number.")
elif num2 > num1:
    print(num2, "is the greatest number.")
else:
    print("Both numbers are equal.")
print("----------------------------------------------------------")

'''Output:
Enter first number: 5
Enter second number: 10
10.0 is the greatest number.'''
