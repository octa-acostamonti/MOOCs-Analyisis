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
st.markdown("##### Hipotesis:")
st.write("Con el resultado de este analisis se podra justificar el idioma de los cursos a impartir en su empresa.")
st.divider()
st.markdown("##### Numero de Suscripciones por Idioma")
fig, ax = plt.subplots()
sns.barplot(data=edx_language, x="language", y="n_enrolled", saturation=1, ax=ax)
sns.despine(left=True, bottom=True)
ax.set_xlabel("Idioma")
ax.set_ylabel("Numero de Suscriptores")
ax.set_xticklabels(ax.get_xticklabels(), fontsize=8)
plt.xticks([2,3]) 
st.pyplot(fig)  

st.write("Como se puede observar, el mercado de cursos en ingles domina a los demas idiomas de manera contundente. De hecho, la suma de todos los demas idiomas no alcanza para llegarle ni a los talones a los numeros de los cursos en ingles.")
st.code("cursos_español = edx[edx['language'].str.contains('Spanish', na=False) | edx['subtitles'].str.contains('Español', na=False, case=False, regex=False)]",language="python")

cursos_español = edx[edx['language'].str.contains('Spanish', na=False) | edx['subtitles'].str.contains('Español', na=False, case=False, regex=False)]
almenos_español = cursos_español['n_enrolled'].sum()


st.write("Con el codigo expuesto arriba se logro desglosar todos los cursos dispobibles en el dataset que tengan al menos Español (idioma o subtitulos). Luego se resto ese numero con la cantidad de suscriptores anotados en cursos en Español y se llego al numero de:")
st.write(almenos_español - edx_language["n_enrolled"].iloc[3])
st.write("A partir de este numero, con cierto margen de error, se podria observar que existe un mercado de aproximadamente 1.700.000 personas que buscan contenido en español pero no lo encuentran. De hecho si se quiere dar un margen de error del 50%, seguirian habiendo unas 850.000 personas. Incluso con un margen de error del 95%, siguen existiendo 88.000 personas que buscan cursos en español de calidad.")
st.divider()
st.markdown("##### Conclusion:")
st.write("Si bien es evidente que el numero de suscriptores en cursos en ingles es holgadamente superior al resto, existe un mercado de personas que buscan cursos en español de calidad que la oferta no esta pudiendo satisfacer. Ahi es donde ustedes, como empresa, deberian ingresar.")




