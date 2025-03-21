# -*- coding: utf-8 -*-
"""FashionMNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F22eXRxX4heYrE5xtWlfj0nYrT87xmh5

# Assignment 1, Task 1

---
Authors: Chloe Tap, Evan Meltz, Giulia Rivetti (Group 36)

# Fashion MNIST dataset
"""

# Import libraries
import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt
from tensorflow import keras
import tensorflow as tf
from functools import partial
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout

"""## MLP Model

Load data and divide it into train and test set.

Reshape and scale the data.
"""

'''MLP model on Fashion MNIST dataset'''


# Import libraries
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128
num_classes = 10
epochs = 20

# Split data between train and test sets
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Reshaping
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Scaling
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'Train samples')
print(x_test.shape[0], 'Test samples')

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""### Initializations
1.   Glorot Uniform
2.   Random Normal
3.   Random Uniform
4.   Zeros

"""

model = Sequential()

# Different initializations
initialization = 1 # Initialization flag: change it to use other initializations

if initialization == 1: # weights are random and biases are set to 0
  initializer = tf.keras.initializers.GlorotUniform()
elif initialization == 2: #RandomNormal class initializer
  initializer = tf.keras.initializers.RandomNormal(mean=0., stddev=1.)
elif initialization == 3: # RandomUniform class
  initializer = tf.keras.initializers.RandomUniform(minval=0., maxval=1.)
elif initialization == 4: # Zeros class
  initializer = tf.keras.initializers.Zeros()

"""### Activation Functions:
1.   ReLU
2.   Sidmoid
3.   Softmax
4.   Tanh





"""

activations = ['relu', 'sigmoid', 'softmax', 'tanh']

"""### Optimizers


1.   SGD
2.   Adam
3.   Adamax
4.   AdamW


"""

optimizer_flag = 2
lr = [0.1, 0.01, 0.001]

if optimizer_flag == 1:
  opt=tf.keras.optimizers.SGD(learning_rate=lr[2])
elif optimizer_flag == 2:
  opt=tf.keras.optimizers.Adam(learning_rate=lr[2])
elif optimizer_flag == 3:
  opt=tf.keras.optimizers.Adamax(learning_rate=lr[2])
else:
  optimizer=tf.keras.optimizers.AdamW(learning_rate=lr[2])

"""### MLP architecure

### Regularizers:
1.   L1 on all layers
2.   L1 on first two layers
3.   L2 on all layers
4.   L2 on first two layers


"""

# Regularizers
regularizers = ['l1', 'l2']

# MLP architectures
model = Sequential()
architecture_flag = 1

# With dropout
dropout_rate = [0.1, 0.2, 0.3]
if architecture_flag == 1:
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0],
                  input_shape=(784,)))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(num_classes, activation='softmax', kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))

# Without dropout
if architecture_flag == 2:
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  kernel_regularizer=regularizers[0], input_shape=(784,)))
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))
  model.add(Dense(num_classes, activation='softmax', kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))

# Add 1 dense and droput layers
if architecture_flag == 3:
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0],
                  input_shape=(784,)))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(256, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(num_classes, activation='softmax', kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))

# Remove a dense + dropout layer
if architecture_flag == 4:
  model.add(Dense(512, activation=activations[1], kernel_initializer = initializer,
                  kernel_regularizer=regularizers[0], input_shape=(784,)))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(num_classes, activation='softmax', kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))

# Changing sizes in dense layer
if architecture_flag == 5:
  model.add(Dense(256, activation=activations[1], kernel_initializer = initializer,
                  kernel_regularizer=regularizers[0], input_shape=(784,)))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(256, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(num_classes, activation='softmax', kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))

# Changing sizes in dense layer
if architecture_flag == 6:
  model.add(Dense(256, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0],
                  input_shape=(784,)))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(128, activation=activations[1], kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))
  model.add(Dropout(dropout_rate[1]))
  model.add(Dense(num_classes, activation='softmax', kernel_initializer = initializer,
                  #kernel_regularizer=regularizers[0]
                  ))

"""Compile and fit the model"""

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=opt,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""### Performance for different architectures for the MLP model:
**architecture_flag == 1:**
- **Test loss: 0.3046928346157074**
- **Test accuracy: 0.8924999833106995**

architecture_flag == 2:
- Test loss: 0.34101492166519165
- Test accuracy: 0.8888999819755554

architecture_flag = 3:
- Test loss: 0.306431382894516
- Test accuracy: 0.8920000066757202

architecture_flag = 4:
- Test loss: 0.3157365322113037
- Test accuracy: 0.888700008392334

architecture_flag = 5:
- Test loss: 0.3112395405769348
- Test accuracy: 0.8863999843597412

architecture_flag = 6:
- Test loss: 0.3162446618080139
- Test accuracy: 0.8845999836921692

# CNN Model

Load and reshape data
"""

batch_size = 128
num_classes = 10
epochs = 12

# input image dimensions
img_rows, img_cols = 28, 28


# Load Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# Reshaping
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""### CNN architecture"""

# CNN architecture
model = tf.keras.Sequential()
arch_flag = 3

if arch_flag == 1:
  model.add(Conv2D(32, kernel_size=(3, 3),
                  activation=activations[3],
                  input_shape=input_shape))
  model.add(Conv2D(64, (3, 3), activation=activations[3]))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.1))
  model.add(Flatten())
  model.add(Dense(128, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(num_classes, activation='softmax'))

elif arch_flag == 2:
  model.add(Conv2D(64, kernel_size=(3, 3),
                  activation=activations[3],
                  input_shape=input_shape))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Conv2D(128, (3, 3), activation=activations[3]))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.1))
  model.add(Flatten())
  model.add(Dense(128, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(num_classes, activation='softmax'))

elif arch_flag == 3:
  model.add(Conv2D(32, kernel_size=(3, 3),
                  activation=activations[3],
                  input_shape=input_shape))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.1))
  model.add(Flatten())
  model.add(Dense(128, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(num_classes, activation='softmax'))

if arch_flag == 4:
  model.add(Conv2D(32, kernel_size=(3, 3),
                  activation=activations[3],
                  input_shape=input_shape))
  model.add(Conv2D(64, (3, 3), activation=activations[3]))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.1))
  model.add(Flatten())
  model.add(Dense(128, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(64, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(num_classes, activation='softmax'))

if arch_flag == 5:
  model.add(Conv2D(128, kernel_size=(3, 3),
                  activation=activations[3],
                  input_shape=input_shape))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Conv2D(256, (3, 3), activation=activations[3]))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.1))
  model.add(Flatten())
  model.add(Dense(128, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(64, activation=activations[3]))
  model.add(Dropout(0.1))
  model.add(Dense(num_classes, activation='softmax'))

model.summary()

"""Compile, fit and evaluate the model"""

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.AdamW(learning_rate=0.001),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""### Performance for different architectures for CNN model:

arch_flag = 1:
- Test loss: 0.2668193578720093
- Test accuracy: 0.9121000170707703

arch_flag = 2:
- Test loss: 0.27006328105926514
- Test accuracy: 0.9093999862670898

arch_flag = 3:
- Test loss: 0.27031201124191284
- Test accuracy: 0.9053999781608582

**arch_flag = 4:**
- **Test loss: 0.26930156350135803**
- **Test accuracy: 0.9146999716758728**

arch_flag = 5:
- Test loss: 0.26973482966423035
- Test accuracy: 0.9128999710083008
"""