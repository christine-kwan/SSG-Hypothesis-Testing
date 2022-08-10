import streamlit as st
from PIL import Image

st.write('## Skills Extraction Hypothesis test')

image = Image.open(r'logo.png')
st.image(image)
st.write("##### Hypothesis testing experiment to conclude the performance of SEA and JobTech's skills extraction algorithm.")
