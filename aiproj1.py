# -*- coding: utf-8 -*-
"""aiproj1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v9-cGbfC1qGZSlXOGjF99oS_2Wt5yx_S

Imports
"""

import tensorflow as tf
from numpy import unique, argmax
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import plot_model

from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np

"""Data Preprocessing"""

##load dataset into training (input and output) and test (input and output) sets
(x_train, y_train), (x_test, y_test) = load_data()

#reshaping training and testing data
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1],
x_train.shape[2], 1))                           
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], x_test.shape[2], 1))

#normalize (scale) the values of piexels of images
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

#determine the shape of the input images
img_shape = x_train.shape[1:]

#defining the model
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape = img_shape))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Dropout(0.5)) #dropout weight (50%) to reduce overfitting
model.add(Flatten()) #flattens input, makes array 1d
model.add(Dense(400, activation='relu'))
model.add(Dense(10, activation='softmax')) #output

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
x = model.fit(x_train, y_train, epochs=10, batch_size=1024, verbose=2, validation_split=0.2)

loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f'Accuracy: {accuracy*100}')