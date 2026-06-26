'''-----------------Parking Fee Waiver Program-----------------
A shopping mall waives the parking fee if a customer has made purchases worth ₹2,000 or more. 
Otherwise, the customer must pay a parking fee of ₹100. 
Write a Python program to accept the purchase amount and display whether the parking fee is 
waived or payable. 
Sample Input 1 
Enter the purchase amount: 2500 
Sample Output 1 
Parking Fee Waived! 
Parking Fee: ₹0 
Sample Input 2 
Enter the purchase amount: 1500 
Sample Output 2 
Parking Fee Applicable! 
Parking Fee: ₹100 
-----------------------------------------------------------'''


# n program to accept the purchase amount and display whether the parking fee is 
# waived or payable. 
purchase_amount = float(input("Enter the Purchase amount : "))

# to validate amount 
if(purchase_amount < 0):
    exit("Amount should be positive  ")
# to verify the purchase amount 
if(purchase_amount >= 2000):
    print("Mall Waives the parking fee ")

else:
    print("you must have to pay parking fee of 100 rs.")
print("-----------------------------------------------------------")

'''output:
Enter the Purchase amount : 2500
Mall Waives the parking fee 
-----------------------------------------------------------
Enter the Purchase amount : 1500
you must have to pay parking fee of 100 rs.
-----------------------------------------------------------
'''