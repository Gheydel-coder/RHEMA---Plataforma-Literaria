import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="RHEMA - Perfil", page_icon="👤", layout="wide")

# Estilo visual de la interfaz
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #e0e0e0; }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (Acceso y Seguridad) ---
st.sidebar.title("🔐 Acceso")
api_key = st.sidebar.text_input("Gemini API Key", type="password")

# --- CUERPO PRINCIPAL: PERFIL DE USUARIO 👤 ---
st.title("👤 Perfil de Soberanía")
st.info("Configura tu identidad y la de tu Asistente (Elias).")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Datos del Autor")
    nombre = st.text_input("Nombre del Maestro/Autor:", value="Gheydel Guerrero")
    rango = st.selectbox("Rango Literario:", ["Novicio", "Escriba", "Maestro", "Soberano"])
    tinta = st.number_input("Créditos de Tinta:", value=500)
    id_usuario = "ID-001" 

with col2:
    st.subheader("Configuración del Asistente")
    tipo_asistente = st.selectbox(
        "Esencia del Guía:",
        ["Autor Clásico (ej. Cervantes, Poe)", "Personaje Literario/Cine", "Avatar Propio"]
    )
    nombre_guia = st.text_input("Nombre de tu Guía (ej. Elias, Quijote, Cuervo):")
    
    st.write("---")
    st.write("**Personalidad del Asistente (La Amalgama):**")
    st.caption("Tu guía será una mezcla de la esencia elegida + Mentor Místico + Editor Técnico.")
    descripcion_avatar = st.text_area("Si elegiste Avatar Propio, descríbelo aquí:")

# --- GUARDAR CONFIGURACIÓN ---
if st.button("Sellar Identidad"):
    st.success(f"Identidad Sellada. Bienvenido, Maestro {nombre}. Tu guía {nombre_guia} está listo.")
