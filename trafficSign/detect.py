# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u88nI1EKxk_Eci_nV2cPRUKj3V-5i-jc
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('model')

model.summary()

from tensorflow.keras.preprocessing import image

img_rows, img_cols = 224, 224
img = image.load_img('/content/img_rand.png', target_size=(224,224))
x = np.asarray(img)[None, ...]
# x = image.img_to_array(img)

x.shape

values = model.predict(x)

values

index_max = np.argmax(values)

index_max

import matplotlib.pyplot as plt

model.history.history