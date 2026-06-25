''' To calculate simple interest '''
#input of principal from the user
principal = float(input("Enter the principal (in Rs): "))
#validating the principal amount
if principal < 0:
    exit("Principal amount cannot be negative.")
#input of rate from the user
rate = float(input("Enter the rate of interest(in %): "))
#validating the rate of interest
if rate < 0:
    exit("Rate of interest cannot be negative.")
#input of time from the user
time = int(input("Enter the time period(in year): "))
#validating the time period
if time < 0:
    exit("Time period cannot be negative.")
#-----------------------------------------------------
#Displaying data to the user
print("Principal: Rs", principal)
print("Rate of Interest: ", rate, "%")
print("Time Period: ", time, "year")
#-----------------------------------------------------
#displaying simple interest
print("Simple Interest: Rs", (principal * rate * time) / 100)


'''Output:
Enter the principal (in Rs): 10000
Enter the rate of interest(in %): 5
Enter the time period(in year): 2
Principal: Rs 10000.0
Rate of Interest:  5.0 %
Time Period:  2 year
Simple Interest: Rs 1000.0'''
