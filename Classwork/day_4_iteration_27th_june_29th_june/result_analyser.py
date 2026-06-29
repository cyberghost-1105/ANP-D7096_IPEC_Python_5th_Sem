''' Student Result Analyzer 
Problem Statement 
A teacher wants to analyze the marks of N students. 
Accept the marks of each student (out of 100). 
Finally display: 
• Highest Marks  
• Lowest Marks  
• Average Marks  
• Number of students who passed (Marks ≥ 40)  
• Number of students who scored distinction (Marks ≥ 75)'''

#coding starts here 

# Input number of students
n = int(input("Enter the number of students: "))

# Input marks of first student
marks = float(input("Enter marks of Student 1: "))

highest = marks
lowest = marks
total = marks

passed = 0
distinction = 0

if marks >= 40:
    passed += 1

if marks >= 75:
    distinction += 1

# Input marks of remaining students
for i in range(2, n + 1):
    marks = float(input(f"Enter marks of Student {i}: "))

    total += marks

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

    if marks >= 40:
        passed += 1

    if marks >= 75:
        distinction += 1

# Calculate average
average = total / n

# Display results
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Number of students passed:", passed)
print("Number of students with distinction:", distinction)


'''output
Enter the number of students: 5
Enter marks of Student 1: 85
Enter marks of Student 2: 62
Enter marks of Student 3: 39
Enter marks of Student 4: 75
Enter marks of Student 5: 28

Highest Marks: 85.0
Lowest Marks: 28.0
Average Marks: 57.8
Number of students passed: 3
Number of students with distinction: 2'''