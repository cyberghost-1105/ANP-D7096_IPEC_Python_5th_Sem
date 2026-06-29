'''Shopping Cart Billing System 
Problem Statement 
A supermarket allows a customer to purchase multiple products. 
The customer first enters the number of products. 
For each product, enter: 
• Product Name  
• Quantity  
• Price per Unit  
Finally display: 
• Individual Product Cost  
• Total Bill Amount  
• Most Expensive Product  
• Cheapest Product  
• Average Product Cost
'''

#coding starts here 
# Input number of products
n = int(input("Enter the number of products: "))

# Input details of the first product
name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))

cost = quantity * price

total_bill = cost
highest_cost = cost
lowest_cost = cost
expensive_product = name
cheapest_product = name

print(f"{name} Cost = ₹{cost}")

# Input details of remaining products
for i in range(2, n + 1):
    print(f"\nProduct {i}")

    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit: "))

    cost = quantity * price

    print(f"{name} Cost = ₹{cost}")

    total_bill += cost

    if cost > highest_cost:
        highest_cost = cost
        expensive_product = name

    if cost < lowest_cost:
        lowest_cost = cost
        cheapest_product = name

# Calculate average product cost
average_cost = total_bill / n

# Display results
print("\n----- Shopping Bill Summary -----")
print("Total Bill Amount: ₹", total_bill)
print("Most Expensive Product:", expensive_product, "(₹", highest_cost, ")")
print("Cheapest Product:", cheapest_product, "(₹", lowest_cost, ")")
print("Average Product Cost: ₹", average_cost)


'''output
Enter the number of products: 3

Enter Product Name: Rice
Enter Quantity: 2
Enter Price per Unit: 50
Rice Cost = ₹100.0

Product 2
Enter Product Name: Oil
Enter Quantity: 3
Enter Price per Unit: 180
Oil Cost = ₹540.0

Product 3
Enter Product Name: Soap
Enter Quantity: 5
Enter Price per Unit: 30
Soap Cost = ₹150.0

----- Shopping Bill Summary -----
Total Bill Amount: ₹ 790.0
Most Expensive Product: Oil (₹ 540.0 )
Cheapest Product: Rice (₹ 100.0 )
Average Product Cost: ₹ 263.33'''