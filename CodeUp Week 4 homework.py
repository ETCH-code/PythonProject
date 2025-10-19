import random
num = random.randint(1,100)

counter = 0
answer = False
guess = 0

#print(num)
while answer == False:
    guess = int(input("Guess how much money Oscar has: "))
    counter += 1
    if guess < num:
        print("Guess higher!")
        answer = False
    elif guess > num:
        print("Guess lower!")
        answer = False
    elif guess == num:
        print(f"You guessed the correct amount of money in {counter} guesses!")
        answer = True