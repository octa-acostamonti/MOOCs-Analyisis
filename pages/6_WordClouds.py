import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
coursera_completo = pd.read_csv("./Datasets_normalizados/coursera_normalizado.csv").drop(columns="Unnamed: 0")
edx = pd.read_csv("./Datasets_normalizados/edx_normalizado.csv").drop(columns="Unnamed: 0")
udemy = pd.read_csv("./Datasets_normalizados/udemy_normalizado.csv").drop(columns="Unnamed: 0")


st.header("WordClouds")
st.divider()
st.markdown("##### Coursera:")

coursera_titulos = ' '.join(coursera_completo['name'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(coursera_titulos)

# Display WordCloud in Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(fig)
























