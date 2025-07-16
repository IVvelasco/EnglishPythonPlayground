# Level 018

#  -------------------------
#  -- AREA OF A RECTANGLE --
#  -------------------------

print("Let's calculate the area of a rectangle!")
basis = float(input("Enter the base size here: "))
height = float(input("Enter the height: "))
area = basis * height 

if basis == height:
    print(f"Hey, that's a square! Area: {area}")
else:
    print(f"The total area of the rectangle is:{area}")