'''-------------------E-Commerce Premium Membership Eligibility-----------------------
Problem Statement 
A customer becomes Premium Member if: 
• Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  
Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  
-------------------------------------------------
Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000
-------------------------------------------------
'''

#coding starts here 
#inputs from the user
print("-------------------------------------------------")
total_purchases = float(input("Total Amount of purchases done till today: "))
orders = int(input("Orders completed: "))
rating   = float(input("Customer Rating(1-5): "))

#validating the input data
if total_purchases <= 0:
    exit("Enter valid amount")
if orders <= 0:
    exit("Enter Valid order range")
if rating <= 0:
    exit("You are not eligible")


#validating membership conditions
if total_purchases >= 100000:
    print("Premium Membership Status: Eligible")
    print("Reason: Purchase amount exceeded ₹100000")
elif total_purchases >= 50000 and orders >= 20  and rating >= 4.5:
    print("Premium Membership Status: Eligible")
else:
    print("Premium Membership Status: Not Eligible")
print("-------------------------------------------------")


'''Output:
-------------------------------------------------
Total Amount of purchases done till today: 120000
Orders completed: 12
Customer Rating(1-5): 3
Premium Membership Status: Eligible
Reason: Purchase amount exceeded ₹100000
-------------------------------------------------
-------------------------------------------------
Total Amount of purchases done till today: 60000
Orders completed: 25
Customer Rating(1-5): 4.2
Premium Membership Status: Not Eligible
-------------------------------------------------
-------------------------------------------------
Total Amount of purchases done till today: 80000
Orders completed: 65
Customer Rating(1-5): 4.8
Premium Membership Status: Eligible
-------------------------------------------------'''