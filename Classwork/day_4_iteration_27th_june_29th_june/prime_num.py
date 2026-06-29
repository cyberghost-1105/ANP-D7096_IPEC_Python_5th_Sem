'''Count Prime Numbers in a Range 
Problem Statement 
Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and finally display the total number of prime numbers 
found.'''

#coding starts here 
#input from the user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
            count += 1

print("Total prime numbers:", count)


'''output
Enter ending number: 32
3
5
7
11
13
17
19
23
29
31
Total prime numbers: 10'''