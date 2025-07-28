# Level 032

#  ----------------------------
#  -- TRYING WITH def main() --
#  ----------------------------

def main():
    print("*****************************************************")
    print("*     TEST TO FIND OUT IF YOU ARE A VAMPIRE         *")
    print("*****************************************************")

    probability = int(0)
    bite = input("You were recently bitten by a vampire? [y/n] ")
    if bite == 'y':
        probability += 1 
    elif bite == 'n':
        probability += 0
    else:
        print("Insert a valid answer!")

    age = int(input("Your age: "))
    if age >= 100:
        probability += 1
    elif age <=100:
        probability += 0 
    else:
        print("Insert a valid answer!")

    garlic = input("Garlic scares you: [y/n] ")
    if garlic == 'y':
        probability += 1 
    elif garlic == 'n':
        probability += 0
    else:
        print("Insert a valid answer!")

    live = input("Do you live in a medieval castle? [y/n] ")
    if live == 'y':
        probability += 1 
    elif live == 'n':
        probability += 0
    else:
        print("Insert a valid answer!")

    crucifix = input("You feel discomfort around crucifixes? [y/n] ")
    if crucifix == 'y':
        probability += 1 
    elif crucifix == 'n':
        probability += 0
    else:
        print("Insert a valid answer!")

    sun = input("You avoid the sun? [y/n] ")
    if sun == 'y':
        probability += 1
    elif sun == 'n':
        probability += 0
    else:
        print("Insert a valid answer!")

    church = input("You avoid Churchs? [y/n] ")
    if church == 'y':
        probability += 1
    elif church == 'n':
        probability += 0
    else:
        print("Insert a valid answer!")

    blood = input("When you see blood, your feel thirst? [y/n] ")
    if blood == 'y':
        probability += 1 
    elif blood == 'n':
        probability += 0 
    else: 
        print("Insert a valid answer!")

    if probability >= 5:
        print("VAMPIRE!!!")
    else:
        print("You're just a EMO")
if __name__ == "__main__":
    main()