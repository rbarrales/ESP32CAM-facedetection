#emotion_detection.py
import cv2
from deepface import DeepFace
import numpy as np  #this will be used later in the process

imgpath = "/home/rbg/Arduino/ESP32CAM-face/RBG_060721.jpg"
analyze = DeepFace.analyze(imgpath, actions=['emotion', 'age', 'gender', 'race'], models={}, enforce_detection=False)
print(analyze)