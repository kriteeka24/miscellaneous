import random

secret = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))

if guess == secret:
    print("🎉 Correct! You guessed it!")
elif guess > secret:
    print("Too high!")
else:
    print("Too low!")

print(f"The number was: {secret}")
