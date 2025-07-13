# Level 006

# ---------------
# -- IF - ELSE --
# ---------------

# Level 006

print("Welcome to the menu that averages your grades!")

math = float(input("Your grade in Math: "))
geography = float(input("Your grade in Geography: "))
pshysics = float(input("Your grade in Physics: "))
english = float(input("Your grade in English: "))
chemistry = float(input("Your grade in Chemistry: "))
history = float(input("Your grade in History: "))
literature = float(input("Your grade in Literature: "))
arts = float(input("Your grade in Arts: "))

total = math + geography + pshysics + english + chemistry + history + literature + arts
average = total / 8 

if average  >= 70:
    print("Congrats, you pass! Your average is: ", average)
else: 
    print("Oh, you shall not pass! Your average is: ", average)
