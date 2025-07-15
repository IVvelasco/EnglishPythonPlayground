# Level 011

# ------------------
# -- Using Import --
# ------------------

import random 
"""
Mini Game based on the school games we have in Brazil, like how many children you will have, who you will marry, etc.
"""
age = random.randint(18,100)
print(f"Age you got married: {age}") # I'm Brazil if you have 18 you can, maybe in other countrys it can change so adapt to your country

number = random.randint(1, 1000)
print(f"Number of dates you had before finding the right person: {number}")

local = ["Park", "Japanese Restaurant", "Cinema", "Apartment", "Italian Restaurant", "Food Truck", "Soccer Stadium", "Shopping Mall"]
print(f"On the day of the meeting, you went to a: {random.choice(local)}")

initial = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(f"Your soulmate's name starts with the letter: {random.choice(initial)}")

rizz = ["Oh Moon, I want to love you", "In a shower of kisses I go out without an umbrella", "You are my Sabrina Carpender song", "Are you gringo?", "I want my next zip code to be your house", "I'm not a pirate, but if you want, you can walk the plank", "Shall we watch Netflix at my house?", "I looked up perfection in the dictionary and in the examples I saw a picture of you", "What if we ran away together?", "Pspspspspspspspspspssp, kitty kitty", "Phew, phew, phew"]
print(f"Him whisper at your ears: {random.choice(rizz)}")

excuse = ["My fish is drowning", "I forgot the iron was on", "I forgot I can't take off my electronic ankle bracelet", "I forgot to vacuum the carpet", "Today is my hamster's birthday", "My grandmother is at bingo and I had to pick her up", "My wife is calling me", "I need to go play the numbers game before the booth closes", "The voices told me you're a potato", "I have a meeting later", "It feels like I'm dreaming so I'm going to try to fly", "Someone needs to teach my parrot some bad words", "I forgot I'm a priest and today I'm having a baptism", "I forgot where I parked the car, I'll be right back", "I have to watch a replay of the soccer team Botafogo beating PSG", "I'm out of silk"]
print(f"The excuse your soulmate gave for leaving the first date was: {random.choice(excuse)}")

hour_am = random.randint(1, 12)
minutes = random.randint(1, 60)
print(f"The date started around {hour_am} and {minutes}")

hour_pm = random.randint(1, 12)
minutes = random.randint(1, 60)
print(f"and over at {hour_pm} and {minutes}")

religion = ["Catholicism", "Islam", "Umbandista", "Spiritist", "Buddhist", "Hindu", "Shintoism", "Evangelical", "Judaism", "Confucianism", "Wicca", "Satanism", "Young Mystic", "Astrologer", "Tarotologist"]
print(f"To get married you converted to: {random.choice(religion)}")

disappointment = ["Grandma", "Manuel from the Bakery", "Computer", "Russian Hacker", "Mother", "Father", "Ex", "Friends", "Distant Relatives", "Cousin", "Best Friend", "Neighbor", "Old Radio Patrol", "Bakery Guy", "Cat", "Neighbor's Dog", "Best Friend", "Robber", "Fair Priest", "Peanut Seller", "Ex-Boss", "Hotel Manager", "Friend You Owe Money To", "Manicurist", "Old Man from Havan"]
print(f"Who was most disappointed with the wedding?: {random.choice(disappointment)}")

testemunha = ["Grandma", "Manuel from the Bakery", "Computer", "Russian Hacker", "Mother", "Father", "Ex", "Friends", "Distant Relatives", "Cousin", "Best Friend", "Neighbor", "Old Radio Patrol", "Bakery Guy", "Cat", "Neighbor's Dog", "Best Friend", "Robber", "Fair Priest", "Peanut Seller", "Ex-Boss", "Hotel Manager", "Friend You Owe Money To", "Manicurist", "Old Man from Havan"]
print(f"Who served as a witness at the time of signing: {random.choice(testemunha)}")

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(f"The wedding took place in the month of: {random.choice(month)}")

game = ["Russian Roulette", "UNO", "Truco","Chess", "Strip Poker", "Soccer", "Chess", "Kama Sutra", "Frescobol", "Blind Man's Buff", "Tag", "Hide and Seek", "Checkers", "RPG", "Video Game", "Any Steam Game", "BlackJack", "Poker", "Uno", "Truco", "Board Games", "Truth or Dare"]
print(f"Even after married you guys like to play {random.choice(game)} together")






