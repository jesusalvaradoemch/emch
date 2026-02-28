import streamlit as st
import streamlit.components.v1 as components
#from streamlit_gsheets import GSheetsConnection
#import pandas as pd

# ==================================================
# CONFIGURACIÓN GENERAL
# ==================================================

st.set_page_config(
    page_title="Química General 2026",
    page_icon="🧪",
    layout="wide"
)

st.sidebar.image("img/combustion-metano.svg", caption="Química General 2026")

st.sidebar.markdown("## 👨‍🏫 Docente")
st.sidebar.write("Dr. Jesús Alvarado Huayhuaz")
st.sidebar.write("Escuela Militar de Chorrillos")
st.sidebar.write("📩 jalvaradoh@escuelamilitar.edu.pe")

st.sidebar.markdown("---")

# ==================================================
# FUNCIÓN GENERAL PARA INSERTAR GOOGLE FORM
# ==================================================

def insertar_formulario(url_form):
    st.markdown("### 📤 Entrega de Actividad")
    st.info("Sube tu actividad mediante el siguiente formulario (uso obligatorio institucional).")
    components.iframe(url_form, width=800, height=900, scrolling=True)
    st.markdown("---")


# ==================================================
# PÁGINA PRINCIPAL
# ==================================================

def Home():
    st.title("📘 QUÍMICA GENERAL")
    st.markdown("### Bachillerato en Ciencias Militares | Ciencias y Humanidades")
    st.markdown("---")

    st.write("""
    Bienvenidos al curso de **Química General 2026**.
    
    Este curso está orientado al desarrollo de:
    
    - Pensamiento científico
    - Razonamiento cuantitativo
    - Aplicación práctica en ciencias militares
    - Resolución de problemas reales
    """)

    silabo_url = "https://github.com/jesusalvaradoemch/emch/raw/refs/heads/main/Clases/SILABO.pdf"
    st.markdown(f"[⬇️ Descargar Sílabo Oficial]({silabo_url})")

    st.markdown("---")
    st.success("⚠️ Cada semana incluye actividad obligatoria con entrega mediante formulario.")
    st.text("IMPORTANTE: La actividad se deja el martes y la revisión es el miércoles")

# ==================================================
# SEMANA 1
# ==================================================

def semana1():
    st.header("Semana 1: Presentación del Curso y Materia", divider="rainbow")

    st.subheader("🎯 Objetivo")
    st.write("Comprender la estructura del átomo y aplicar correctamente los números cuánticos.")

    diapositivas = "https://docs.google.com/presentation/d/1mrNHsc_6a0d4AQsiWsYsQvvRqqctcFey/preview"
    components.iframe(diapositivas, width=900, height=500)
    
    st.info("Construye átomos")
    phet1 = "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_all.html"
    st.components.v1.iframe(phet1, width=800, height=600, scrolling=False)
    
    st.info("Estados de la materia")
    phet2 = "https://phet.colorado.edu/sims/html/states-of-matter-basics/latest/states-of-matter-basics_en.html"
    st.components.v1.iframe(phet2, width=800, height=600, scrolling=False)

# ==================================================
# SEMANA 2
# ==================================================

def semana2():
    st.header("Semana 2: Estructura Atómica y Números Cuánticos", divider="rainbow")

    st.subheader("🎯 Objetivo")
    st.write("Comprender la estructura del átomo y aplicar correctamente los números cuánticos.")

    diapositivas = "https://docs.google.com/presentation/d/1mrNHsc_6a0d4AQsiWsYsQvvRqqctcFey/preview"
    components.iframe(diapositivas, width=900, height=500)

    st.subheader("🧪 Actividad")
    st.write("""
    1. En una tabla, reflexiona y redacta 5 cambios físicos y 5 cambios químicos que identificas en tu día a día en la EMCH.
    2. Crea tu cuenta de GITHUB con tu correo institucional (EMCH) y tu cuenta en STREAMLIT (de acuerdo al video adjunto)
    3. Guarda en un PDF los puntos 1 y 2 (enlaces de github y de streamlit, por ejemplo: https://github.com/jesusalvaradoemch y https://emch26.streamlit.app/, respectivamente.) y adjúntalo al FORMULARIO.
    IMPORTANTE: La actividad se deja el martes y la revisión es el miércoles.
    """)

    # LINK AL FORMULARIO
    st.markdown("FORMULARIO: (https://forms.gle/HyMZBGY7ht9j7WpQ8)")
    
    st.markdown("### Complementario: Simulación interactiva")
    phet = "https://phet.colorado.edu/sims/html/isotopes-and-atomic-mass/latest/isotopes-and-atomic-mass_all.html"
    components.iframe(phet, width=900, height=600)

