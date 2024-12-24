import cv2 
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import string

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=2, padding='same', activation='relu', 
                        input_shape=(32, 32, 3)))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=2, padding='same', activation='tanh'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=2, padding='same', activation='tanh'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(26, activation='softmax'))
model.summary()
model.load_weights('./training/model.weights.best_1000.keras')
def predict(image):
    image = cv2.resize(image, (32, 32))
    image = image.reshape(1, 32, 32, 3)
    prediction = model.predict(image)
    return prediction[0]

def get_letter(output):
    max_index = 0
    count = 0
    for i in output:
        if i>output[max_index]:
            max_index = count
        count+=1
    print(max_index)
    return string.ascii_lowercase[max_index]
