from encoder import runEncoder
import multiprocessing
import pickle
import face_recognition
import time
import cv2
from fappeningBookScraper import runTest


start_time = time.time()

unknown_image = face_recognition.load_image_file("new3.jpg")
dataset = {}  
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]


def compare(showImage = False, presetTolerance = 0.6):
    i = 0
    with open('dataset.pickle', 'rb') as handle:
            loadedDataset = pickle.load(handle)
            for loadedKnown in loadedDataset:
                loadedResults = face_recognition.compare_faces([loadedDataset[loadedKnown]], unknown_encoding, tolerance = presetTolerance)
                #print(results)
                if loadedResults[0]:
                    print(loadedKnown)
                    loadedIndex = list(loadedDataset).index(loadedKnown)
                    if showImage:
                        imgResult = cv2.imread('./all/' + loadedKnown)
                        cv2.imshow('pic', imgResult)
                        cv2.waitKey(0)
                    
                    i = i + 1 
                    print(i)
def testFunction():
    print(face_recognition.compare_faces([unknown_encoding], unknown_encoding, tolerance = 0.0001))

#testFunction()
#runEncoder('large')
#compare(showImage = False, presetTolerance= 0.6)
#print("--- %s seconds ---" % (time.time() - start_time))
runTest()

