import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


edx = pd.read_csv("./Datasets_normalizados/edx_normalizado.csv").drop(columns="Unnamed: 0")
edx_lev = edx[["Level","n_enrolled"]]
edx_level = edx_lev.groupby("Level")["n_enrolled"].sum()
edx_level = edx_level.to_frame().reset_index()
edx_level.sort_values("n_enrolled",ascending=False,inplace=True)

st.title("NIVEL")
st.divider()
st.markdown("##### Hipotesis:")
st.write("Mediante los datos de el nivel de los cursos se podra concluir cual es el mejor nivel para ofrecer.")
st.divider()
st.markdown("##### Cantidad de Suscriptores por Nivel")
fig, ax = plt.subplots()
colores = ['#4c81bf'] + ['#a6a6a5'] * (len(edx_level) - 1)
sns.barplot(data=edx_level, x="n_enrolled", y="Level", saturation=1, ax=ax,palette=colores)
sns.despine(left=True, bottom=True)
ax.set_xlabel("Numero de Suscriptores")
ax.set_ylabel("Nivel")
st.pyplot(fig)  
st.write("En este grafico se puede observar como los cursos que son de nivel Introductorio son los que mas cantidad de suscriptores tienen. Los cursos Avanzados son los que menos tienen. Esto habla de que existe una alta tasa de personas que no cumplen los cursos o que no esta lo suficientemente capacitada como para abordar dicho nivel.")
st.write("Pero, hay otro analisis que me gustaria que observen.")



edx_ganancia = edx[["Level","ganancia_curso"]].groupby("Level")["ganancia_curso"].mean().sort_values(ascending=False).round(2).to_frame().reset_index()


fig1, ax1 = plt.subplots()
colores1 = ['#4c81bf'] + ['#a6a6a5'] * (len(edx_level) - 1)
sns.barplot(data=edx_ganancia, x="ganancia_curso", y="Level", saturation=1, ax=ax1,palette=colores1)
sns.despine(left=True, bottom=True)
ax1.set_xlabel("Ganancias")
ax1.set_ylabel("Nivel")
st.pyplot(fig1)  

st.write("Si se toma en cuenta la ganancia que se podria tener por cusro, nos damos cuenta que los cursos Avanzados son los que mayor ganancia tienen. Esto es por que son mas especificos y, por tanto, pueden permitirse cobrar mas por curso (El precio lo vimos paginas anteriores.)")
st.write("En esta pequeña tablita podemos observar como la cantidad de cursos Avanzados es infima en comparacion con los demas niveles.")
st.write(edx["Level"].value_counts())
st.divider()
st.markdown("##### Conclusion:")
st.write("En una primera instancia se podria pensar en hacer cursos introductorios, pero la oferta ya acapara esa demanda. Ya existen suficientes cursos introductorios y existe un mercado de personas que supera ese nivel que no sigue ya que hay una falta de oferta.")












