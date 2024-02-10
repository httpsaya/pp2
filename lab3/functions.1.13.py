import random
def tr():
    a = str(input("Hello! What is your name?"))
    print("Well,",a,", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    secret = random.randint(1,20)
    attemp = 0
    while True:
        attemp += 1
        guess = int(input())
        if secret > guess:
            print("Your guess is too low.")
            print("Take a guess.")
        elif secret < guess:
            print("Your guess is too high")
            print("Take a guess.")
        else:
            print("Good job,",a,"! You guessed my number in",attemp,"guesses!")
            break
tr()        