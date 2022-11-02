
import cv2
import numpy as np




contours= cv2.findContours(passedImageGrayThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   

hierarchy = cv2.drawContours(passedImage, contours, -1, (0, 255, 0), 3)




# A combination of:-
# https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/ 

# and

import cv2
import numpy as np

while(1):
    passedImage = cv2.imread('lanes.jpeg')
    filename = 'savedImage.jpg'

    imageHeight, imageWidth = passedImage.shape[:2]
    passedImage2 = cv2.cvtColor(passedImage, cv2.COLOR_BGR2GRAY)
    passedImageGrayThresh = cv2.bitwise_not(cv2.threshold(passedImage2, 45, 255, cv2.THRESH_BINARY)[1])

    contours, hierarchy = cv2.findContours(passedImageGrayThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(passedImage, contours, -1, (0, 255, 0), 3)

    lower_lanes = np.array([0, 0, 0])
    upper_lanes = np.array([20, 20, 125])
    hsv = cv2.cvtColor(passedImage, cv2.COLOR_BGR2HSV)
    maskOurs = cv2.inRange(hsv, lower_lanes, upper_lanes)

    cv2.imwrite(filename, passedImage)
    # Create image mask background
    maskWhite = np.ones(passedImageGrayThresh.shape[:2], dtype="uint8") * 255

# calculate points to be masked based on provided ratio
maskVehicleBoxTopLeftXY = (0, 0)

# calculate points to be masked based on provided ratio
maskVehicleBoxBottomRightXY = (int(imageWidth), int(imageHeight / 2))

maskVehicle = cv2.rectangle(maskWhite, maskVehicleBoxTopLeftXY, maskVehicleBoxBottomRightXY, color=0, thickness=-1)

# Mask out the area of the vehicle
passedImageGrayThreshMasked = cv2.bitwise_and(maskOurs, maskOurs, mask=maskVehicle)
