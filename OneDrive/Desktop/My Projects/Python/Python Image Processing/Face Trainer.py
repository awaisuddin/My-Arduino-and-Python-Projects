import os
import numpy as np
from PIL import Image
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
imagedir = os.path.join(BASE_DIR )

facecascade = cv2.CascadeClassifier('C:/Users/owais/OneDrive/Desktop/Python Image Processing/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = []
x_train = []
y_labels = []

for root, dirs, files in os.walk(imagedir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ","-").lower()
            if not label in label_ids:
                label_ids[label] = current_id
                current_id +=1
            id_ = label_ids[label]
            print(label_ids)
            #ylabels.append(label)
            #xtrain.append(path)
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image,"uint8")
            print(image_array)
            faces = facecascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            #print(faces)
            for(x, y, w, h) in faces:
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids  ,f)

recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainer.yml")
