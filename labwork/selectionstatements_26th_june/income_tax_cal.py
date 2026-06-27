'''---------Income Tax Calculator---------
A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax  
• ₹5,00,001 to ₹10,00,000 → 10%  
• ₹10,00,001 to ₹20,00,000 → 20%  
• Above ₹20,00,000 → 30%  
Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
• Women taxpayers receive an additional 2% rebate on tax.  
Write a Python program to calculate the final tax amount payable. 
-----------------------------------------------------------------
Sample Input 
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F 
Sample Output 
Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0
------------------------------------------------------------------'''

#coding starts here 
#inputting salary, age from the user
print("______________________________________________________________")
print("---------Income Tax Calculator---------")
income = float(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (Male/Female): ")

#validating the input data
if income < 0:
    exit("Income cannot be negative. Enter a valid income.")
if age < 0:
    exit("Age cannot be negative. Enter a valid age.")
if gender.lower() != "male" and gender.lower() != "female":
    exit("Invalid gender. Enter 'Male' or 'Female'.")

#calculating tax based on income slabs
    #for inccome upto 5,00,000

if income <= 500000:
    tax = 0
    print("No tax for the Income up to ₹5,00,000")
    #for income between 5,00,001 to 10,00,000
elif income <= 1000000:
    #for female and senior citizens
    if gender.lower() == "female" and age >= 60:
        tax = (income - 500000) * 0.10
        print("Tax before rebate: ₹", tax)
        print("Senior Citizen Rebate:: ₹", (tax - (tax * 0.05)))
        print("Women Rebate: ₹", (tax - (tax * 0.02)))
        print("Final Tax Payable: ₹", (tax - (tax * 0.07)))
        #for female taxpayers
    elif gender.lower() == "female" :
        tax = (income - 500000) * 0.10
        print("Tax before rebate: ₹", tax)
        print("Tax for Female taxpayers after rebate: ₹", (tax - (tax * 0.02)))
        #for senior citizens taxpayers
    elif age >= 60:
        tax = (income - 500000) * 0.10
        print("Tax before rebate: ₹", tax)
        print("Tax for Senior Citizens after rebate: ₹", (tax - (tax * 0.05)))
        #for normal taxpayers
    else:
        tax = (income - 500000) * 0.10
        print("Income Tax: ₹", tax)

    #for income between 10,00,001 to 20,00,000
elif income <= 2000000:
      #for female and senior citizens
    if gender.lower() == "female" and age >= 60:
        tax = (income - 500000) * 0.20
        print("Tax before rebate: ₹", tax)
        print("Senior Citizen Rebate:: ₹", (tax - (tax * 0.05)))
        print("Women Rebate: ₹", (tax - (tax * 0.02)))
        print("Final Tax Payable: ₹", (tax - (tax * 0.07)))
     #for female taxpayers
    elif gender.lower() == "female" :
        tax = (income - 500000) * 0.20
        print("Tax before rebate: ₹", tax)
        print("Tax for Female taxpayers after rebate: ₹", (tax - (tax * 0.02)))
       #for senior citizens taxpayers
    elif age >= 60:
        tax = (income - 500000) * 0.20
        print("Tax before rebate: ₹", tax)
        print("Tax for Senior Citizens after rebate: ₹", (tax - (tax * 0.05)))
       #for normal taxpayers
    else:
        tax = (income - 500000) * 0.20
        print("Income Tax: ₹", tax)

    #for income above 20,00,000
elif income > 2000000:
        #for female and senior citizens
    if gender.lower() == "female" and age >= 60:
        tax = (income - 500000) * 0.30
        print("Tax before rebate: ₹", tax)
        print("Senior Citizen Rebate:: ₹", (tax - (tax * 0.05)))
        print("Women Rebate: ₹", (tax - (tax * 0.02)))
        print("Final Tax Payable: ₹", (tax - (tax * 0.07)))
        #for female taxpayers    
    elif gender.lower() == "female" :
        tax = (income - 500000) * 0.30  
        print("Tax before rebate: ₹", tax)
        print("Tax for Female taxpayers after rebate: ₹", (tax - (tax * 0.02)))
        #for senior citizens taxpayers
    elif age >= 60:
        tax = (income - 500000) * 0.30
        print("Tax before rebate: ₹", tax)
        print("Tax for Senior Citizens after rebate: ₹", (tax - (tax * 0.05)))
        #for normal taxpayers
    else:
        tax = (income - 500000) * 0.30
        print("Income Tax: ₹", tax)
print("______________________________________________________________")


'''output:
______________________________________________________________
---------Income Tax Calculator---------
Enter Annual Income: 1200000
Enter Age: 65
Enter Gender (Male/Female): F
Tax before rebate: ₹ 70000.0
Senior Citizen Rebate:: ₹ 66500.0
Women Rebate: ₹ 68600.0
Final Tax Payable: ₹ 65100.0
______________________________________________________________'''