# ==================================================
# SEMANA 3
# ==================================================

def semana3():
    st.header("Semana 3: Configuración Electrónica y Tabla Periódica", divider="rainbow")

    st.subheader("🎯 Objetivo")
    st.write("Relacionar configuración electrónica con propiedades periódicas.")

    diapositivas = "https://docs.google.com/presentation/d/1-DfJRnfVsC4PgaiBUFDLZ1eoEV1Ix0MP/preview"
    components.iframe(diapositivas, width=900, height=500)

    st.subheader("🧪 Actividad")
    st.write("""
    - Determinar grupo y período de 15 elementos.
    - Justificar tendencias periódicas.
    - Identificar elementos estratégicos militares.
    """)

    phet = "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_all.html"
    components.iframe(phet, width=900, height=600)

    #form_semana2 = "https://docs.google.com/forms/d/e/FORM_ID_SEMANA2/viewform?embedded=true"
    #insertar_formulario(form_semana2)


# ==================================================
# SEMANA 4
# ==================================================

def semana4():
    st.header("Semana 4: Unidades Químicas de Masa", divider="rainbow")

    st.subheader("🎯 Objetivo")
    st.write("Aplicar correctamente mol, masa molar y número de Avogadro.")

    st.subheader("🧪 Actividad")
    #st.write("""
    #- 20 ejercicios de conversión mol ↔ gramos.
    #- Problemas aplicados a logística militar.
    #""")

    #form_semana3 = "https://docs.google.com/forms/d/e/FORM_ID_SEMANA3/viewform?embedded=true"
    #insertar_formulario(form_semana3)

# ==================================================
# SEMANA 5
# ==================================================

def semana5():
    st.header("Semana 5: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 6
# ==================================================

def semana6():
    st.header("Semana 6: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 7
# ==================================================

def semana7():
    st.header("Semana 7: ", divider="rainbow")

    st.subheader("🎯 Objetivo")
    
# ==================================================
# SEMANA 8
# ==================================================

def semana8():
    st.header("Semana 8: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 9
# ==================================================

def semana9():
    st.header("Semana 9: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 10
# ==================================================

def semana10():
    st.header("Semana 10: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 11
# ==================================================

def semana11():
    st.header("Semana 11: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 12
# ==================================================

def semana12():
    st.header("Semana 12: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 13
# ==================================================

def semana13():
    st.header("Semana 13: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 14
# ==================================================

def semana14():
    st.header("Semana 14: ", divider="rainbow")

    st.subheader("🎯 Objetivo")

# ==================================================
# SEMANA 15
# ==================================================

def semana15():
    st.header("Semana 15: EXAMEN FINAL", divider="rainbow")

    st.subheader("🎯 Objetivo")


# ==================================================
# DICCIONARIO DE PÁGINAS
# ==================================================

pages = {
    "Inicio": Home,
    "Semana 1": semana1,
    "Semana 2": semana2,
    "Semana 3": semana3,
    "Semana 4": semana4,
    "Semana 5": semana5,
    "Semana 6": semana6,
    "Semana 7": semana7,
    "Semana 8": semana8,
    "Semana 9": semana9,
    "Semana 10": semana10,
    "Semana 11": semana11,
    "Semana 12": semana12,
    "Semana 13": semana13,
    "Semana 14": semana14,
    "Semana 15": semana15,
}

selected = st.sidebar.selectbox("📚 Temario", pages.keys())
pages[selected]()
