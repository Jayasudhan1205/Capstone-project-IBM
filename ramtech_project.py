# -*- coding: utf-8 -*-
"""ramtech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MuemQ6FlXUV5VjW_nSwO0PMeIhG_-hdc
"""

from google.colab import drive
drive.mount('/content/drive')

import cv2
loc = '/content/drive/My Drive/project photos/project'

import os
label = []
for i in os.listdir(loc):
  if(i.split('.')[0]== 'non_defective'):
    label.append(0)
  elif(i.split('.')[0]== 'Copy of non_defective'):
    label.append(0)
  else:
    label.append(1)

import pandas as pd
import matplotlib.pyplot as plt
label = pd.DataFrame(label)
label[0].value_counts().plot.bar(rot=0)

label.shape

from tqdm import tqdm
features = []
for i in tqdm(os.listdir(loc)):
  path = os.path.join(loc,i)
  f = cv2.imread(path)
  fr = cv2.resize(f,(70,70))
  features.append(fr)

import numpy as np
X = np.array(features)
Y = np.array(label)
y = np.array(label)

X.shape

Xt = X.reshape(1626,14700)

Xt = Xt/Xt.max()

Xt.shape[1]

import keras
from keras import layers
from keras.utils import to_categorical

model = keras.Sequential()
model.add(layers.Dense(200, activation = 'relu' , input_dim = Xt.shape[1]))
model.add(layers.Dense(100 , activation = 'relu'))
model.add(layers.Dense(2, activation = 'softmax'))

Yt = to_categorical(Y)

Yt

pd.DataFrame(Yt).to_csv('detection_features.csv')

model.summary()

model.compile(optimizer='sgd', loss='categorical_crossentropy',
              metrics = ['accuracy'])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(Xt,Yt,test_size=0.25,random_state =1)

xtrain.shape

ytrain.shape

f= model.fit(xtrain,ytrain,epochs=15)

model.evaluate(xtest,ytest)

model.save('detector.h5')

p = ['non_defective','defective']

k = cv2.imread('/content/test1.jpg')
kt = cv2.resize(k,(70,70))
model.predict(kt.reshape(1,14700))

p[np.argmax(model.predict(kt.reshape(1,14700)))]

plt.imshow(k)
plt.show()

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization

model1 = Sequential()

model1.add(Conv2D(32, (3, 3), activation='relu', input_shape=(70, 70,3)))
model1.add(BatchNormalization())
model1.add(MaxPooling2D(pool_size=(2, 2)))
model1.add(Dropout(0.25))

model1.add(Conv2D(64, (3, 3), activation='relu'))
model1.add(BatchNormalization())
model1.add(MaxPooling2D(pool_size=(2, 2)))
model1.add(Dropout(0.25))

model1.add(Conv2D(128, (3, 3), activation='relu'))
model1.add(BatchNormalization())
model1.add(MaxPooling2D(pool_size=(2, 2)))
model1.add(Dropout(0.25))

model1.add(Flatten())
model1.add(Dense(512, activation='relu'))
model1.add(BatchNormalization())
model1.add(Dropout(0.5))
model1.add(Dense(2, activation='softmax')) # 2 because we have cat and dog classes

model1.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model1.summary()

model1.save('detector_CNN.h5')

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X,Yt,test_size=0.25,random_state =1)

model1.fit(xtrain,ytrain,epochs=15)

model1.evaluate(xtest,ytest)

k = cv2.imread('/content/defective.216.jpg')
kt = cv2.resize(k,(70,70))
model1.predict(kt.reshape(1,70,70,3))

p[np.argmax(model1.predict(kt.reshape(1,70,70,3)))]

plt.figure(figsize=(15,15))
plt.imshow(k)
plt.show()

k1 = cv2.imread('/content/test1.jpg')
kt1 = cv2.resize(k1,(70,70))
model1.predict(kt1.reshape(1,70,70,3))

p[np.argmax(model1.predict(kt1.reshape(1,70,70,3)))]

plt.figure(figsize=(15,15))
plt.imshow(k1)
plt.show()

k3 = cv2.imread('/content/defective.71.jpg')
kt = cv2.resize(k3,(70,70))
print(model1.predict(kt.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k3)
plt.show()

k4 = cv2.imread('/content/non_defective.208.jpg')
kt4 = cv2.resize(k4,(70,70))
print(model1.predict(kt4.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt4.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k4)
plt.show()

k5 = cv2.imread('/content/defective.27.jpg')
kt5 = cv2.resize(k5,(70,70))
print(model1.predict(kt5.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt5.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k5)
plt.show()

k6 = cv2.imread('/content/defective.600.jpg')
kt6 = cv2.resize(k6,(70,70))
print(model1.predict(kt6.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt6.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k6)
plt.show()

k7 = cv2.imread('/content/test3.jpg')
kt7 = cv2.resize(k7,(70,70))
print(model1.predict(kt7.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt7.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k7)
plt.show()

k8 = cv2.imread('/content/test2.jpg')
kt8 = cv2.resize(k8,(70,70))
print(model1.predict(kt8.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt8.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k8)
plt.show()

k9 = cv2.imread('/content/test4.jpg')
kt9 = cv2.resize(k9,(70,70))
print(model1.predict(kt9.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt9.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k9)
plt.show()

k10 = cv2.imread('/content/test10.jpg')
kt10 = cv2.resize(k10,(70,70))
print(model1.predict(kt10.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt10.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k10)
plt.show()

k10 = cv2.imread('/content/test6.jpg')
kt10 = cv2.resize(k10,(70,70))
print(model1.predict(kt10.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt10.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k10)
plt.show()

k10 = cv2.imread('/content/test7.jpg')
kt10 = cv2.resize(k10,(70,70))
print(model1.predict(kt10.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt10.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k10)
plt.show()

k11 = cv2.imread('/content/test9.jpg')
kt11 = cv2.resize(k11,(70,70))
print(model1.predict(kt11.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt11.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k11)
plt.show()

k12 = cv2.imread('/content/test5.jpg')
kt12 = cv2.resize(k12,(70,70))
print(model1.predict(kt12.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt12.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k12)
plt.show()

k13 = cv2.imread('/content/non_defective.208.jpg')
kt13 = cv2.resize(k13,(70,70))
print(model1.predict(kt13.reshape(1,70,70,3)))
print(p[np.argmax(model1.predict(kt13.reshape(1,70,70,3)))])
plt.figure(figsize=(15,15))
plt.imshow(k13)
plt.show()

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))