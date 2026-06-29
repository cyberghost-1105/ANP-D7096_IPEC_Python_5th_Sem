''' Electricity Bill Analysis 
Problem Statement 
An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
Calculate and display: 
• Total units consumed  
• Average units consumed  
• Highest consumption  
• Lowest consumption 
'''

#coding starts here 

# Input number of houses
n = int(input("Enter the number of houses: "))

total = 0

# Input for the first house
units = int(input("Enter units consumed by House 1: "))

total = units
highest = units
lowest = units

# Input for remaining houses
for i in range(1, n + 1):
    units = int(input(f"Enter units consumed by House {i}: "))
    total += units

    if units > highest:
        highest = units

    if units < lowest:
        lowest = units

# Calculate average
average = total / n

# Display results
print("Total Units Consumed:", total)
print("Average Units Consumed:", average)
print("Highest Consumption:", highest)
print("Lowest Consumption:", lowest)

'''output
Enter the number of houses: 5
Enter units consumed by House 1: 120
Enter units consumed by House 2: 150
Enter units consumed by House 3: 100
Enter units consumed by House 4: 180
Enter units consumed by House 5: 140

Total Units Consumed: 690
Average Units Consumed: 138.0
Highest Consumption: 180
Lowest Consumption: 100'''