'''python program to calculate number of complete rows can be formed '''


#inputing the data

students = int(input("Enter total number of students: "))
students_per_row = int(input("enter minimum number of students in a row"))

#number of rows formed 

print("complete rows formed: ", students//students_per_row)