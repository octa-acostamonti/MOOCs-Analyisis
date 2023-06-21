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


fig, ax = plt.subplots()
sns.barplot(data=edx_language, x="language", y="n_enrolled", saturation=1, ax=ax)
sns.despine(left=True, bottom=True)
ax.set_xlabel("Numero de Suscriptores")
ax.set_ylabel("Idioma")
st.pyplot(fig)  

st.write