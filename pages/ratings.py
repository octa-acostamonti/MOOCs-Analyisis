import streamlit as st
import pandas as pd

coursera_completo = pd.read_csv("./Datasets_normalizados/coursera_normalizado.csv").drop(columns="Unnamed: 0")

st.title("RATINGS")
st.divider()
st.markdown("##### Hipotesis:")
st.write("A partir de estos datos se podra concluir cual es la tematica de curso mejor aceptada entre la demanda.")
st.divider()
st.markdown("##### CANTIDAD DE PERSONAS POR CURSO")
st.dataframe(coursera_completo["course_id"].value_counts().to_frame().sort_values("count",ascending=False))
st.write("A partir de esta data, podemos observar que el curso de Python de la Universidad de Michigan es el que más inscriptos tiene. Con esto se podría pensar en concluir con que el tema a impartir debería ser Python. Pero aún no hemos analizado los ratings.")
st.dataframe()