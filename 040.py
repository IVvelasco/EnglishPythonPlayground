# Level 040

#  ------------------------------
#  -- CRIPTOGRAPHY WITH RANDOM --
#  ------------------------------

#Trying do a code that turn letter into binary

import random 

def main(): 

    key = input('Digite a palavra que você quer criptografar: ')
    traceback = '' 
    letter1 = [
        "A", "B","C", "D",  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
    
    for letter in key:
        if letter in 'A':
            traceback = traceback + random.choice(letter1)
            traceback = traceback + random.choice(letter1) 
        elif letter in 'C':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'D':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'E':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'F':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'G':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'H':
            traceback = traceback + random.choice(letter1)
        elif letter in 'I':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'J':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'K':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'L': 
            traceback = traceback + random.choice(letter1) 
        elif letter in 'M':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'N': 
            traceback = traceback + random.choice(letter1)
        elif letter in 'O':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'P': 
            traceback = traceback + random.choice(letter1) 
        elif letter in 'Q':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'R':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'S':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'T':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'U':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'V':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'W':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'X':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'Y':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'Z':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'a':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'b':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'c':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'd':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'e':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'f':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'g':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'h':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'i':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'j':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'k':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'l':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'm':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'n':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'o':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'p':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'q':
            traceback = traceback + random.choice(letter1)
        elif letter in 'r':
            traceback = traceback + random.choice(letter1) 
        elif letter in 's':
            traceback = traceback + random.choice(letter1) 
        elif letter in 't':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'u':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'v':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'w':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'x':
            traceback = traceback + random.choice(letter1)  
        elif letter in 'y':
            traceback = traceback + random.choice(letter1) 
        elif letter in 'z':
            traceback = traceback + random.choice(letter1)
    
        print(f'Resultado da criptografia: {traceback}')

if __name__ == '__main__':
    main()