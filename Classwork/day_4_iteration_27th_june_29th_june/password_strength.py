'''Password Strength Checker 
Problem Statement 
A website requires users to create a password having at least 8 characters. 
Keep asking the user to enter a password until the entered password satisfies the minimum length 
requirement. 
Sample Output 
Enter Password: hello 
Password too short. 
 
Enter Password: python@123 
Password Accepted. '''


#codin starts here 
# Input from the user
password = input("Enter Password: ")

while len(password) < 8:
    print("Password too short.")
    password = input("Enter Password: ")

print("Password Accepted.")


'''output
Enter Password: vnavb
Password too short.
Enter Password: vabbvuibaivb
Password Accepted.
'''