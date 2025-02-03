from random import randint

def guess_the_number():
    print("Hello! What is your name?")
    name = input() 
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess.\n"))
        sum+=1
        if guess == number:
            run = False
            print(f"\nGood job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("\nYour guess is too high.")
        else:
            print("\nYour guess is too low")

guess_the_number()