'''1. ATM PIN Verification 
Problem Statement 
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. The user can keep entering the 
PIN until it matches the correct one. 
Display "Access Granted" when the correct PIN is entered. 
Sample Output 
Enter PIN: 1234 
Incorrect PIN 
 
Enter PIN: 9876 
Incorrect PIN 
 
Enter PIN: 4589 
Access Granted
'''


#coding starts here 
#input pin from the user

pin = int(input("Enter 4 digit pin: "))

correct_pin = 4589

while pin != correct_pin:
    pin = int(input("Enter 4 digit pin: "))

print("Access Granted")


'''Output
Enter 4 digit pin: 5555
Enter 4 digit pin: 5555
Enter 4 digit pin: 4589
Access Granted
'''