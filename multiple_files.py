from utils import *

mensaje_original = input("Please type your message\n")
cantidad_a = count_letters(mensaje_original, "a")
mensaje_invertido = flip(mensaje_original)
mensaje_codificado = f"{mensaje_invertido}{cantidad_a}"
print(f"Your encoded message is: {mensaje_codificado}")