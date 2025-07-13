# Level 005

# ------------------
# -- IF-ELIF-ELSE --
# ------------------

ask = input("Are you having a headache? R: ")
answer = ask
if answer == 'Yes':
    print("Go drink some water!")
elif answer == 'YES':
    print("Go drink some water!")
elif answer == 'yes':
    print("Go drink some water!")
else: 
    print("Thanks God!")