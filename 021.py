# Level 021

# ---------------------------------
# -- AGE GROUP WITH IF-ELIF-ELSE --
# ---------------------------------

# Age group based on Brazilian laws

age = int(input("Please enter your age (Use only int numbers): "))

if age <= 12:
    print("According to the official Brazilian classification, your age group is: Child!")
elif age <=19:
    print("Acording to the official Brazilian classification, your age group is: Teenager")
elif age <= 59:
    print("According to the official Brazilian classification, your age group is: Adult!")
else: 
    print("According to the official Brazilian classification, your age is: Elderly!")