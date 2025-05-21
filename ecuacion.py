import streamlit as st
import random

# Función para generar una ecuación de primer grado
def generar_ecuacion():
    a = random.randint(1, 10)
    x = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = a * x + b
    return f"{a}x + {b} = {c}", x

# Título
st.title("Ecuaciones de Primer Grado")

# Generar nueva ecuación si no existe ya una
if "ecuacion" not in st.session_state:
    st.session_state.ecuacion, st.session_state.resultado = generar_ecuacion()

# Mostrar la ecuación
st.write("Resuelve la siguiente ecuación:")
st.latex(st.session_state.ecuacion)

# Campo para la respuesta del usuario
respuesta_usuario = st.number_input("¿Cuál es el valor de x?", step=1.0)

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if respuesta_usuario == st.session_state.resultado:
        st.success("✅ ¡Correcto! 🎉")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta es x = {st.session_state.resultado}")

# Botón para nueva ecuación
if st.button("Nueva ecuación"):
    st.session_state.ecuacion, st.session_state.resultado = generar_ecuacion()
    st.experimental_rerun()
