def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    suma_total = 0
    for nota in calificaciones:
        suma_total = suma_total + nota
    return float(suma_total / len(calificaciones))