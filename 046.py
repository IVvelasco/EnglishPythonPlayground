# Level 047

#--------------------------------
# -- TESTING TERNARY OPERATORS --
# --   USER LOGIN OR LOGOUT    --
# -------------------------------

def main():
    user = 'name'
    password = int(12345678)
    print("------------------------------")
    print("Welcome to Login Menu")
    print("------------------------------")

    u = input("User: ")
    s = int(input("Password: "))
    if u == user and s == password:
        user_login = True 
    else:
        user_login = False

    if user_login == True:
        print("You have been successfully logged in!")
    else:
        print("Incorrect username or password, please try again!")

if __name__ == "__main__":
    main()