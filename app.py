import streamlit as st
import pandas as pd
import os
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
# Mostrar resultados como tabla HTML
html = """
<table style="width:100%; border-collapse:collapse;">
<tr style="background-color:#f2f2f2;">
    <th style="padding:8px; border:1px solid #ddd;">Fecha</th>
    <th style="padding:8px; border:1px solid #ddd;">Título</th>
    <th style="padding:8px; border:1px solid #ddd;">Código</th>
</tr>
"""

for _, fila in resultado.iterrows():
    html += f"""
    <tr>
        <td style="padding:8px; border:1px solid #ddd;">{fila['Fecha']}</td>
        <td style="padding:8px; border:1px solid #ddd;">{fila['Título']}</td>
        <td style="padding:8px; border:1px solid #ddd;">
            <a href="fichas/{fila['Código Ficha']}.pdf" target="_blank">
                {fila['Código Ficha']}
            </a>
        </td>
    </tr>
    """

html += "</table>"

st.html(html)


    