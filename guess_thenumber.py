#this is a guess number game
import random
secret_number = random.randint(1, 5)
print("I am thinking of a number between 1 and 20")
print("Take a guess")
for guessestaken in range(1, 7):
    guess = int(input())
    if guess < secret_number:
        print("Your guess is too low.")
        continue
    elif guess > secret_number:
        print("Your guess is too high")
        continue
    else:
        break

if guess == secret_number:
    print("Good job! You guessed my number in " + str(guessestaken) + " guesses!")
else:
    print("Nope i wa thinking of the number " + str(secret_number))