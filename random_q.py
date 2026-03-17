import random

random.seed(123)
inicio_texto = input("Enter the start value:\n")
inicio = int(inicio_texto)
fin_texto = input("Enter the end value:\n")
fin = int(fin_texto)
numero_aleatorio = random.randint(inicio, fin)
print(f"Generated random number: {numero_aleatorio}")