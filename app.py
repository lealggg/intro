import streamlit as st 
from PIL import Image 
st.title (" Leal G!!")

st.header(" En este espacio encontraras informacion sobre leal g ")
st.write(" Conoceras facilmente a este personaje ")
image = Image.open ("leal.jpeg")

st.image(image, caption="leal")
texto = st.text_input("escribe algo", "este es mi texto")
st.write("el texto escrito es ", texto)

st.subheader("ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("esta es la primera columna")
  st.write("leal gg es una gran persona ")
  resp = st.checkbox("estoy de acuerdo")
  if resp:
    st.write("correcto!")
    
with col2:
  st.subheader("esta es la segunda columna")
  modo = st.radio("que modalidad es la principal en tu interfaz", ("visual", "auditiva", "tactil"))
  if modo == "visual":
    st.write("la vista es fundamental para tu intefaz ")
  if modo == "auditiva":
    st.write("la audicion es fundamental para tu interfaz")
  if modo == "tactil":
    st.write("el tacto es fundamental para tu interfaz")

  
    
