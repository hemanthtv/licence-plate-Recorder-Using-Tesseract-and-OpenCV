import cv2
from imutils import contours
import pytesseract
import re
import numpy as np
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd=r"c:\Program Files\Tesseract-OCR\tesseract.exe"

plate = cv2.imread(r'C:\Users\Hemanth\Desktop\License-Plate-Reading-OCR-master\License-Plate-Reading-OCR-master\example_2.jpg')
plate = cv2.cvtColor(plate, cv2.COLOR_BGR2RGB)
plate_cascade = cv2.CascadeClassifier(r'C:\Users\Hemanth\AppData\Roaming\JetBrains\PyCharmCE2020.2\scratches\scratch.xml')

# function that will automate the usage of the model to identify the car plate in the image
def detect_plate(img):
       plate_img = img.copy()

       # getting the coordinates of the carplate in the image
       plate_coord = plate_cascade.detectMultiScale(plate_img, scaleFactor = 1.2,minNeighbors = 10)
       # drawing the rectangle
       for x, y, w, h in plate_coord:
              cv2.rectangle(img = plate_img, pt1 = (x, y), pt2 = (x + w, y + h), color = (255, 0, 0), thickness = 5)
       return plate_img

anno_plate = detect_plate(plate)
plt.imshow(anno_plate)

# function that would zoom into the bounding box
def zoom_plate(img):
       plate_img = img.copy()

       # getting the coordinates of the carplate in the image
       plate_coord = plate_cascade.detectMultiScale(plate_img, scaleFactor = 1.2,minNeighbors = 10)
       
       for x, y, w, h in plate_coord:
              # getting the points that show the license plate
              zoomed_img = plate_img[y:y+h, x:x+w]
              # resizing
              zoomed_img = cv2.resize(zoomed_img, (0, 0), fx = 2, fy = 2)
              kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
              zoome_img = cv2.filter2D(zoomed_img, -1, kernel)
              return zoome_img

zoomed_plate = zoom_plate(plate)
plt.imshow(zoomed_plate)
def plate_string(img):
       # extract all strings from the image
       text = pytesseract.image_to_string(img)

       # clean the string
       text = re.sub("[^a-zA-Z1234567890]", ' ', text).split(' ')
       text = [i for i in text if i != '']
       text = [i for i in text if re.search('[0-9]', i)]
       if len(text) == 1:
              return text[0]
       return text
print('THE NO. PLATE SHOWS:')
print(plate_string(zoomed_plate))
