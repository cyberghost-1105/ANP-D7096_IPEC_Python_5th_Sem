'''Number Guessing Game 
Problem Statement 
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct. 
'''
#coding start here 
# Secret number
secret_number = 37

# First guess
guess = int(input("Enter your guess: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    guess = int(input("Enter your guess: "))

print("Correct! You guessed the number.")