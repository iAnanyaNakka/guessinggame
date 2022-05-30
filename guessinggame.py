import random
chance = 0
r = random.randint(1,9)
print("Number Guessing Game")
while chance < 5:
    guess = int(input(" Enter a number between 1 & 9 : "))
    if guess == r :
        print("Congratulations! You Won!") 
    if guess > r :
        print("Your guess is too high")
    if guess < r :
        print("Your guess is too less")
    chance = chance + 1


if not chance < 5:
    print("You lose! The number is ", r)7