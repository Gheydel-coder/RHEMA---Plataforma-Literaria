import streamlit as st
import google.generativeai as genai

# Configuración con la nueva identidad
st.set_page_config(page_title="RHEMA", page_icon="✍️")

st.title("✍️ RHEMA: El Verbo Creador")
st.markdown("### *Donde la voz del autor se convierte en legado*")

# Barra lateral para la llave de poder
st.sidebar.header("Configuración de Soberanía")
api_key = st.sidebar.text_input("Introduce tu Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.write("---")
    st.write("### 🎙️ Dictado de Obra")
    texto_original = st.text_area("Vierte aquí tu palabra:", placeholder="Ejemplo: El nacimiento del amor en primavera...", height=200)

    if st.button("Transformar en Rhema"):
        if texto_original:
            with st.spinner('Procesando el Verbo...'):
                prompt = f"Actúa como un editor literario místico y profundo. Toma el siguiente texto y elévalo a una narrativa épica, manteniendo la esencia del autor pero dándole la fuerza de una obra clásica: {texto_original}"
                response = model.generate_content(prompt)
                
                st.write("### ✨ El Verbo Transformado")
                st.info(response.text)
                
                # Opción para guardar
                st.download_button("Descargar Fragmento", response.text, file_name="rhema_fragmento.txt")
        else:
            st.warning("El silencio no crea. Por favor, escribe o dicta algo.")
else:
    st.info("Para activar el poder de RHEMA, introduce tu API Key en la barra lateral.")
