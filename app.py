import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="RHEMA", page_icon="✒️", layout="wide")

# 2. Inicialización de Memoria (Evita el AttributeError)
if 'nombre_autor' not in st.session_state: st.session_state['nombre_autor'] = "Gheydel Guerrero"
if 'rango_autor' not in st.session_state: st.session_state['rango_autor'] = "Maestro"
if 'nombre_asistente' not in st.session_state: st.session_state['nombre_asistente'] = "Elías"
if 'identidad_guia' not in st.session_state: st.session_state['identidad_guia'] = "Mentor literario místico"
if 'api_key' not in st.session_state: st.session_state['api_key'] = ""
if 'resultado_ia' not in st.session_state: st.session_state['resultado_ia'] = ""

# --- NAVEGACIÓN ---
st.sidebar.title("RHEMA")
menu = st.sidebar.radio("Navegación:", ["👤 Perfil", "📚 Biblioteca", "🖋️ Taller"])

# --- MÓDULO 1: PERFIL ---
if menu == "👤 Perfil":
    st.title("👤 Configuración de Soberanía")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state['nombre_autor'] = st.text_input("Autor:", value=st.session_state['nombre_autor'])
        st.session_state['rango_autor'] = st.selectbox("Nivel:", ["Escritor Nobel", "Autor Consagrado", "Maestro"], index=2)
        st.session_state['api_key'] = st.text_input("Google API Key:", value=st.session_state['api_key'], type="password")
    with col2:
        st.session_state['nombre_asistente'] = st.text_input("Asistente:", value=st.session_state['nombre_asistente'])
        st.session_state['identidad_guia'] = st.text_area("Instrucciones del Guía:", value=st.session_state['identidad_guia'], height=150)
    if st.button("Sellar"):
        st.success("Configuración guardada.")

# --- MÓDULO 2: BIBLIOTECA ---
elif menu == "📚 Biblioteca":
    st.title("📚 Mi Biblioteca")
    st.write(f"### Estante de: {st.session_state['nombre_autor']}")
    st.info("Módulo de archivos en construcción.")

# --- MÓDULO 3: TALLER (IA Activa) ---
elif menu == "🖋️ Taller":
    st.title("🖋️ El Taller Literario")
    if not st.session_state['api_key']:
        st.warning("⚠️ Ingresa la API Key en el Perfil.")
    else:
        col_in, col_out = st.columns(2)
        with col_in:
            st.subheader("Borrador")
            texto_usuario = st.text_area("Escribe aquí:", height=300)
            if st.button("✨ Elevar Texto"):
                if texto_usuario:
                    try:
                        genai.configure(api_key=st.session_state['api_key'])
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        p = f"Actúa como {st.session_state['nombre_asistente']}. {st.session_state['identidad_guia']}. Mejora esto: {texto_usuario}"
                        with st.spinner("Procesando..."):
                            response = model.generate_content(p)
                            st.session_state['resultado_ia'] = response.text
                    except Exception as e:
                        st.error(f"Error: {e}")
        with col_out:
            st.subheader("Resultado RHEMA")
            st.write(st.session_state['resultado_ia'])
