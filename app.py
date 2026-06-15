import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador GP", layout="wide")

st.title("📚 Biblioteca Digital de Aprendizajes GP")

st.info(
    "Consulta eventos históricos, lecciones aprendidas y controles asociados para apoyar la planificación y ejecución segura de proyectos."
)

# Cargar Excel
df = pd.read_excel("BD Buscador GP.xlsx")

# Buscador libre
texto = st.text_input("Buscar palabra clave")

# Filtros
disciplina = st.selectbox(
    "Disciplina",
    ["Todas"] + sorted(df["Disciplina"].dropna().unique().tolist())
)

subtipo = st.selectbox(
    "Subtipo",
    ["Todas"] + sorted(df["Subtipo"].dropna().unique().tolist())
)

edc = st.selectbox(
    "EDC",
    ["Todas"] + sorted(df["EDC"].dropna().unique().tolist())
)

equipo = st.selectbox(
    "Equipo involucrado",
    ["Todos"] + sorted(df["Equipo involucrado"].dropna().unique().tolist())
)

codigo_ficha = st.selectbox(
    "Código Ficha",
    ["Todos"] + sorted(df["Código Ficha"].dropna().unique().tolist())
)

# Aplicar filtros
resultado = df.copy()
if texto:
    resultado = resultado[
        resultado.astype(str)
        .apply(lambda row: row.str.contains(texto, case=False, na=False))
        .any(axis=1)
    ]

if disciplina != "Todas":
    resultado = resultado[resultado["Disciplina"] == disciplina]

if subtipo != "Todas":
    resultado = resultado[resultado["Subtipo"] == subtipo]

if edc != "Todas":
    resultado = resultado[resultado["EDC"] == edc]

if equipo != "Todos":
    resultado = resultado[resultado["Equipo involucrado"] == equipo]

if codigo_ficha != "Todos":
    resultado = resultado[resultado["Código Ficha"] == codigo_ficha]

st.write(f"Resultados encontrados: {len(resultado)}")

st.dataframe(resultado, use_container_width=True)
