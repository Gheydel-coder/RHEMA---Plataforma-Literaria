import streamlit as st
import google.generativeai as genai

# Configuración básica de la aplicación
st.set_page_config(page_title="RHEMA - Perfil de Usuario", page_icon="👤", layout="wide")

# Estética limpia y profesional
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; color: #212529; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- ACCESO ---
st.sidebar.title("Configuración")
api_key = st.sidebar.text_input("Gemini API Key", type="password", help="Introduce tu clave para activar el asistente.")

# --- PERFIL DE USUARIO ---
st.title("👤 Perfil de Usuario")
st.write("Gestiona tu información de autor y personaliza tu asistente literario.")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Información del Autor")
    nombre = st.text_input("Nombre o Seudónimo:", value="Gheydel Guerrero")
    rango = st.selectbox("Nivel de Experiencia:", ["Principiante", "Escritor", "Maestro", "Autor Consagrado"])
    tinta = st.number_input("Créditos disponibles (Tinta):", value=500)
    st.caption("ID de Usuario: RHEMA-1001")

with col2:
    st.subheader("Personalización del Asistente (IA)")
    nombre_asistente = st.text_input("Nombre de tu Asistente:", placeholder="Ej: Elías, Mentor, Editor...")
    
    tipo_voz = st.selectbox(
        "Base del Estilo:",
        ["Autor Clásico", "Personaje Literario", "Avatar Personalizado"]
    )
    
    st.write("**Modo de Intervención:**")
    enfoque = st.multiselect(
        "Elige las funciones del asistente:",
        ["Corrección Técnica/Ortográfica", "Mentoría Mística/Creativa", "Análisis Estructural", "Edición de Estilo"],
        default=["Corrección Técnica/Ortográfica"]
    )
    
    descripcion_guia = st.text_area("Instrucciones específicas para el asistente:", placeholder="Ej: Quiero que seas asertivo y uses un lenguaje elevado...")

st.write("---")
if st.button("Guardar Cambios"):
    if api_key:
        st.success(f"Configuración guardada. Bienvenido, {nombre}. Tu asistente '{nombre_asistente}' está configurado.")
    else:
        st.warning("Por favor, introduce tu API Key en la barra lateral para validar los cambios.")
