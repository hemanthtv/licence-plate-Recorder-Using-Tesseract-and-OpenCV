# licence-plate-Recorder-Using-Tesseract-and-OpenCV

# License-Plate-Reading-OCR
I attempt to create a model that is able to 'look' at picture of cars and return the text version of their number plate number. 

## Objective:
It's simple for humans but complex for machines. I attempt to create a model that will look at cars, detect where's the license plate, segment that out and 'read it', return what it read in string format.

## Methodology:
The main method comprises of 2 parts. The objective of the first part is to be able to detect where's the license plate on the car. Using OpenCV, I retrieved the coordinates for where the model detects rectangular boxes. I had to filter these out by the size of the license plate. After sieving through all the non-license plate coordinates, i created a new image of the zoomed license plate. This will make it easier for the next step, which is to read the numbers off the picture. We zoom into the license plate so as to reduce noise and non-essential information. 

Now that we have a zoomed image of the license plate, we implement a module that is able to segment the individual characters in the picture and churn out a string. Now that the bulk of the project is done and dusted, all i had to do was to clean the string for the license plate numbers only.

## Evaluation:
I think more can be done when it comes to cleaning the image before processing it through OpenCV. Perhaps contrasting the image so that OpenCV can better detect rectangles. As of right now the model has trouble looking at images of cars that are taken at night. This could be due to the pixels are being roughly of the same value, and if we reduce the threshold to detect edges, we might end up with more difficulties. 

## Images:

#### The Original Image
![Original](https://github.com/hemanthtv/licence-plate-Recorder-Using-Tesseract-and-OpenCV/blob/master/Original%20Image.jpg)

#### Annotated Image
![Annotated](https://github.com/hemanthtv/licence-plate-Recorder-Using-Tesseract-and-OpenCV/blob/master/Annoted%20Image.png)

#### Zoomed Image
![Zoomed](https://github.com/hemanthtv/licence-plate-Recorder-Using-Tesseract-and-OpenCV/blob/master/Zoomed%20Image.png)

#### Results
![Results](https://github.com/hemanthtv/licence-plate-Recorder-Using-Tesseract-and-OpenCV/blob/master/Results.png)
