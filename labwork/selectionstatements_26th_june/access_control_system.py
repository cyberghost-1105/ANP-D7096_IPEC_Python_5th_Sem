'''---------------------Multi-Level Access Control System----------------------------
Problem Statement 
Assign access levels based on: 
Roles: 
• Admin  
• Manager  
• Employee  
• Guest  
Conditions: 
• Admin + Security Clearance ≥ 5 → Full Access  
• Manager + Experience > 5 Years → Department Access  
• Employee + Experience > 2 Years → Limited Access  
• Guest → Read-Only Access  
• Inactive Account → No Access  
----------------------------------------------------
Sample Input 
Role: Admin 
Security Clearance: 6 
Account Status: Active 
Sample Output 
Access Level: FULL ACCESS
-----------------------------------------------------
'''


#coding starts here 
#input user data
print("-------------------------------------------")


role = input("Enter Role (Admin/Manager/Employee/Guest): ")
status = input("Enter Account Status (Active/Inactive): ")

if role.lower() not in ["admin", "manager", "employee", "guest"]:
    exit("Access Level: NO ACCESS")

if status.lower() == "inactive":
    exit("Access Level: NO ACCESS")

else:
    if role.lower() == "admin":
        clearance = int(input("Enter Security Clearance: "))
        if clearance >= 5:
            print("Access Level: FULL ACCESS")
        else:
            print("Access Level: NO ACCESS")

    elif role.lower() == "manager":
        experience = int(input("Enter Experience (Years): "))
        if experience > 5:
            print("Access Level: DEPARTMENT ACCESS")
        else:
            print("Access Level: NO ACCESS")

    elif role.lower() == "employee":
        experience = int(input("Enter Experience (Years): "))
        if experience > 2:
            print("Access Level: LIMITED ACCESS")
        else:
            print("Access Level: NO ACCESS")

    elif role.lower() == "guest":
        print("Access Level: READ-ONLY ACCESS")

    else:
        print("Invalid Role")

print("-------------------------------------------")

'''Output
-------------------------------------------
Enter Role (Admin/Manager/Employee/Guest): Admin
Enter Account Status (Active/Inactive): Active
Enter Security Clearance: 6
Access Level: FULL ACCESS
-------------------------------------------
'''