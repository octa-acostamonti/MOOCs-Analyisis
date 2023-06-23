import streamlit as st
import pandas as pd

coursera_completo = pd.read_csv("./Datasets_normalizados/coursera_normalizado.csv").drop(columns="Unnamed: 0")

st.title("RATINGS")
st.divider()

st.markdown("##### Hipotesis:")
st.write("A partir de estos datos se podrá concluir cuál es la temática de curso mejor aceptada entre la demanda.")
st.divider()

st.markdown("##### CANTIDAD DE PERSONAS POR CURSO")
st.dataframe(coursera_completo["course_id"].value_counts().to_frame().sort_values("count",ascending=False))
st.write("A partir de esta data, podemos observar que el curso de Python de la Universidad de Michigan es el que más inscriptos tiene. Con esto se podría pensar en concluir con que el tema a impartir debería ser Python. Pero aún no hemos analizado los ratings.")

st.markdown("##### CANTIDAD DE VOTOS POR CURSO")
st.dataframe(coursera_completo.groupby('course_id')['rating'].value_counts().unstack(fill_value=0))

rating_conteo = coursera_completo.groupby('course_id')['rating'].value_counts().unstack(fill_value=0)
rating_porcentaje = rating_conteo.div(rating_conteo.sum(axis=1), axis=0) * 100

st.write("En esta tabla se puede observar como varía la votación de cada curso. A pesar de esto, es muy difícil todavía concluir cual es el curso más valorado por la demanda.")
st.write("Para poder efectivamente saber cuales son los cursos más valorados entre la demanda se calculará el porcentaje de cada curso. Se mostrará aquellos cursos que fueron votados con 5 y tienen mayor porcentaje que el resto.")

st.markdown("##### PORCENTAJE DE PERSONAS QUE VALORARON CON 5")

st.dataframe(rating_porcentaje[5].sort_values(ascending=False).to_frame().round(2))

st.write("Aqui se puede observar que el curso mejor valorado es el de Science of the well being, mientras que el peor es Python.")

st.divider()

st.markdown("##### Conclusion:")

st.write("Si bien se podría pensar en primera instancia que realizar un curso sobre Science of well being sería la opción viable y segura, no es lo que vengo a proponer. La demanda sobre ese tema en específico ya está acaparada. No es necesario que se cree otro curso,la demanda está satisfecha. Como observamos en la primera tabla, Python es el tema que más personas inscriptas tiene, es decir, hay mucha demanda sobre dicha temática. Sin embargo, en el análisis de satisfacción con el producto, encontramos que los cursos disponibles no son valorados positivamente. Esto deja un espacio en el mercado para que su empresa entre y monopolice ese contenido. De hecho, las últimas 4 peores valoradas son temáticas relacionadas con Python. (Deep Learning,Machine Learning, Data Science y Python) Hay todo un cúmulo de personas que quieren aprender Python pero no están pudiendo con lo ofertado. Aquí deberian entrar ustedes.")

st.write("\* *toda la informacion fue extraida de coursera* ")





