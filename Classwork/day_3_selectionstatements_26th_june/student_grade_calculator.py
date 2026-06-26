'''-----------------STUDENT GRADE CALCULATOR PROGRAM-----------------
A school assigns grades based on the marks obtained by students according to the following criteria: 
• Marks 90 and above → Grade A  
• Marks 75 to 89 → Grade B  
• Marks 50 to 74 → Grade C  
• Below 50 → Grade F 
----------------------------------------------------------
Write a Python program to accept marks from the user and display the corresponding grade. 
Sample Input 
Enter Marks: 92 
Sample Output 
Grade A 
Sample Input 
Enter Marks: 80 
Sample Output 
Grade B 
Sample Input 
Enter Marks: 65 
Sample Output 
Grade C 
Sample Input 
Enter Marks: 35 
Sample Output 
Grade F
---------------------------------------------------------- '''


#Coding starts here
#inputs the data from the user
marks = float(input("Enter marks between 0 and 100: "))
#validating the marks obtained
if marks < 0 or marks > 100:
    exit("Invalid input. ")

print("----------------------------------------------------------")

#determining grade based on the marks obtained
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")
print("----------------------------------------------------------")


'''Output:
Enter Marks: 92
Grade A
----------------------------------------------------------
Enter Marks: 80
Grade B
----------------------------------------------------------
Enter Marks: 65
Grade C
----------------------------------------------------------
Enter Marks: 35
Grade F
----------------------------------------------------------
Enter Marks: 105
Invalid input. Please enter marks between 0 and 100.
----------------------------------------------------------'''