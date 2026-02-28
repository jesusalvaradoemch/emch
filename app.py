import streamlit as st
import streamlit.components.v1 as components

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


# ==================================================
# SEMANA 1
# ==================================================

def semana1():
    st.header("Semana 1: Estructura Atómica y Números Cuánticos", divider="rainbow")

    st.subheader("🎯 Objetivo")
    st.write("Comprender la estructura del átomo y aplicar correctamente los números cuánticos.")

    diapositivas = "https://docs.google.com/presentation/d/1mrNHsc_6a0d4AQsiWsYsQvvRqqctcFey/preview"
    components.iframe(diapositivas, width=900, height=500)

    st.subheader("🧪 Actividad")
    st.write("""
    1. En una tabla, reflexiona y redacta 5 cambios físicos y 5 cambios químicos que identificas en tu día a día en la EMCH.
    2. Crea tu cuenta de GITHUB con tu correo institucional (EMCH) y tu cuenta en STREAMLIT (de acuerdo al video adjunto)
    3. Guarda en un PDF los puntos 1 y 2 (enlaces de github y de streamlit, por ejemplo: github.com/jesusalvaradoemch y https://emch26.streamlit.app/, respectivamente.) y adjúntalo al FORMULARIO.
    IMPORTANTE: La actividad se deja el martes y la revisión es el miércoles.
    """)

    # LINK AL FORMULARIO
    form_semana1 = "https://forms.gle/HyMZBGY7ht9j7WpQ8" #"https://docs.google.com/forms/d/e/FORM_ID_SEMANA1/viewform?embedded=true"
    insertar_formulario(form_semana1)
    
    st.markdown("### Complementario: Simulación interactiva")
    phet = "https://phet.colorado.edu/sims/html/isotopes-and-atomic-mass/latest/isotopes-and-atomic-mass_all.html"
    components.iframe(phet, width=900, height=600)

# ==================================================
# SEMANA 2
# ==================================================

def semana2():
    st.header("Semana 2: Configuración Electrónica y Tabla Periódica", divider="rainbow")

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
# SEMANA 3
# ==================================================

def semana3():
    st.header("Semana 3: Unidades Químicas de Masa", divider="rainbow")

    st.subheader("🎯 Objetivo")
    st.write("Aplicar correctamente mol, masa molar y número de Avogadro.")

    st.subheader("🧪 Actividad")
    st.write("""
    - 20 ejercicios de conversión mol ↔ gramos.
    - Problemas aplicados a logística militar.
    """)

    #form_semana3 = "https://docs.google.com/forms/d/e/FORM_ID_SEMANA3/viewform?embedded=true"
    #insertar_formulario(form_semana3)


# ==================================================
# DICCIONARIO DE PÁGINAS
# ==================================================

pages = {
    "Inicio": Home,
    "Semana 1": semana1,
    "Semana 2": semana2,
    "Semana 3": semana3,
}

selected = st.sidebar.selectbox("📚 Temario", pages.keys())
pages[selected]()
