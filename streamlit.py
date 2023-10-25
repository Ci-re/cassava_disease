import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from PIL import Image
import pickle
import tensorflow as tf
from keras.applications.resnet50 import preprocess_input, decode_predictions
import cv2

st.title('Cassava Disease Image Prediction Using CNN')

IMAGE_SIZE = 255
uploaded_file = st.file_uploader("Choose a file", type=['png','jpg','jpeg'])

if uploaded_file is not None:
    st.image(uploaded_file)

    def load_model():
        model = pickle.load(open("resnet_model.pkl", "rb"))
        image = Image.open(uploaded_file)
        img = image.resize((225, 225))
        img_array = preprocess_input(np.array(img))
        image = np.expand_dims(img_array, axis=0)
        prediction = model.predict(image)
        return prediction[0]

    prediction = load_model()
    st.write(prediction)