import streamlit as st
import google.generativeai as genai

# 1. Configuración de Identidad
st.set_page_config(page_title="RHEMA - Taller", page_icon="🖋️", layout="wide")

# 2. Inicialización de Memoria (Session State)
if 'nombre_autor' not in st.session_state: st.session_state['nombre_autor'] = "Gheydel Guerrero"
if 'nombre_asistente' not in st.session_state: st.session_state['nombre_asistente'] = "Elías"
if 'identidad_guia' not in st.session_state: st.session_state['identidad_guia'] = "Mentor literario técnico"
if 'api_key' not in st.session_state: st.session_state['api_key'] = ""
if 'resultado_ia' not in st.session_state: st.session_state['resultado_ia'] = ""

# --- NAVEGACIÓN ---
menu = st.sidebar.radio("Navegación:", ["👤 Perfil", "📚 Biblioteca", "🖋️ Taller"])

# --- MÓDULO 1: PERFIL (Donde pones la Llave) ---
if menu == "👤 Perfil":
    st.title("👤 Configuración")
    st.text_input("Autor:", key='nombre_autor')
    st.text_input("Asistente:", key='nombre_asistente')
    st.text_area("Personalidad del Guía:", key='identidad_guia')
    st.password_input("Introduce tu Gemini API Key:", key='api_key')
    st.info("Pega tu llave arriba para activar el Taller.")

# --- MÓDULO 2: BIBLIOTECA ---
elif menu == "📚 Biblioteca":
    st.title("📚 Biblioteca")
    st.write(f"Estante de {st.session_state.nombre_autor}")
    st.info("Módulo de archivos en construcción...")

# --- MÓDULO 3: TALLER (EL TINTERO ACTIVO) ---
elif menu == "🖋️ Taller":
    st.title("🖋️ El Taller de Escritura")
    
    if not st.session_state.api_key:
        st.error("⚠️ Falta la API Key. Ve al Perfil y agrégala.")
    else:
        # Configurar la IA con tu llave
        genai.configure(api_key=st.session_state.api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Borrador / Dictado")
            texto_usuario = st.text_area("Escribe o pega aquí tu idea:", height=400, placeholder="Escribe el germen de tu obra...")
            
            if st.button("✨ Transformar Obra"):
                if texto_usuario:
                    with st.spinner(f"{st.session_state.nombre_asistente} está trabajando..."):
                        # El "Prompt": Le decimos a la IA quién debe ser
                        prompt = f"""
                        Actúa como {st.session_state.nombre_asistente}. 
                        Tu personalidad es: {st.session_state.identidad_guia}.
                        Tu misión es tomar el siguiente texto y elevar su calidad literaria, 
                        manteniendo el alma del autor pero aplicando rigor técnico y belleza mística:
                        
                        Texto del autor: {texto_usuario}
                        """
                        response = model.generate_content(prompt)
                        st.session_state.resultado_ia = response.text
                else:
                    st.warning("Escribe algo primero para que pueda ayudarte.")

        with col2:
            st.subheader("Resultado RHEMA")
            st.markdown(f'<div style="background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #ddd; color: #333; min-height: 400px;">{st.session_state.resultado_ia}</div>', unsafe_allow_html=True)
            
            if st.session_state.resultado_ia:
                if st.button("💾 Enviar a Biblioteca"):
                    st.success("Obra sellada y enviada al estante.")
