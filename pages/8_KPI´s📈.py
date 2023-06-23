import streamlit as st
import pandas as pd


coursera_completo = pd.read_csv("./Datasets_normalizados/coursera_normalizado.csv").drop(columns="Unnamed: 0")
edx = pd.read_csv("./Datasets_normalizados/edx_normalizado.csv").drop(columns="Unnamed: 0")
udemy = pd.read_csv("./Datasets_normalizados/udemy_normalizado.csv").drop(columns="Unnamed: 0")

st.header("KPI´s")
st.divider()
st.write("En este area se presentaran 4 KPI´s que representan las metricas mas importantes a apuntar una vez lanzada la plataforma de MOOCs.")
st.divider()
st.markdown("### **Tasa de Conversion:**")
st.write("Esta metrica representa la proporcionalidad entre, personas inscripitas a cursos pagos contra las personas inscriptas a cursos gratuitos.")
st.markdown("# "+ str(((udemy[udemy["is_paid"]==True]["num_subscribers"].sum()/udemy[udemy["is_paid"]==False]["num_subscribers"].sum())*100).round(2))+"%")
st.write("**Este numero indica que exiten aproximadamente 2 personas suscriptas a cursos pagos por cada 1 persona inscripta a un curso gratuito.**")
st.write("Si proyectamos esta metrica a un crecimiento de un 30% en un año, obtendriamos el siguiente numero")
st.markdown("##### "+ str(((udemy[udemy["is_paid"]==True]["num_subscribers"].sum()/udemy[udemy["is_paid"]==False]["num_subscribers"].sum())*130).round(2))+"%")
st.write("Si se logra crecer esta tasa un 30% en un año, lograriamos tener aproximadamente 3 personas inscriptas a cursos pagos por cada persona inscripta a un curso gratuito.")
st.divider()
st.markdown("### **Rating Promedio de Cursos:**")
st.write("Este KPI indica el rating promedio de los cursos en los datasets analizados.")
st.markdown("# " + str(((coursera_completo["rating"].sum() / coursera_completo["reviews"].size).round(2))))
st.write("Como se logra observar, el promedio de rating es muy alto. Se deberia apuntar a tener buenos instructores y seguir las recomendaciones dadas en este analisis para llegar a tener dicho rating.")
st.divider()
st.markdown("### **Ganancia por Curso:**")
st.write("El KPI presentado evalua la ganancia generada por cada curso.")
kpi_ganancia = (edx["ganancia_curso"].sum()/edx["title"].value_counts().sum()).round(2)
kpi_ganancia1 = (udemy["ganancia_curso"].sum()/udemy["course_title"].value_counts().sum()).round(2)
kpi_ganancia_total = (kpi_ganancia + kpi_ganancia1).round(2)
st.markdown("# "+ str(kpi_ganancia_total) + "$")
st.write("Este KPI nos da un target de ganancias a las que apuntar una vez lanzada la plataforma.")
st.divider()
st.markdown("### **Promedio de duración de Cursos:**")
st.write("El KPI representa el promedio de duracion de los cursos.")
average_course_length = udemy['content_duration'].mean()
st.markdown("# " + str(average_course_length.round(2))+" hrs")
st.write("Este KPI nos da un target de aproximadamente la duracion del contenido impartido.")
















