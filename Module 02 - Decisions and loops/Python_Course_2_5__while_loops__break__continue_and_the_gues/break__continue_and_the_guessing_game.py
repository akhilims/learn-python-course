# break, continue and the guessing game
# Every cell of the notebook, in order, as one script (run: python break__continue_and_the_guessing_game.py)

# ## break: leave a loop at once

for number in range(1, 10):
    if number == 4:
        break
    print(number)

# ## continue: skip one round

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# ## The guessing game: while, input, if and break

secret = 6
while True:
    guess = int(input("Guess a number 1-10: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("You got it!")
        break

# ## The game with an attempts counter

secret = 4
tries = 0
while True:
    tries = tries + 1
    guess = int(input("Guess a number 1-10: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("You got it!")
        break
print("Attempts used:", tries)
