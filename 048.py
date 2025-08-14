# Level 048

# ------------------------------
# -- QUESTIONARY WITH LOOPING --
# ------------------------------

print("What is my favorite movie trilogy?")
print("a) The Matrix")
print("b) The Hunger Games")
print("c) Twilight")
guess = input("R: ")

while guess != 'a':
    print("Nah ah, wrong!")
    guess = input("Try again: ")
else:
    print("Congrats!")    
