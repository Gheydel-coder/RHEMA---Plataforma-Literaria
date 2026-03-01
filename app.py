import streamlit as st
import google.generativeai as genai

# Configuración técnica de la App
st.set_page_config(page_title="RHEMA - Perfil", page_icon="👤", layout="wide")

# Interfaz profesional y limpia
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; background-color: #1a1c23; color: white; height: 3em; border-radius: 8px; }
    .stTextInput>div>div>input { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- CONFIGURACIÓN DE ACCESO ---
st.sidebar.title("🛡️ Acceso")
api_key = st.sidebar.text_input("Gemini API Key", type="password")

# --- PERFIL DE USUARIO ---
st.title("👤 Perfil de Usuario")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Datos del Autor")
    nombre = st.text_input("Nombre o Seudónimo:", value="Gheydel Guerrero")
    rango = st.selectbox("Nivel:", ["Principiante", "Escritor", "Maestro", "Autor Consagrado"])
    tinta = st.number_input("Créditos de Tinta:", value=500)
    st.caption("ID de Sistema: RHEMA-1001")

with col2:
    st.subheader("Identidad del Asistente")
    st.write("El asistente integrará Mentoría Mística, Edición Técnica y Análisis Estructural.")
    
    nombre_asistente = st.text_input("Nombre del Asistente:", value="Elías")
    
    tipo_base = st.selectbox(
        "Personificación base:",
        ["Autor", "Personaje Literario / Cine", "Avatar de Autoría Propia"]
    )
    
    # Campo obligatorio para definir la "piel" del asistente
    referencia_identidad = st.text_area(
        "Describe la identidad del asistente:", 
        placeholder="Ejemplo: Edgar Allan Poe. Quiero que hable con su estilo melancólico, pero que sea un editor técnico implacable."
    )

st.write("---")

if st.button("Sellar Configuración"):
    if api_key:
        st.success(f"Configuración sellada. Maestro {nombre}, su asistente {nombre_asistente} está activo.")
    else:
        st.error("Se requiere la API Key para validar la conexión con el asistente.")
