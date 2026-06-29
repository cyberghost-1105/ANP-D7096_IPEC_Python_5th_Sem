'''. Bank Transaction Summary 
Problem Statement 
A customer keeps entering transaction amounts. 
Positive numbers indicate deposits, while negative numbers indicate withdrawals. 
The customer enters 0 to finish. 
Display: 
• Total Deposit  
• Total Withdrawal  
• Final Balance  
'''
# Initialize variables
total_deposit = 0
total_withdrawal = 0
balance = 0

while True:
    amount = float(input("Enter transaction amount (0 to finish): "))

    if amount == 0:
        break

    if amount > 0:
        total_deposit += amount
    else:
        total_withdrawal += abs(amount)

    balance += amount

# Display results
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", balance)


'''output
Enter transaction amount (0 to finish): 5000
Enter transaction amount (0 to finish): -1500
Enter transaction amount (0 to finish): 2000
Enter transaction amount (0 to finish): -500
Enter transaction amount (0 to finish): 0

Total Deposit: 7000.0
Total Withdrawal: 2000.0
Final Balance: 5000.0'''