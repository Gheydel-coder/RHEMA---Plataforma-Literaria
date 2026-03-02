import streamlit as st

# 1. Configuración de Identidad de la App
st.set_page_config(page_title="RHEMA", page_icon="✒️", layout="wide")

# 2. Estilos Visuales (Lomos de Libros y Diseño)
st.markdown("""
    <style>
    .main { background-color: #f4f1ea; }
    .stSidebar { background-color: #1a1c23; color: white; }
    .lomo-terminado {
        background-color: #4a2c2a; color: #d4af37; padding: 30px 5px;
        border-left: 8px solid #d4af37; border-radius: 3px 10px 10px 3px;
        text-align: center; font-family: 'Georgia', serif; font-weight: bold;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3); 
        writing-mode: vertical-rl; text-orientation: mixed; height: 350px; margin: auto;
    }
    .lomo-proceso {
        background-color: #ffffff; color: #333333; padding: 30px 5px;
        border-left: 8px solid #cccccc; border-radius: 3px 10px 10px 3px;
        text-align: center; font-family: 'Verdana', sans-serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1); border: 1px solid #ddd;
        writing-mode: vertical-rl; text-orientation: mixed; height: 350px; margin: auto;
    }
    .sello-lacre { font-size: 24px; margin-top: 10px; writing-mode: horizontal-tb; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZACIÓN DE MEMORIA (Para que no se borre nada) ---
if 'nombre_autor' not in st.session_state:
    st.session_state.nombre_autor = "Gheydel Guerrero"
if 'rango_autor' not in st.session_state:
    st.session_state.rango_autor = "Maestro"
if 'nombre_asistente' not in st.session_state:
    st.session_state.nombre_asistente = "Elías"
if 'identidad_guia' not in st.session_state:
    st.session_state.identidad_guia = ""

# --- NAVEGACIÓN LATERAL ---
st.sidebar.title("RHEMA")
menu = st.sidebar.radio("Navegación:", ["👤 Perfil de Usuario", "📚 Biblioteca Personal"])

# --- MÓDULO 1: PERFIL DE USUARIO 👤 ---
if menu == "👤 Perfil de Usuario":
    st.title("👤 Perfil de Usuario")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Datos del Autor")
        st.session_state.nombre_autor = st.text_input("Nombre o Seudónimo:", value=st.session_state.nombre_autor)
        
        # Sincronizar el selectbox con la memoria
        opciones_rango = ["Escritor Nobel", "Autor Consagrado", "Maestro"]
        index_rango = opciones_rango.index(st.session_state.rango_autor)
        st.session_state.rango_autor = st.selectbox("Nivel de Experiencia:", opciones_rango, index=index_rango)
        
        tinta = st.number_input("Créditos de Tinta:", value=500)
    
    with col2:
        st.subheader("Configuración del Asistente")
        st.session_state.nombre_asistente = st.text_input("Nombre del Asistente:", value=st.session_state.nombre_asistente)
        st.info("El asistente integra: Mentoría Mística + Edición Técnica + Análisis Estructural.")
        st.session_state.identidad_guia = st.text_area("Personificación del Asistente:", value=st.session_state.identidad_guia, placeholder="Ej: Edgar Allan Poe. Quiero que sea asertivo...")
    
    if st.button("Sellar Configuración"):
        st.success(f"Configuración guardada para {st.session_state.nombre_autor}.")

# --- MÓDULO 2: BIBLIOTECA 📚 ---
elif menu == "📚 Biblioteca Personal":
    st.title("📚 Mi Biblioteca")
    st.write(f"### Estante de: {st.session_state.nombre_autor}")
    st.write(f"**Rango:** {st.session_state.rango_autor}")
    st.write("---")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="lomo-terminado">EL SECRETO DE DENDERA<br><span class="sello-lacre">🔴</span></div>', unsafe_allow_html=True)
        st.caption("Estado: Concluido")
    with col2:
        st.markdown('<div class="lomo-proceso">EL ORINOCO Y EL ONIRONAUTA</div>', unsafe_allow_html=True)
        st.caption("Estado: En proceso")
    with col3:
        st.markdown('<div class="lomo-proceso">NUEVA OBRA</div>', unsafe_allow_html=True)
        st.caption("Estado: En proceso")
    with col4:
        if st.button("➕ Crear Nueva Obra"):
            st.toast("Abriendo el Tintero...")
