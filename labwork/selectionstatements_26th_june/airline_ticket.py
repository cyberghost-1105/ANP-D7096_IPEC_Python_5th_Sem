'''---------------Airline Ticket Pricing Engine -------------------
Problem Statement 
An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  
Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  
Calculate the final ticket fare. 
----------------------------------------------
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0
-----------------------------------------------
'''


#coding starts here 
#input the user data
print("----------------------------------------------------")
age = int(input("Enter Passenger age: "))
business_class = input("Business Class(Y/N): ")
window_seat = input("Window Seat (Y/N): ")
weekend_travel = input("Weekend Travel(Y/N): ")

#validaring input 
if age < 0:
    exit("Enter valid age")
    
#setting base fare
base_fare = 5000 

#validating ticket conditions
if business_class.lower() == "y" and window_seat.lower() == "y" and weekend_travel.lower() == "y":
    print("Base Fare: ₹", base_fare)
    base_fare+= 4500
    print("Additional Charges: ₹", 4500)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
elif business_class.lower() == "y" and window_seat.lower() == "y" and weekend_travel.lower() == "n":
    print("Base Fare: ₹",base_fare)
    base_fare += 3500
    print("Additional Charges: ₹", 3500)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
elif business_class.lower() == "y" and window_seat.lower() == "n" and weekend_travel.lower() == "n":
    print("Base Fare: ₹",base_fare)
    base_fare += 1500
    print("Additional Charges: ₹", 1500)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
elif business_class.lower() == "y" and window_seat.lower() == "n" and weekend_travel.lower() == "y":
    print("Base Fare: ₹", base_fare)
    base_fare += 4000
    print("Additional Charges: ₹", 4000)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
    print("Final Ticket Fare: ₹", base_fare)
elif business_class.lower() == "n" and window_seat.lower() == "n" and weekend_travel.lower() == "y":
    print("Base Fare: ₹", base_fare)
    base_fare += 1000
    print("Additional Charges: ₹", 1000)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
elif business_class.lower() == "n" and window_seat.lower() == "y" and weekend_travel.lower() == "y":
    print("Base Fare: ₹", base_fare)
    base_fare += 1500
    print("Additional Charges: ₹", 1500)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
elif business_class.lower() == "n" and window_seat.lower() == "y" and weekend_travel.lower() == "n":
    print("Base Fare: ₹", base_fare)
    base_fare += 500
    print("Additional Charges: ₹", 500)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)
else:
    print("Base Fare: ₹", base_fare)
    if age <= 12:
        print("Child Discount : 50%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.5)))
    elif age >= 60:
        print("Senior citizen Discount: 20%")
        print("Final Ticket Fare: ₹", (base_fare - (base_fare * 0.2)))
    else:
        print("Final Ticket Fare: ₹", base_fare)

print("----------------------------------------------------------")



'''Output:
----------------------------------------------------
Enter Passenger age: 65
Business Class(Y/N): y
Window Seat (Y/N): n 
Weekend Travel(Y/N): n
Base Fare: ₹ 5000
Additional Charges: ₹ 1500
Senior citizen Discount: 20%
Final Ticket Fare: ₹ 5200.0
----------------------------------------------------------
----------------------------------------------------
Enter Passenger age: 25
Business Class(Y/N): y
Window Seat (Y/N): y
Weekend Travel(Y/N): n
Base Fare: ₹ 5000
Additional Charges: ₹ 3500
Final Ticket Fare: ₹ 8500
----------------------------------------------------------'''




