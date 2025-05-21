import math

def resolver_ecuacion_2do_grado(a, b, c):
    if a == 0:
        return "No es una ecuación de segundo grado."

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Tiene dos soluciones reales:\nx1 = {x1}\nx2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Tiene una solución real doble:\nx = {x}"
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        return (f"Tiene dos soluciones complejas:\n"
                f"x1 = {parte_real} + {parte_imaginaria}i\n"
                f"x2 = {parte_real} - {parte_imaginaria}i")
        # Ejemplo de uso
try:
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    resultado = resolver_ecuacion_1er_grado(a, b)
    print(resultado)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")


