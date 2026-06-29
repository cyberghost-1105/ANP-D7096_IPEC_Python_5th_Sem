'''Multiplication Table Generator 
Problem Statement 
Write a Python program that accepts a number from the user and displays its multiplication table up to 
20. 
Sample Output 
Enter Number: 8 
 
8 x 1 = 8 
8 x 2 = 16 
... 
8 x 20 = 160'''

#coding starts here 
#input from the user

num = int(input("Enter number: "))

for i in range (1, 21):
    print(num, "x", i, "=", num*i)

'''output
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
4 x 11 = 44
4 x 12 = 48
4 x 13 = 52
4 x 14 = 56
4 x 15 = 60
4 x 16 = 64
4 x 17 = 68
4 x 18 = 72
4 x 19 = 76
4 x 20 = 80
'''