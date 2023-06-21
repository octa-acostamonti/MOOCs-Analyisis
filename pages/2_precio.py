import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
st.set_option('deprecation.showPyplotGlobalUse', False)


edx = pd.read_csv("./Datasets_normalizados/edx_normalizado.csv").drop(columns="Unnamed: 0")
udemy = pd.read_csv("./Datasets_normalizados/udemy_normalizado.csv").drop(columns="Unnamed: 0")

st.title("PRECIO")
st.divider()

st.markdown("##### Hipotesis:")
st.write("A partir de estos datos se podrá concluir: ")
st.write("* 1. Cursos pagos o gratuitos?")
st.write("* 2. Precio optimo")
st.divider()

st.markdown("##### CURSOS PAGOS VS GRATUITOS")

udemy_paid = udemy[["is_paid","num_subscribers"]]
udemy_paid = udemy_paid.groupby(by="is_paid")["num_subscribers"].sum()
udemy_paid = udemy_paid.to_frame().reset_index()


pagos = st.checkbox("Cursos gratuitos",value=True)
gratis = st.checkbox("Cursos pagos")

if pagos and not gratis:
    color_pagos = "#4c81bf"
    color_gratis = "#a6a6a5"
elif gratis and not pagos:
    color_pagos = "#a6a6a5"
    color_gratis = "#4c81bf"
else:
    color_pagos = "#a6a6a5"
    color_gratis = "#a6a6a5"

fig, ax = plt.subplots()
sns.barplot(data=udemy_paid, x="is_paid", y="num_subscribers", saturation=1, ax=ax,palette=[color_pagos, color_gratis])
sns.despine(left=True, bottom=True)
ax.set_xticklabels(['Falso', 'Verdadero'])
ax.set_xlabel("Es Pago")
ax.set_ylabel("Numero de Suscriptores")
ax.set_yticks([0, 3000000, 8000000])
st.pyplot(fig)  

st.write("Como se puede observar, los cursos que son pagos son ampliamente superiores en términos de cantidad de suscriptores que aquellos que son gratuitos. Esto nos lleva a pensar que lo ideal sería realizar un curso pago.")
















