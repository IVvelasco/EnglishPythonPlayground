# Level 010

# -------------------
# -- Using Looping --
# -------------------

import random

number = random.randint(1, 1000)
did = False

while not did:
    guess = int(input("Choose a random number between 1 and 1000: "))

    if number == guess:
        print("Congratulations, your chances were weaks but you did it!")
        acertou = True
    else: 
        print("Don't give up, try again!")

    # Bônus para o jogador

        if guess < number:
            print("Try high!")
        else: 
            print("Try low!")