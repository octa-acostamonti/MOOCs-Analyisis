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


st.markdown("##### RANGO DE PRECIOS")
st.write("Como se puede observar en el siguiente grafico, la cantidad de personas anotada a cursos que tiene un rango de valor entre los 1-50 dolares es superior al resto.")
st.write("Pero, algo interesante pasa cuando observamos la media de la cantidad de subscriptores.")

media = st.checkbox("Media de suscriptores")

edx_pr = edx[["n_enrolled", "price"]]

if media:
    edx_price = edx_pr.groupby("price")["n_enrolled"].mean()
else:
    edx_price = edx_pr.groupby("price")["n_enrolled"].sum()

edx_price = edx_price.to_frame().reset_index()
edx_price.sort_values("n_enrolled", ascending=False, inplace=True)

rangos = [
    (1, 50),
    (51, 100),
    (101, 150),
    (151, 200),
    (201, 250),
    (251, 300),
    (301, 350),
    (351, 400),
    (401, 450)
]
edx_price["price_range"] = pd.cut(edx_price['price'], bins=[r[0]-1 for r in rangos] + [rangos[-1][1]], labels=[f'{r[0]}-{r[1]}' for r in rangos])

if media:
    edx_price = edx_price.groupby('price_range')['n_enrolled'].mean().reset_index()
else:
    edx_price = edx_price.groupby('price_range')['n_enrolled'].sum().reset_index()

colores1 = ['#a6a6a5'] * len(edx_price)
if media:
    colores1[6] = '#4c81bf'  
else:
    colores1[0] = '#4c81bf' 
fig1, ax1 = plt.subplots()
sns.barplot(data=edx_price, x="price_range", y="n_enrolled", saturation=1, ax=ax1, palette=colores1)
sns.despine(left=True, bottom=True)
ax1.set_xlabel("Precio")
if media:
    ax1.set_ylabel("Media de Suscriptores")
else:
    ax1.set_ylabel("Numero de Suscriptores")

ticks = plt.xticks()[0]
if media:
    plt.xticks([ticks[6]])
else:
    plt.xticks([ticks[0]])
st.pyplot(fig1)

st.write("Si analizamos mediante la media, la cantidad de suscriptores promedio de cursos de entre 1-50 dolares cae muy por detras de sus pares, y el rango de precio que emerge es el de entre los 301-350 dolares")
st.divider()
st.markdown("##### Conclusion:")
st.write("Se debe optar por realizar un curso pago donde el rango de precio sea de entre 301-350 dolares")










