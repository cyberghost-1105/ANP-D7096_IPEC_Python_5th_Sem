'''to calculate compound interest'''

#inputing the data from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = int(input("Enter the time period (in years): "))
print("---------------------------------")

#displaying the input data
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time Period:", time, "years")
print("---------------------------------")

#calculating compound interest
compound_interest = principal * (1 + rate / 100) ** time - principal
print("Compound Interest:", compound_interest)
print("---------------------------------")

'''output:
Enter the principal amount: 1000
Enter the rate of interest (in %): 5
Enter the time period (in years): 2
---------------------------------
Principal Amount: 1000.0
Rate of Interest: 5.0 %
Time Period: 2 years
---------------------------------
Compound Interest: 102.5
---------------------------------
'''