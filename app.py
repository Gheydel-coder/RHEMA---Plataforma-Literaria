import streamlit as st
import google.generativeai as genai

# 1. Configuración de Identidad de la App
st.set_page_config(page_title="RHEMA", page_icon="✒️", layout="wide")

# 2. INICIALIZACIÓN CRÍTICA DE MEMORIA (La Red de Seguridad)
# Si la variable no existe, la creamos aquí mismo para evitar el AttributeError
if 'nombre_autor' not in st.session_state:
    st.session_state['nombre_autor'] = "Gheydel Guerrero"
if 'rango_autor' not in st.session_state:
    st.session_state['rango_autor'] = "Maestro"
if 'nombre_asistente' not in st.session_state:
    st.session_state['nombre_asistente'] = "Elías"
if 'identidad_guia' not in st.session_state:
    st.session_state['identidad_guia'] = "Mentor literario técnico"
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = ""
if 'resultado_ia' not in st.session_state:
    st.session_state['resultado_ia'] = ""

# --- NAVEGACIÓN ---
st.sidebar.title("RHEMA")
menu = st.sidebar.radio("Navegación:", ["👤 Perfil", "📚 Biblioteca", "🖋️ Taller"])

# --- MÓDULO 1: PERFIL ---
if menu == "👤 Perfil":
    st.title("👤 Configuración de Soberanía")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state['nombre_autor'] = st.text_input("Tu Nombre:", value=st.session_state['nombre_autor'])
        st.session_state['rango_autor'] = st.selectbox("Nivel:", ["Escritor Nobel", "Autor Consagrado", "Maestro"], 
                                                      index=["Escritor Nobel", "Autor Consagrado", "Maestro"].index(st.session_state['rango_autor']))
        st.session_state['api_key'] = st.text_input("Google API Key:", value=st.session_state['api_key'], type="password")
        
    with col2:
        st.session_state['nombre_asistente'] = st.text_input("Asistente:", value=st.session_state['nombre_asistente'])
        st.session_state['identidad_guia'] = st.text_area("Instrucciones para el Guía:", value=st.session_state['identidad_guia'], height=150)
    
    if st.button("Sellar"):
        st.success("Configuración guardada en la memoria.")

# --- MÓDULO 2: BIBLIOTECA ---
elif menu == "📚 Biblioteca":
    st.title("📚 Mi Biblioteca")
    st.write(f"### Estante de: {st.session_state['nombre_autor']}")
    st.info("Módulo en construcción. Aquí verás tus lomos de libros pronto.")

# --- MÓDULO 3: TALLER (IA Activa) ---
elif menu == "🖋️ Taller":
    st.title("🖋️ El Taller Literario")
    
    if not st.session_state['api_key']:
        st.warning("⚠️ Falta la API Key. Ve al Perfil para activarla.")
    else:
        col_in, col_out = st.columns(2)
        with col_in:
            st.subheader("Borrador")
            texto_usuario = st.text_area("Dicta o escribe aquí:", height=300)
            
            if st.button("✨ Elevar Texto"):
                if texto_usuario:
                    try:
                        genai.configure(api_key=st.session_state['api_key'])
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        
                        prompt = f"Actúa como {st.session_state['nombre_asistente']}. Personalidad: {st.session_state['identidad_guia']}. Mejora literariamente este texto: {texto_usuario}"
                        
                        with st.spinner("Transformando..."):
                            response = model.generate_content(prompt)
                            st.session_state['resultado_ia'] = response.text
                    except Exception as e:
                        st.error(f"Error de conexión: {e}")
        
        with col_out:
            st.subheader("Resultado RHEMA")
            st.write(st.session_state['resultado_ia'])
