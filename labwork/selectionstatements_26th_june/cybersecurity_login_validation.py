'''--------------------------Cybersecurity Login Validation------------------------
Problem Statement 
A login system validates: 
• Username  
• Password  
• OTP  
Conditions: 
• All correct → Login Successful  
• Incorrect OTP → Re-enter OTP  
• Incorrect Password after 3 attempts → Account Locked  
• Incorrect Username → User Not Found  
----------------------------------------------
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 
Sample Output 
Login Successful 
Welcome Admin
------------------------------------------------'''

#coding starts here 
#inputs from the user


correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"
print("----------------------------------------------------")

username = input("Enter Username: ")

# Cybersecurity Login Validation

if username != correct_username:
    print("User Not Found")
else:
    attempts = 0
    while attempts < 3:
        password = input("Enter Password: ")

        if password == correct_password:
            otp = input("Enter OTP: ")

            if otp == correct_otp:
                print("Login Successful")
                print("Welcome Admin")
            else:
                print("Re-enter OTP")
            break
        else:
            attempts += 1
            if attempts == 3:
                print("Account Locked")
            else:
                print("Incorrect Password. Try Again.")
print("----------------------------------------------------")


'''Output
----------------------------------------------------
Enter Username: admin
Enter Password: admin123
Enter OTP: 4567
Login Successful
Welcome Admin
----------------------------------------------------
----------------------------------------------------
Enter Username: admin
Enter Password: admin123
Enter OTP: 1234
Re-enter OTP
----------------------------------------------------
----------------------------------------------------
Enter Username: admin
Enter Password: abc
Enter Password: 123
Enter Password: test
Incorrect Password. Try Again.
Incorrect Password. Try Again.
Account Locked
----------------------------------------------------
'''