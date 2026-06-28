'''----------------Electricity Billing System-------------------------
Smart Electricity Billing System 
Problem Statement 
Calculate electricity bill using: 
Units Rate 
0-100 ₹5/unit 
101-300 ₹7/unit 
Above 300 ₹10/unit 
Additional Rules: 
• Commercial consumers pay 20% extra.  
• Bills above ₹5000 attract 5% surcharge.  
• Senior citizens receive 10% discount. 
-------------------------------------------- 
Sample Input 
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial 
Senior Citizen (Y/N): Y 
Sample Output 
Base Bill: ₹4500 
Commercial Charge: ₹900 
Surcharge: ₹270 
Senior Citizen Discount: ₹567 
Final Bill Amount: ₹5103
-------------------------------------------
'''


#CODING STARts here
#input user data

print("--------------------------------------------------")

units = int(input("Enter Units Consumed: "))
consumer_type = input("Enter Consumer Type (Residential/Commercial): ")
senior = input("Senior Citizen (Y/N): ")

# Calculate Base Bill
if units <= 100:
    base_bill = units * 5
elif units <= 300:
    base_bill = (100 * 5) + ((units - 100) * 7)
else:
    base_bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

print("Base Bill: ₹", base_bill)

# Commercial Charge
commercial_charge = 0
if consumer_type.lower() == "commercial":
    commercial_charge = base_bill * 0.20

print("Commercial Charge: ₹", commercial_charge)

# Bill after Commercial Charge
bill = base_bill + commercial_charge

# Surcharge
surcharge = 0
if bill > 5000:
    surcharge = bill * 0.05

print("Surcharge: ₹", surcharge)

bill = bill + surcharge

# Senior Citizen Discount
discount = 0
if senior.upper() == "Y":
    discount = bill * 0.10

print("Senior Citizen Discount: ₹", discount)

# Final Bill
final_bill = bill - discount

print("Final Bill Amount: ₹", final_bill)
print("--------------------------------------------------")


'''Output
--------------------------------------------------
Enter Units Consumed: 450
Enter Consumer Type (Residential/Commercial): Commercial
Senior Citizen (Y/N): Y
--------------------------------------------------
Base Bill: ₹ 3000
Commercial Charge: ₹ 600.0
Surcharge: ₹ 0
Senior Citizen Discount: ₹ 360.0
Final Bill Amount: ₹ 3240.0
--------------------------------------------------'''

