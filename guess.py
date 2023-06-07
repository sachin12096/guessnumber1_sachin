import random

number = random.randrange(1, 10)
print(number)
guess_count = 0
guess_limit = 3

while True:
    if guess_count < guess_limit:
        guess = int(input("enter ur guess: "))
        guess_count += 1
        if guess == number:
            print("u Win")
            break
    else:
        print("Out of guesses u lose: ")
        break
    
    if guess > number:
        print("ur guess is higer than the number")
    elif guess < number:
        print("ur guess is lower than the number:")
