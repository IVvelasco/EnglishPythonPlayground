# Level 023

# -------------------------------
# -- INTERACTION WITH THE USER --
# -------------------------------

name = input("Type your name here: ")
last_name = input("Type your lastname here: ")
age = int(input("Now type your age: "))
food = input("Type your favorite food: ")
collor = input("Now your favorite collor: ")
hobbies = input("Insert here your hobbies: ")
animal = input("Do you have a pet? [y/n]: ")
if animal == 'y':
    animal = "You have a pet!"
else:
    animal ="Oh, you don't have a pet :c "

print(f"Hello {name} {last_name}, your age is {age}, your favorite food is {food} and your hobbies are {hobbies}. About pet: {animal} ")