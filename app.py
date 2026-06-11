import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador GP", layout="wide")

st.title("🔍 Buscador de Aprendizajes GP")

# Cargar Excel
df = pd.read_excel("BD Buscador GP.xlsx")

# Buscador libre
texto = st.text_input("Buscar palabra clave")

# Filtros
disciplina = st.selectbox(
    "Disciplina",
    ["Todas"] + sorted(df["Disciplina"].dropna().unique().tolist())
)

empresa = st.selectbox(
    "Empresa",
    ["Todas"] + sorted(df["Empresa"].dropna().unique().tolist())
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

if empresa != "Todas":
    resultado = resultado[resultado["Empresa"] == empresa]

st.write(f"Resultados encontrados: {len(resultado)}")

st.dataframe(resultado, use_container_width=True)
