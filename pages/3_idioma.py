import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

edx = pd.read_csv("./Datasets_normalizados/edx_normalizado.csv").drop(columns="Unnamed: 0")

edx_lan = edx[["language","n_enrolled"]]
edx_lan.loc[6, 'language'] = 'Japones'
edx_lan.loc[7, 'language'] = 'Chino'

edx_language = edx_lan.groupby("language")["n_enrolled"].sum()
edx_language = edx_language.to_frame().reset_index()
edx_language.sort_values("n_enrolled",ascending=False)

st.title("IDIOMA")
st.divider()

fig, ax = plt.subplots()
sns.barplot(data=edx_language, x="language", y="n_enrolled", saturation=1, ax=ax)
sns.despine(left=True, bottom=True)
ax.set_xlabel("Idioma")
ax.set_ylabel("Numero de Suscriptores")

plt.xticks([2,3]) 
st.pyplot(fig)  

st.write("Como se puede observar, el mercado de cursos en ingles domina a los demas idiomas de manera contundente. De hecho, la suma de todos los demas idiomas no alcanza para llegarle ni a los talones a los numeros de los cursos en ingles.")
st.write("En un analisis mas profundo, se logro desglosar que existe un mercado de aproximadamente 1.700.000 personas que quiere cursos en español, pero solo consigue cursos subtitulados en español. Esto podria ser de gran ventaja para su empresa.")



