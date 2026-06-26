''' Electricity Bill Discount 
Problem Statement 
An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 
or more. Otherwise, no discount is applied. 
Write a Python program to accept the total bill amount from the user and display the final amount to 
be paid. 
Sample Input 1 
Enter the electricity bill amount: 6200 
Sample Output 1 
Discount Applied! 
Final Bill Amount: ₹5580.0 
Sample Input 2 
Enter the electricity bill amount: 4200 
Sample Output 2 
No Discount Applied! 
Final Bill Amount: ₹4200
----------------------------------------------------------'''


# program to accept the total bill amount from the user and display the final amount to 
# be paid.
total_bill = float(input("Enter the total electricity bill :"))
# to validate electricity bill 

if(total_bill < 0):
    exit("Amount should be positive")

# to verify the electricity bill
if(total_bill >= 5000):
    print(" discount applied : ")
    print("Final Bill Amount is : ",total_bill-(total_bill*0.1))
else:
    print("No Discount Applied ")
    print("FInal bill amount is : ",total_bill)
print("----------------------------------------------------------")

'''output:
Enter the total electricity bill :6200
 discount applied : 
Final Bill Amount is : 5580.0
----------------------------------------------------------'''