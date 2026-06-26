'''---------------Loan Eligibility Checker----------------
A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or 
more. 
Write a Python program to accept the applicant's monthly salary and display whether they are 
eligible to apply for the loan.
---------------------------------------------------------- 
Sample Input 1 
Enter your monthly salary: 45000 
Sample Output 1 
Congratulations! You are eligible to apply for the loan. 
---------------------------------------------------------
Sample Input 2 
Enter your monthly salary: 22000 
Sample Output 2 
Sorry! You are not eligible to apply for the loan. 
---------------------------------------------------------
'''

#Coding starts here
#inputs the data from the user
print("----------------------------------------------------------")
salary = float(input("Enter your monthly salary: "))
#validating the salary input    
if salary <= 0:
    exit("Invalid input. Please enter a valid monthly salary.")

#checking eligibility
if salary >= 30000:
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.") 
print("----------------------------------------------------------")