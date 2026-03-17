from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

semilla = int(input("Enter a seed number: "))
seed_secret_numbers(semilla)
numero_secreto = generate_secret_number()
intentos = 0
adivinado = False
while not adivinado:
    intento_usuario = int(input("What is your guess: "))
    intentos = intentos + 1
    mensaje, adivinado = input_response(numero_secreto, intento_usuario)
    print(mensaje)
print(f"It took you {intentos} tries!")