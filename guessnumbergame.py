#SB This is random number program and We have to guess it

import random

print("This is random number game. Guess it!")
print("Please specify the range for the random numbers.")
first = int(input("First range : "))
second = int(input("Second range : "))

count = 10

print("Now Guess it number! You have 10 chance.")
purpose = random.randint((first), (second))

while True:
    guess = int(input("Please enter your number : "))
    if guess < purpose:
        print("It's a value larger than that number.")
        count -= 1
        print(f"Now you have {count} chance.")
    elif guess > purpose:
        print("It's a value smaller than that value.")
        count -= 1
        print(f"Now you have {count} chance.")
    elif guess == purpose:
        print("You are Win!")
        break
    
    if count == 0:
        print("You lose!")
        break
    
    #I made Guess number game! random number! I was import random module and i used! Coding is so fun. SB Wed/Feb/4/2026/ 12:53pm 