import streamlit as st
import time
import pathlib
import numpy as np

st.set_page_config(page_title="Descriptive Stats", page_icon="📈")

st.markdown("# Descriptive Statistics")
st.sidebar.header("Descriptive Stat")
st.write(
    """This page gives us a summary of our dataset"""
)

path = "cassava leaf disease dataset/"
data_dir = pathlib.Path(path)

Cbb = list(data_dir.glob('Cassava CB (Cassava Blight)/*'))
Cmd = list(data_dir.glob('Cassava CM (Cassava Mosaic)/*'))
Chl = list(data_dir.glob('Cassava Healthy Leaf/*'))


col1, col2, col3 = st.columns(3)

with col1:
    st.image(str(Cbb[0]), caption="Cassava Bacteria Blight")

with col2:
    st.image(str(Chl[0]), caption="Cassava Healthy Leaf")

with col3:
    st.image(str(Cmd[0]), caption="Cassava Mosaic Disease")

data = {"Bacteria Blight" : len(Cbb), "Mosaic Disease": len(Cmd), "Healthy Leaf": len(Chl) }

st.bar_chart(data)

st.text(f'Bacteria Blight: {len(Cbb)}')
st.text(f'Mosaic Disease: {len(Cmd)}')
st.text(f'Healthy Leaf: {len(Chl)}')