import random
n = 100
to_be_guess = int(n * random.random()) + 1
guess = 0

while guess != to_be_guess:
    guess = int(input("Guess the number: "))
    if guess > 0:
        if guess > to_be_guess:
            print("Number is too large")
        elif guess < to_be_guess:
            print("Number is too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulations to guessed correct!")