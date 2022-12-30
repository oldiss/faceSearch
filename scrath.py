from fappeningBookScraper import runTest
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import os
import glob

imgPath2 = './test4.png'
results = []
outputNames =[]
parent_dir = './all'
results = [os.path.basename(f) for f in glob.glob(os.path.join(parent_dir, '*.jpg'))]
#print(results)
#print(len(results))
i = 0
img2 = cv2.imread(imgPath2)
for name in results:
    try:
        imgPath1 = './all/' + name
        img1 = cv2.imread(imgPath1)
        result = DeepFace.verify(img1, img2)
        if (result['verified'] == True):
            outputNames.append(name)
            #cv2.imshow(name, img1)
            
            
        else:
            print('###\n')
            print(imgPath1)
            print('###\n')
    except(TypeError,ValueError):
        i = i + 1
        print(i)
        print('/////\n')

for pic in outputNames:
    imgResult = cv2.imread('./testData/' + pic)
    cv2.imshow('pic', imgResult)
    cv2.waitKey(0)
print(outputNames)





#print()

#result = DeepFace.verify(img1, img2)

#print(img1)