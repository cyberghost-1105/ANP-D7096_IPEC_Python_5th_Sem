'''------------------# Scholarship Award Program----------------------------
Problem Statement 
Scholarship is awarded based on percentage: 
Percentage Scholarship 
95+ 100% 
90-94 75% 
85-89 50% 
80-84 25% 
Below 80 No Scholarship 
Conditions: 
• Family income must be below ₹8,00,000.  
• Students with disciplinary actions receive no scholarship. 
---------------------------------------------- 
Sample Input 
Percentage: 92 
Family Income: 500000 
Disciplinary Action (Y/N): N 
Sample Output 
Scholarship Awarded: 75%
----------------------------------------------
'''

#coding starts here 
#inputs from the user
print("-------------------------------------------------")

percentage = float(input("Enter Percentage: "))
family_income = float(input("Enter Family Income: "))
disciplinary = input("Disciplinary Action (Y/N): ")

#validating conditions
if family_income >= 800000 or disciplinary.upper() == "Y":
    print("Scholarship Awarded: No Scholarship")
else:
    if percentage >= 95:
        print("Scholarship Awarded: 100%")
    elif percentage >= 90:
        print("Scholarship Awarded: 75%")
    elif percentage >= 85:
        print("Scholarship Awarded: 50%")
    elif percentage >= 80:
        print("Scholarship Awarded: 25%")
    else:
        print("Scholarship Awarded: No Scholarship")
print("-------------------------------------------------")


'''Output:
-------------------------------------------------
Enter Percentage: 85
Enter Family Income: 2500
Disciplinary Action (Y/N): n
Scholarship Awarded: 50%
-------------------------------------------------
-------------------------------------------------
Enter Percentage: 98
Enter Family Income: 560000
Disciplinary Action (Y/N): y
Scholarship Awarded: No Scholarship
-------------------------------------------------
'''
