import random
num = 0
sco = 0
while num != 1 and sco < 5:
    input("Press the enter key to roll: ")
    num = random.randint(1, 6)
    print(f"You rolled a {num}")
    if num != 1:
        sco +=1

print(f"Your final score is {sco}")
if sco ==5:
    print("You won")