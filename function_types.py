def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] = lista[i] + valor
def calc_avg(lista):
    total = 0
    for num in lista:
        total = total + num
    promedio = total / len(lista)
    return float(promedio)
def print_normalized(lista):
    print(lista)