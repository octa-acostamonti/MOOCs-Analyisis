import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

edx = pd.read_csv("./Datasets_normalizados/edx_normalizado.csv").drop(columns="Unnamed: 0")
edx_len = edx[["n_enrolled","course_length"]]
edx_lenght = edx_len.groupby("course_length")["n_enrolled"].mean()
edx_lenght = edx_lenght.to_frame().reset_index()
rangos_semanas = [
    (1, 4),
    (5, 8),
    (9, 12),
    (13, 16),
    (17, 20)
]
def rango_semanas(semanas):
    for r in rangos_semanas:
        if r[0] <= semanas <= r[1]:
            return f"{r[0]}-{r[1]}"
    return np.nan

edx_lenght["rango_semanas"] = edx_lenght["course_length"].str.extract("(\d+)").astype(int).applymap(rango_semanas)

edx_lenght = edx_lenght.groupby("rango_semanas")["n_enrolled"].sum().reset_index()
edx_lenght.sort_values("n_enrolled",ascending=False,inplace=True)
st.title("TIEMPO")
st.divider()
fig, ax = plt.subplots()
sns.barplot(data=edx_lenght, x="rango_semanas", y="n_enrolled", saturation=1, ax=ax)
sns.despine(left=True, bottom=True)
ax.set_xlabel("Tiempo en semanas")
ax.set_ylabel("Numero de Suscriptores")
st.pyplot(fig)  

st.write("Se puede observar en el grafico que, el rango de tiempo optimo para hacer un curso es entre 9 y 12 semanas.")