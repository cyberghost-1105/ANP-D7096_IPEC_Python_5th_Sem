'''-----------Voting Eligibility Checker----------------
write a program to check the whether a person is eligible for voting or not 
a person will be eligible for voting if his/her age is greater than or equal to 18 years.
-----------------------------------------------------------
Sample Input
Enter your age(in years): 20
Sample Output
You are eligible for voting.
----------------------------------------------------------'''

#Coding section 
#taking input from the user
print("----------------------------------------------------------")
age = int(input("Enter your age(in years): "))

#validating age input
if age <= 0:
    exit("Invalid input. Please enter a valid age.")    

#checking voting eligibility 
if age >= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")

print("----------------------------------------------------------")


'''Output:
Enter your age(in years): 20
You are eligible for voting.
----------------------------------------------------------
Enter your age(in years): 15
You are not eligible for voting.
----------------------------------------------------------'''