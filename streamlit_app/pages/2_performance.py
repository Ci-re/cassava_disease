import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from keras.models import model_from_json
import altair as alt
import numpy as np


st.set_page_config(page_title="Model Evaluation", page_icon="✅")

st.markdown("# Models Evaluation")
st.sidebar.header("Evaluation")
st.write(
    """We will be evaluating our models here"""
)

path = "models/"
def load_json(file_name):
    with open(path+file_name, 'r') as json_file:
        json_savedModel = json_file.read() 
    return model_from_json(json_savedModel)

# @st.cache_data
model_ = load_json("resnet_model.json")
st.write("Model Summary:")
model_.summary(print_fn=lambda x: st.text(x))

col1, col2 = st.columns(2)
with col1:
    json_ = path+"evaluation.json"
    data = pd.read_json(json_)
    dat = data[["resnet_acc", "resnet_valacc"]]
    dat['index'] = dat.index
    dat = pd.melt(dat, id_vars="index", value_vars=['resnet_acc', 'resnet_valacc'])
    
    alt_chart = alt.Chart(dat).mark_line().encode(
        alt.X("index", title="Epochs").scale(zero=False),
        alt.Y("value", title="Loss").scale(zero=False),
        color = "variable"
    )
    st.altair_chart(alt_chart)
    
with col2:
    json_ = path+"evaluation.json"
    data = pd.read_json(json_)
    dat = data[["resnet_loss", "resnet_val_loss"]]
    dat['index'] = dat.index
    dat = pd.melt(dat, id_vars="index", value_vars=['resnet_loss', 'resnet_val_loss'])
    
    alt_chart = alt.Chart(dat).mark_line().encode(
        alt.X("index",title="Epochs").scale(zero=False),
        alt.Y("value", title="loss").scale(zero=False),
        color = "variable"
    )
    st.altair_chart(alt_chart)