# Level 010

# ----------------
# -- Calculator --
# ----------------

print("Enter two numbers and choose one of the basic operators: ")
print("(+) --> Addition") 
print("(-) --> Subtraction")
print("(/) Division")
print("(*) Multiplication")

n1 = int(input("Choose the first number: "))
n2 = int(input("Choose the second number: ")) 
operator = input('Choose the operator: ') 

if operator == '+':
    result = (n1 + n2)
elif operator == '-':
    result = (n1 - n2)
elif operator == '/':
    result = (n1 / n2)
elif operator == '*':
    result = (n1 * n2)


print(f"resultado = {result}")