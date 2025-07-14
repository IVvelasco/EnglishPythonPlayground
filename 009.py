# Level 009 

# ---------------------------------
# -- Using import random choices --
# ---------------------------------

import random
numero = random.randint(1, 1000)
palpite = int(input("Choose a random number between 1 and 1000: "))

if numero == palpite:
    print("Congratulations, your chances were weaks but you did it!")
else:
    print(f"The answer was: ", numero)
    print("Don't give up, try again!")