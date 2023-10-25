import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from PIL import Image
from keras.optimizers import Adam, SGD
from keras.preprocessing.image import ImageDataGenerator

from keras.models import Sequential
from keras.layers import Dropout, Activation, BatchNormalization, Dense
from keras.layers import MaxPooling2D, Conv2D, Flatten
from keras.utils import to_categorical




class PrepareData:
    
    def __init__(self) -> None:
        pass
    
    def __init__(self, *args, **kwargs):
        super(CLASS_NAME, self).__init__(*args, **kwargs)
    
    