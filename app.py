import streamlit as st
import google.generativeai as genai

# 1. Configuración de Identidad
st.set_page_config(page_title="RHEMA", page_icon="✒️", layout="wide")

# 2. RED DE SEGURIDAD (Inicialización de Memoria)
# Esto elimina el AttributeError de raíz
if 'nombre_autor' not in st.session_state: st.session_state['nombre_autor'] = "Gheydel Guerrero"
if 'rango_autor' not in st.session_state: st.session_state['rango_autor'] = "Maestro"
if 'nombre_asistente' not in st.session_state: st.session_state['nombre_asistente'] = "Elías"
if 'identidad_guia' not in st.session_state: st.session_state['identidad_guia'] = "Mentor literario técnico"
if 'api_key' not in st.session_state: st.session_state['api_key'] = ""
if 'resultado_ia' not in st.session_state: st.session_state['resultado_ia'] = ""

# --- NAVEGACIÓN ---
st.sidebar.title("RHEMA")
menu = st.sidebar.radio("Ir a:", ["👤 Perfil", "📚 Biblioteca", "🖋️ Taller"])

# --- MÓDULO: PERFIL ---
if menu == "👤 Perfil":
    st.title("👤 Configuración")
    st.session_state['nombre_autor'] = st.text_input("Nombre del Autor:", value=st.session_state['nombre_autor'])
    st.session_state['api_key'] = st.text_input("Tu Google API Key:", value=st.session_state['api_key'], type="password")
    st.session_state['nombre_asistente'] = st.text_input("Nombre del Asistente:", value=st.session_state['nombre_asistente'])
    st.session_state['identidad_guia'] = st.text_area("Instrucciones del Guía:", value=st.session_state['identidad_guia'])
    if st.button("Sellar"):
        st.success("Configuración guardada.")

# --- MÓDULO: BIBLIOTECA ---
elif menu == "📚 Biblioteca":
    st.title("📚 Biblioteca")
    st.write(f"Estante de: {st.session_state['nombre_autor']}")
    st.info("Aquí aparecerán tus obras.")

# --- MÓDULO: TALLER ---
elif menu == "🖋️ Taller":
    st.title("🖋️ Taller Literario")
    if not st.session_state['api_key']:
        st.warning("⚠️ Falta la API Key en el Perfil.")
    else:
        # Configuración de IA
        try:
            genai.configure(api_key=st.session_state['api_key'])
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            texto_usuario = st.text_area("Dicta o escribe aquí:", height=300)
            if st.button("✨ Elevar Texto"):
                if texto_usuario:
                    with st.spinner("Elías está trabajando..."):
                        p = f"Actúa como {st.session_state['nombre_asistente']}. {st.session_state['identidad_guia']}. Mejora esto: {texto_usuario}"
                        response = model.generate_content(p)
                        st.session_state['resultado_ia'] = response.text
                else:
                    st.error("Escribe algo primero.")
            
            if st.session_state['resultado_ia']:
                st.subheader("Resultado:")
                st.write(st.session_state['resultado_ia'])
        except Exception as e:
            st.error(f"Error técnico: {e}")
