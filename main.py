from utils import *

while True:
    print("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):")
    op = input().lower()
    if op == "exit":
        break
    if op not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
        print("Invalid option!")
        continue
    if op == "absolute":
        n = float(input("Enter the number:\n"))
        resultado = absolute(n)
    else:
        n1 = float(input("Enter the first number:\n"))
        n2 = float(input("Enter the second number:\n"))
        if op == "add":
            resultado = add(n1, n2)
        elif op == "subtract":
            resultado = sub(n1, n2)
        elif op == "multiply":
            resultado = multiply(n1, n2)
        elif op == "divide":
            resultado = divide(n1, n2)
        elif op == "exponent":
            resultado = exponent(n1, n2)
        elif op == "modulo":
            resultado = modulo(n1, n2)
        elif op == "floor_divide":
            resultado = floor_divide(n1, n2)
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"The result is: {resultado}")