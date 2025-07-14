# Level 009 

# ---------------------------------
# -- Using import random choices --
# ---------------------------------

import random
number = random.randint(1, 1000)
guess = int(input("Choose a random number between 1 and 1000: "))

if number == guess:
    print("Congratulations, your chances were weaks but you did it!")
else:
    print(f"The answer was: ", number)
    print("Don't give up, try again!")
