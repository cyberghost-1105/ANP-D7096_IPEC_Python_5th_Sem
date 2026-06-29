''' Login System with Maximum Attempts 
Problem Statement 
A system allows only three login attempts. 
The correct username is admin and the password is python123. 
If the credentials are correct, display "Login Successful". 
Otherwise, after three unsuccessful attempts, display "Account Locked". 
Sample Output 
Attempt 1 
Username: admin 
Password: abc 
 
Invalid Credentials 
 
Attempt 2 
Username: admin 
Password: python123 
 
Login Successful'''

# Correct credentials
correct_username = "admin"
correct_password = "python123"

attempt = 1

while attempt <= 3:
    print(f"\nAttempt {attempt}")

    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempt += 1

if attempt > 3:
    print("Account Locked")


'''Attempt 1
Username: admin
Password: abc

Invalid Credentials

Attempt 2
Username: admin
Password: python123

Login Successful'''