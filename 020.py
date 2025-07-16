# Level 020

#  ---------------
#  -- SHOPPING  --
#  ---------------

import random

print("===================================================")
print("= Let's simulate a little stroll around the mall! =")
print("===================================================")
print("")

entrance = ["Uber brought you", "went by bus", "got a ride", "went walking", "gave spawn", "went by motorcycle"]
task0 = print(f"You went to the mall because {random.choice(entrance)} ")
if random.choice(entrance) == 'Uber brought you':
    print("It was very expensive but the Uber was a nice person")
elif random.choice(entrance) == "went by bus":
    print("You did a bad trip and feel tired")
elif random.choice(entrance) == "got a ride":
    print("The funny part is that you don't even know the guy that gave you the ride")
elif random.choice(entrance) == "went walking":
    print("And now your feet hurt. What was your idea of walking 10 km in high heels?")
elif random.choice(entrance) == "gave spawn":
    print("You koff and give spawn no shopping")
elif random.choice(entrance) == "went by motorcycle":
    print("And got a speeding ticket.")
print("")

floor0 = ["take the stairs", "wait for the elevator", "do parkour", "allow a stranger to carry you on their back", "hide in a baby stroller", "go up a ramp"]
print(f"You went to the ground floor and decided to {random.choice(floor0)}")
if random.choice(floor0) == "take the stairs":
    print("That was the cardio of the day")
elif random.choice == "wait for the elevator":
    print("You were stuck in the elevator for 30 minutes")
elif random.choice(floor0) == "do parkour":
    print("You fell badly and luckily you didn't break anything.")
elif random.choice(floor0) == "allow a stranger to carry you on their back":
    print("You should rethink your choices, young man")
elif random.choice(floor0) == "hide in a baby stroller":
    print("It only worked because it was a reborn baby")
elif random.choice(floor0) == "go up a ramp":
    print("You ended up in the wrong place and had to retrace your steps.")
print("")

floor1 = ["the women's clothing store", "the men's clothing store", "the shoes store", "the electronics store", "the accessories and handbags store", "a bookstore"]
print(f"Inside the mall you chose to go straight to {random.choice(floor1)}")
if random.choice(floor1) == "the women's clothing store":
    print("you took the opportunity to buy some panties")
elif random.choice(floor1) == "the men's clothing store":
    print("you bought a nice belt")
elif random.choice(floor1) == "the shoes store":
    print("You told the salesperson you were just looking around")
elif random.choice(floor1) == "the electronics store":
    print("You maxed out your card and it was worth every penny")
elif random.choice(floor1) == "the accessories and handbags store":
    print("You thought everything was very expensive and of poor quality but you still bought a wallet")
elif random.choice(floor1) == "a bookstore":
    print("You smelled all the books and the salesman asked you to leave.")
print("")

floor2 = ["visited the children's clothing store", "found a lost dog", "found a lost cat", "stopped on one of the massage chairs", "saw your friend's boyfriend with another woman", "had difficulty using the escalator"]
if random.choice(floor2) == "Visited the children's clothing store":
    print("Now your reborn baby has new clothes!")
elif random.choice(floor2) == "find a lost dog":
    print("The dog bit you, it was a huge mess to find the owner but at least you didn't need to get any vaccines")
elif random.choice(floor2) == "found a lost cat":
    print("You and your new cat went to the pet shop for a complete treatment.!")
elif random.choice(floor2) == "stopped on one of the massage chairs":
    print("The masseuse asked for your phone number and you ran away")
elif random.choice == "saw your friend's boyfriend with another woman":
    print("You took a lot of photos and your friend got into an Uber to catch him in the act.")
elif random.choice(floor2) == "had difficulty using the escalator":
    print("You had to use the normal stairs and arrived at the food court almost out of breath.")
print("")

floor3 = ["eat a hamburger", "eat home-cooked food", "drink a milkshake", "don't eat anything", "go straight to dessert", "order 10 esfirras", "eat a whole pizza"]
print(f"Finally you're in the loved food court, you decide {random.choice(floor3)}")
if random.choice(floor3) == "eat a hamburger":
    print("Tasty but very expensive")
elif random.choice(floor3) == "eat home-cooked food":
    print("You realized it was just overpriced frozen food")
elif random.choice(floor3) == "drink a milkshake":
    print("You are lactose intolerant and had to run to the bathroom.")
elif random.choice(floor3) == "don't eat anything":
    print("Saving is good but your sugar level is too low")
elif random.choice(floor3) == "go straight to dessert":
    print("Who hasn't? The dessert was delicious.")
elif random.choice(floor3) == "order 10 esfirras":
    print("You ordered more 10 for eat at home")
elif random.choice(floor3) == "eat a whole pizza":
    print("Too bad the pizzeria was closed")