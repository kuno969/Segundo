import streamlit as st
import random
import math

st.set_page_config(page_title="Ecuación de Segundo Grado", layout="centered")

st.title("🧮 Resolución de Ecuaciones de Segundo Grado")
st.markdown("Resuelve ecuaciones de la forma: `ax² + bx + c = 0`")

# Entrada de coeficientes
a = st.number_input("Coeficiente a", value=1.0)
b = st.number_input("Coeficiente b", value=0.0)
c = st.number_input("Coeficiente c", value=0.0)

# Botón para resolver
if st.button("Resolver"):
    if a == 0:
        st.error("❌ No es una ecuación de segundo grado (a no puede ser cero).")
    else:
        discriminante = b**2 - 4*a*c
        if discriminante > 0:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            st.success(f"✅ Dos soluciones reales distintas:\n\nx₁ = {x1}\n\nx₂ = {x2}")
        elif discriminante == 0:
            x = -b / (2*a)
            st.success(f"✅ Una solución real doble:\n\nx = {x}")
        else:
            parte_real = -b / (2*a)
            parte_imaginaria = math.sqrt(-discriminante) / (2*a)
            st.info(f"ℹ️ Soluciones complejas:\n\n"
                    f"x₁ = {parte_real} + {parte_imaginaria}i\n\n"
                    f"x₂ = {parte_real} - {parte_imaginaria}i")
