# Level 034
# -------------------------
# -- SPLIT BILLS PART  2 --
# -------------------------

def menu():
    """Function for show the Menu"""
    print("=============================================")
    print("====================MENU====================")
    print("---------------------------------------------")
    print("Beer $5.99")
    print("---------------------------------------------")
    print("French fries $9.99")
    print("---------------------------------------------")
    print("Burguer $19.99")
    print("=============================================")

def bill_calculator():
   
    beer = 5.99
    frensh_fries = 9.99
    burguer = 19.99
    
    beer_request = int(input("Quantas cervejas você pediu? R: "))
    fries_request = int(input("Quantos petiscos foram pedidos? R: "))
    burguer_request = int(input("Quantas porções foram pedidas? R: "))
    
    
    beer_amount = beer * beer_request
    fries_amount = frensh_fries * fries_request
    burguer_amount = burguer * burguer_request
    
    total = beer_amount + fries_amount + burguer_amount
    
    friends = int(input("How many people (including you) will split the bill? R: "))
    each_bill = total / friends
    
    print(f"\n🍺 Bill:")
    print(f"Beers: {beer} x ${beer_request:.2f} = ${beer_amount:.2f}")
    print(f"Frensh Fries: {frensh_fries} x R${fries_request:.2f} = ${fries_amount:.2f}")
    print(f"Burguers: {burguer} x ${burguer_request:.2f} = ${burguer_amount:.2f}")
    print(f"─" * 50)
    print(f"💰 Total: ${total:.2f}")
    print(f"👥 split by {friends} people: ${each_bill:.2f} each")
    print(f"Chears! 🍻")

def main():
    """Principal Function that order all"""
    print("🍺 Welcome to Bar.py! 🍺\n")
    menu()
    print()
    bill_calculator()

if __name__ == "__main__":
    main()