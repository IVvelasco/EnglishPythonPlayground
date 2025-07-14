# Level 008

# --------------------------
# -- Playing with strings --
# --------------------------


"""
A simple and efficient way to test whether a phrase or word is a palindrome: compare the string ::+1 with ::-1 and see if they match
"""

frase = input("Is it a palindrome? Type and find out:")

if frase == frase [::-1]:
    print(f"Uau, it's a palindrome!")
else:
    print(f"It wasn't this time!")
