'''---------ATM BALANCE CHECK PROGRAM---------
A bank requires customers to maintain a minimum balance of ₹5,000 in their savings account. 
Write a Python program that accepts the current account balance from the user. If the balance is 
less than ₹5,000, display a warning message indicating that the minimum balance requirement is not 
maintained. 
---------------------------------------------------------
Sample Input 
Enter Account Balance: 3200 
---------------------------------------------------------
Sample Output 
Warning! Your account balance is below the minimum required balance of ₹5000.
--------------------------------------------------------- '''

#Coding starts here 
#inputs the data from the user
print("---------------------------------------------------------")

minimum_balance = 5000
current_balance = float(input("Enter Account Balance(in Rs): "))
#validating current balance
if current_balance <=   0:
    exit("Invalid input. Please enter a valid account balance.")

#validating the current balance against the minimum balance requirement
if current_balance < minimum_balance:
    print("Warning! Your account balance is below the minimum required balance of ₹5000.")
else:
    print("Your account balance is sufficient and meets the minimum balance requirement.")
print("---------------------------------------------------------")

'''Output:
Enter Account Balance(in Rs): 3200
Warning! Your account balance is below the minimum required balance of ₹5000.
---------------------------------------------------------
Enter Account Balance(in Rs): 6000
Your account balance is sufficient and meets the minimum balance requirement.
---------------------------------------------------------'''