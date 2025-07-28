# Level 033

#  ------------------------------------------
#  -- SPLITING THE BILLS WITH YOUR FRIENDS --
#  ------------------------------------------

def main():
    bill = float(input("What is the total amount of the bill?"))
    friends = int(input("How many friends will split the bills? "))
    split = bill / friends 
    print(f"Amount ${split:.2f} for each friend.")

if __name__ == main():
    main()
