import streamlit as st

# 1. Configuración de Identidad de la App
st.set_page_config(page_title="RHEMA", page_icon="✒️", layout="wide")

# 2. Estilos Visuales (Lomos de Libros y Diseño)
st.markdown("""
    <style>
    .main { background-color: #f4f1ea; }
    .stSidebar { background-color: #1a1c23; color: white; }
    .lomo-terminado {
        background-color: #4a2c2a; color: #d4af37; padding: 30px 10px;
        border-left: 8px solid #d4af37; border-radius: 3px 10px 10px 3px;
        text-align: center; font-family: 'Georgia', serif; font-weight: bold;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3); margin-bottom: 20px;
        writing-mode: vertical-rl; text-orientation: mixed; height: 300px; margin: auto;
    }
    .lomo-proceso {
        background-color: #ffffff; color: #333333; padding: 30px 10px;
        border-left: 8px solid #cccccc; border-radius: 3px 10px 10px 3px;
        text-align: center; font-family: 'Verdana', sans-serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1); border: 1px solid #ddd;
        writing-mode: vertical-rl; text-orientation: mixed; height: 300px; margin: auto;
    }
    .sello-lacre { font-size: 24px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN (ICONOS) ---
st.sidebar.title("RHEMA")
menu = st.sidebar.radio("Navegación:", ["👤 Perfil de Usuario", "📚 Biblioteca Personal"])

# --- MÓDULO 1: PERFIL DE USUARIO 👤 ---
if menu == "👤 Perfil de Usuario":
    st.title("👤 Perfil de Usuario")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Datos del Autor")
        nombre = st.text_input("Nombre o Seudónimo:", value="Gheydel Guerrero")
        rango = st.selectbox("Nivel de Experiencia:", ["Escritor Nobel", "Autor Consagrado", "Maestro"])
        tinta = st.number_input("Créditos de Tinta:", value=500)
    
    with col2:
        st.subheader("Configuración del Asistente")
        nombre_asistente = st.text_input("Nombre del Asistente:", value="Elías")
        identidad_guia = st.text_area("Identidad y Personificación:", placeholder="Ej: Edgar Allan Poe. Editor técnico y mentor místico...")
    
    if st.button("Sellar Cambios"):
        st.success("Configuración guardada en el sistema.")

# --- MÓDULO 2: BIBLIOTECA 📚 ---
elif menu == "📚 Biblioteca Personal":
    st.title("📚 Mi Biblioteca")
    st.write(f"### Estante de: {nombre if 'nombre' in locals() else 'Maestro'}")
    st.write("---")
    
    # Representación visual de los libros (Lomos)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="lomo-terminado">EL SECRETO DE DENDERA<br><span class="sello-lacre">🔴</span></div>', unsafe_allow_html=True)
        st.caption("Estado: Concluido")

    with col2:
        st.markdown('<div class="lomo-proceso">EL ORINOCO Y EL ONIRONAUTA</div>', unsafe_allow_html=True)
        st.caption("Estado: En proceso")
        
    with col3:
        st.markdown('<div class="lomo-proceso">PROYECTO NUEVO</div>', unsafe_allow_html=True)
        st.caption("Estado: En proceso")

    with col4:
        # Espacio para añadir obra
        if st.button("➕ Crear Obra"):
            st.info("Iniciando nuevo proceso creativo...")

