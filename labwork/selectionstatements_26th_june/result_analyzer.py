'''------------------------Online Examination Result Analyzer----------------------- 
Problem Statement 
A student appears in 5 subjects. 
Rules: 
• Minimum 40 marks in every subject to pass.  
• Distinction → Average ≥ 75  
• First Division→ Average ≥ 60  
• Second Division → Average ≥ 50  
• Pass  → Average ≥ 40  
• Fail if any subject score < 40  
-----------------------------------------
Sample Input 
Hindi : 85 
English : 78 
Mathematics : 82 
Science : 75 
Computer : 90 
Sample Output 
Average Marks: 82.0 
Result: PASS 
Classification: Distinction
-------------------------------------------
'''

#coding starts here 
#inputs the data

print("-------------------------------------------------")

hindi = int(input("Enter Hindi Marks: "))
english = int(input("Enter English Marks: "))
mathematics = int(input("Enter Mathematics Marks: "))
science = int(input("Enter Science Marks: "))
computer = int(input("Enter Computer Marks: "))

average = (hindi + english + mathematics + science + computer) / 5

print("Average Marks:", average)

# Check Pass/Fail
if (hindi < 40 or english < 40 or mathematics < 40 or science < 40 or computer < 40):
    print("Result: FAIL")
else:
    print("Result: PASS")

    # Classification
    if average >= 75:
        print("Classification: Distinction")
    elif average >= 60:
        print("Classification: First Division")
    elif average >= 50:
        print("Classification: Second Division")
    elif average >= 40:
        print("Classification: Pass")
print("-------------------------------------------------")

'''Output
-------------------------------------------------
Enter Hindi Marks: 85
Enter English Marks: 78
Enter Mathematics Marks: 82
Enter Science Marks: 75
Enter Computer Marks: 90
Average Marks: 82.0
Result: PASS
Classification: Distinction
-------------------------------------------------
'''