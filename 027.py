
# Level 027

#  -------------------------
#  -- LETTER INTO BINARY  --
#  -------------------------

# My attempt building a code that translates alphabet to binary

key = input('Type what you wanna translate to binary: ')
retorno = ''

for key in key:
    if key in 'A':
        retorno = retorno + '01000001 '
    elif key in 'B':
        retorno = retorno + '01000010 '
    elif key in 'C':
        retorno = retorno + '01000011 '
    elif key in 'D':
        retorno = retorno + '01000100 '
    elif key in 'E':
        retorno = retorno + '01000101 '
    elif key in 'F':
        retorno = retorno + '01000110 '
    elif key in 'G':
        retorno = retorno + '01000111 '
    elif key in 'H':
        retorno = retorno + '01001000 '
    elif key in 'I':
        retorno = retorno + '01001001 '
    elif key in 'J':
        retorno = retorno + '01001010 ' 
    elif key in 'K':
        retorno = retorno + '01001011 '
    elif key in 'L': 
        retorno = retorno + '01001100 '
    elif key in 'M':
        retorno = retorno + '01001101 '
    elif key in 'N': 
        retorno = retorno + '01001110 '
    elif key in 'O':
        retorno = retorno + '01001111 '
    elif key in 'P': 
        retorno = retorno + '01010000 '
    elif key in 'Q':
        retorno = retorno + '01010001 '
    elif key in 'R':
        retorno = retorno + '10100010 '
    elif key in 'S':
        retorno = retorno + '10100011 '
    elif key in 'T':
        retorno = retorno + '01010100 '
    elif key in 'U':
        retorno = retorno + '01010101 '
    elif key in 'V':
        retorno = retorno + '01010110 '
    elif key in 'W':
        retorno = retorno + '01010111 '
    elif key in 'X':
        retorno = retorno + '01011000 '
    elif key in 'Y':
        retorno = retorno + '01011001 '
    elif key in 'Z':
        retorno = retorno + '01011010 '
    elif key in 'a':
        retorno = retorno + '01100001 '
    elif key in 'b':
        retorno = retorno + '01100010 '
    elif key in 'c':
        retorno = retorno + '01100011 '
    elif key in 'd':
        retorno = retorno + '01100100 '
    elif key in 'e':
        retorno = retorno + '01100101 '
    elif key in 'f':
        retorno = retorno + '01100110 '
    elif key in 'g':
        retorno = retorno + '01100111 '
    elif key in 'h':
        retorno = retorno + '01101000 '
    elif key in 'i':
        retorno = retorno + '01101001 '
    elif key in 'j':
        retorno = retorno + '01101010 '
    elif key in 'k':
        retorno = retorno + '01101011 '
    elif key in 'l':
        retorno = retorno + '01101100 '
    elif key in 'm':
        retorno = retorno + '01101101 '
    elif key in 'n':
        retorno = retorno + '01101110 '
    elif key in 'o':
        retorno = retorno + '01101111 '
    elif key in 'p':
        retorno = retorno + '01110000 '
    elif key in 'q':
        retorno = retorno + '01110001 '
    elif key in 'r':
        retorno = retorno + '01110010 '
    elif key in 's':
        retorno = retorno + '01110011 '
    elif key in 't':
        retorno = retorno + '01110100 '
    elif key in 'u':
        retorno = retorno + '01110101 '
    elif key in 'v':
        retorno = retorno + '01110110 '
    elif key in 'w':
        retorno = retorno + '01110111 '
    elif key in 'x':
        retorno = retorno + '01111000 '
    elif key in 'y':
        retorno = retorno + '01111001 '
    elif key in 'z':
        retorno = retorno + '01111010 '
    
    print('Your output: ' + retorno)