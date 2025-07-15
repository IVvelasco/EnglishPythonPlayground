# Level 017

#  -------------------
#  -- PIZZA & INPUT --
#  -------------------

print("################################################")
print("# Welcome to Pypizza, what's your order today? #")
print("################################################")



pizza = int(input("Enter the number of pizzas here: "))
value_pizza = float(19.99)
total0 = value_pizza * pizza

refrigerante = int(input("Enter the amount of soda here: "))
value_soda = float(4.99)
total1 = value_soda * refrigerante

print(f"You must pay ${total0 + total1:.2f}") # This :.2f limit the decimal places that will be displayed on the screen