
import keras
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator 
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm

train = pd.read_csv('train.csv')

train_image = []
for i in tqdm(range(train.shape[0])):
    img = image.load_img('dfgdfgd/'+train['id'][i].astype('str')+'.jpg', target_size=(128,128,3), color_mode="rgb")
    img = image.img_to_array(img)
    img = img/255
    print(img.shape)
    train_image.append(img)
X = np.array(train_image)

y=train['label'].values
y = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

model = Sequential() 
model.add(Conv2D(32, (2, 2), input_shape=(128,128, 3))) 
model.add(Activation('relu')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
  
model.add(Conv2D(32, (2, 2))) 
model.add(Activation('relu')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
  
model.add(Conv2D(64, (2, 2))) 
model.add(Activation('relu')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
  
model.add(Flatten()) 
model.add(Dense(64)) 
model.add(Activation('relu')) 
model.add(Dropout(0.5)) 
model.add(Dense(2)) 
model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy', 
              optimizer='rmsprop', 
              metrics=['accuracy'])






model.summary()

model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))


test_img = []
img = image.load_img('19.png', target_size=(128,128,3), color_mode="rgb")
img = image.img_to_array(img)
img = img/255
test_img.append(img)
test = np.array(test_img)

prediction = model.predict_classes(test)

print (prediction)


