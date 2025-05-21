def resolver_ecuacion_1er_grado(a, b):
    if a == 0:
        if b == 0:
            return "La ecuación tiene infinitas soluciones."
        else:
            return "La ecuación no tiene solución."
    else:
        x = -b / a
        return f"La solución es: x = {x}"

# Ejemplo de uso
try:
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    resultado = resolver_ecuacion_1er_grado(a, b)
    print(resultado)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
