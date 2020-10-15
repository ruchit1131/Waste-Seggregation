from keras.models import load_model
from keras.preprocessing import image
model = load_model('2objects')

import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

i = 100000
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
       
        print(frame.size)
        cv2.imwrite(str(i)+".png", frame)
        test_img = []    
        img = image.load_img(str(i)+".png", target_size=(128,128,3), color_mode="rgb")
        img = image.img_to_array(img)
        img = img/255
        test_img.append(img)
        test = np.array(test_img)
        #print(img.shape)

        prediction = model.predict_classes(test)
        
        if prediction[0] == 0:
            print("No object")
        if prediction[0] == 1 or prediction[0] == 2:
            print("Bio degradable")
        if prediction[0] == 3 or prediction[0] == 4:
            print("Non bio-degradable")
        
        os.remove(str(i)+".png")
        #print (prediction)


        cv2.imshow('frame',frame)
        i = i+1
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()


cv2.destroyAllWindows()
