import face_recognition
import os
import glob
import time
import PIL
import cv2
import json
import numpy as np
import pickle

def runEncoder(model = 'small'):
    start_time = time.time()
    parent_dir = './testData'
    known_image = face_recognition.load_image_file("test1.jpg")
    unknown_image = face_recognition.load_image_file("test5.jpg")
    dataset = {} 
    names = [os.path.basename(f) for f in glob.glob(os.path.join(parent_dir, '*.jpg'))]

    for name in names:
        try:
            known_image = face_recognition.load_image_file('./testData/' + str(name))
            dataset[name] = (face_recognition.face_encodings(known_image, model = model)[0])
            print('###')
            index = list(dataset).index(name)
            print((index/len(names) * 100).__round__(2))
        except(PIL.UnidentifiedImageError, IndexError):
            os.remove('./testData/' + name) 
            pass

    print(len(dataset))
    with open('testDataset.pickle', 'wb') as handle:
        pickle.dump(dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("--- %s seconds ---" % (time.time() - start_time))


#runEncoder()