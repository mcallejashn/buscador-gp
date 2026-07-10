import os
import streamlit as st

st.set_page_config(page_title="Ver ficha", layout="wide")

codigo = st.query_params.get("codigo")

st.title("📄 Ver ficha")

if not codigo:
    st.info("Selecciona una ficha desde la Biblioteca Digital.")
    st.stop()

ruta_pdf = f"fichas/{codigo}.pdf"

if not os.path.exists(ruta_pdf):
    st.error(f"La ficha {codigo} todavía no está disponible.")
    st.stop()

st.subheader(f"Ficha {codigo}")

st.pdf(ruta_pdf, height=900)

with open(ruta_pdf, "rb") as archivo_pdf:
    st.download_button(
        label="⬇ Descargar ficha PDF",
        data=archivo_pdf,
        file_name=f"{codigo}.pdf",
        mime="application/pdf",
    )