### IMPORTS
from __future__ import absolute_import, division, print_function, unicode_literals
import os
import tensorflow as tf
import sys #sys.argv[1]
from tensorflow.keras import datasets, layers, models
from sklearn import svm
from sklearn.model_selection import learning_curve
import numpy as np
import random
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from sklearn.preprocessing import LabelEncoder

### PARAMATERS
CLASSES = [chr(x) for x in range(65,91)]
INPUT_FILE = sys.argv[1]
DF = None
X = None
MODEL_CHKPNT = "../output/cp.ckpt"
MODEL_CHKPNT_DIR = os.path.dirname(MODEL_CHKPNT)
MODEL = None
PRED_INDEX = None
PRED = None

### LOAD MODEL
def Create_Model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())

    model.add(layers.Dense(400, activation='tanh'))
    model.add(layers.Dense(200, activation='tanh'))
    model.add(layers.Dense(26, activation='softmax'))
    # model.summary()

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    return model

MODEL = Create_Model()
MODEL.load_weights(MODEL_CHKPNT)

### LOAD INPUT DATA
DF = pd.read_csv(INPUT_FILE)
X = np.array(DF)

### PREPROCESS INPUT DATA
def preprocess(X):
    X = X.astype(np.float64) / 100
    X = np.tanh(X)
    X = X.reshape(1,28,28,1)
    return X
X = preprocess(X)

### CLASSIFY INPUT DATA
PRED_INDEX = MODEL.predict_classes(X)[0]
PRED = CLASSES[PRED_INDEX]

### IGNORE OUTPUT END
print("OUTPUT")

### PRINT TO CONSOLE
print(PRED)
