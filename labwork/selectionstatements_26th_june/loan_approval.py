'''-------------Loan Approval System-------------
Problem Statement 
A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected 
------------------------------------------------ 
Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 
Sample Output 
Loan Status: Manual Review 
Reason: Income criteria not satisfied.
------------------------------------------------
'''

#coding starts here 
#inputs the data from user
credit_score = int(input("Enter Credit Score: "))
annual_income = int(input("Enter Annual Income: "))
existing_loan_amount = int(input("Enter Existing Loan Amount: "))

#validating the inputs
if credit_score < 0 or credit_score > 1000:
    exit("Invalid Credit Score. Please enter a value between 0 and 1000.")
elif annual_income < 0:
    exit("Invalid Annual Income. Please enter a positive value.")
elif existing_loan_amount < 0:
    exit("Invalid Existing Loan Amount. Please enter a positive value.")


#validating the conditions for loan approval

if credit_score >= 750 and annual_income >= 800000 and existing_loan_amount <= 200000:
    print("Loan Status: Approved")
    #loan conditions for manual review
elif (credit_score < 750 and annual_income >= 800000 and existing_loan_amount <= 200000) or \
     (credit_score >= 750 and annual_income < 800000 and existing_loan_amount <= 200000) or \
     (credit_score >= 750 and annual_income >= 800000 and existing_loan_amount > 200000):   
    print("Loan Status: Manual Review")
    if credit_score < 750:
        print("Reason: Credit score criteria not satisfied.")
    if annual_income < 800000:
        print("Reason: Income criteria not satisfied.")
    if existing_loan_amount > 200000:
        print("Reason: Existing loan amount criteria not satisfied.")
else:
    print("Loan Status: Rejected")



'''Output:
Enter Credit Score: 780
Enter Annual Income: 750000
Enter Existing Loan Amount: 100000
Loan Status: Manual Review
Reason: Income criteria not satisfied.
'''