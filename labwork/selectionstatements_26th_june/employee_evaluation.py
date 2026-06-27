'''-------------------- Employee Performance Evaluation----------------------
Problem Statement 
An employee is evaluated using: 
• Project Score  
• Attendance Percentage  
• Client Feedback Score  
Rules: 
• Excellent → All scores above 90  
• Good → Scores above 75  
• Average → Scores above 60  
• Poor → Otherwise  
Additional Rule: 
• Attendance below 70% cannot receive more than Average rating.  
Sample Input 
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
Sample Output 
Performance Rating: Average 
Reason: Attendance below 70%'''

#coding starts here
#inputs data
print("-------------------------------------------")

project_score = int(input("Project Score: "))
attendance = int(input("Attendance Percentage: "))
client_feedback = int(input("Client Feedback Score: "))

#validating input data
if project_score <=0:
    exit("Enter valid Score")
if attendance <= 0:
    exit("Enter Valid Attendance")


# Check performance rating
if attendance < 70:
    print("Performance Rating: Average")
    print("Reason: Attendance below 70%")

elif project_score > 90 and attendance > 90 and client_feedback > 90:
    print("Performance Rating: Excellent")

elif project_score > 75 and attendance > 75 and client_feedback > 75:
    print("Performance Rating: Good")

elif project_score > 60 and attendance > 60 and client_feedback > 60:
    print("Performance Rating: Average")

else:
    print("Performance Rating: Poor")
print("-------------------------------------------")


'''Output:
-------------------------------------------
Project Score: 98
Attendance Percentage: 25
Client Feedback Score: 98
Performance Rating: Average
Reason: Attendance below 70%
-------------------------------------------
-------------------------------------------
Project Score: 54
Attendance Percentage: 89
Client Feedback Score: 25
Performance Rating: Poor
-------------------------------------------
'''