import streamlit as st
import google.generativeai as genai

# 1. Configuración de Identidad de la App
st.set_page_config(page_title="RHEMA", page_icon="✒️", layout="wide")

# 2. Estilos Visuales
st.markdown("""
    <style>
    .main { background-color: #f4f1ea; }
    .stSidebar { background-color: #1a1c23; color: white; }
    .resultado-caja {
        background-color: #ffffff; padding: 20px; border-radius: 10px;
        border: 1px solid #ddd; color: #333; min-height: 400px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MEMORIA BLINDADA (Inicialización) ---
# Esto evita el AttributeError al asegurar que todas las llaves existan
variables = {
    'nombre_autor': "Gheydel Guerrero",
    'rango_autor': "Maestro",
    'nombre_asistente': "Elías",
    'identidad_guia': "Mentor literario técnico y místico",
    'api_key': "",
    'resultado_ia': ""
}

for key, value in variables.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --- NAVEGACIÓN ---
st.sidebar.title("RHEMA")
menu = st.sidebar.radio("Navegación:", ["👤 Perfil", "📚 Biblioteca", "🖋️ Taller"])

# --- MÓDULO 1: PERFIL ---
if menu == "👤 Perfil":
    st.title("👤 Configuración de Soberanía")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.nombre_autor = st.text_input("Autor:", value=st.session_state.nombre_autor)
        st.session_state.rango_autor = st.selectbox("Rango:", ["Escritor Nobel", "Autor Consagrado", "Maestro"], 
                                                   index=["Escritor Nobel", "Autor Consagrado", "Maestro"].index(st.session_state.rango_autor))
        st.session_state.api_key = st.text_input("Google API Key:", value=st.session_state.api_key, type="password")
        
    with col2:
        st.session_state.nombre_asistente = st.text_input("Asistente:", value=st.session_state.nombre_asistente)
        st.session_state.identidad_guia = st.text_area("Identidad del Guía:", value=st.session_state.identidad_guia, height=150)
    
    if st.button("Sellar"):
        st.success("Configuración guardada.")

# --- MÓDULO 2: BIBLIOTECA ---
elif menu == "📚 Biblioteca":
    st.title("📚 Mi Biblioteca")
    st.write(f"### Estante de: {st.session_state.nombre_autor}")
    st.info("Aquí se almacenarán tus obras terminadas.")

# --- MÓDULO 3: TALLER (IA Activa) ---
elif menu == "🖋️ Taller":
    st.title("🖋️ El Taller Literario")
    
    if not st.session_state.api_key:
        st.error("⚠️ Falta la API Key en el Perfil.")
    else:
        col_in, col_out = st.columns(2)
        
        with col_in:
            st.subheader("Borrador")
            texto_usuario = st.text_area("Escribe aquí:", height=300, placeholder="Escribe el germen de tu idea...")
            
            if st.button("✨ Transformar con RHEMA"):
                if texto_usuario:
                    try:
                        genai.configure(api_key=st.session_state.api_key)
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        
                        prompt = f"Como {st.session_state.nombre_asistente} ({st.session_state.identidad_guia}), reescribe esto con excelencia literaria: {texto_usuario}"
                        
                        with st.spinner("Procesando..."):
                            response = model.generate_content(prompt)
                            st.session_state.resultado_ia = response.text
                    except Exception as e:
                        st.error(f"Error de conexión: {e}")
        
        with col_out:
            st.subheader("Resultado")
            st.markdown(f'<div class="resultado-caja">{st.session_state.resultado_ia}</div>', unsafe_allow_html=True)
