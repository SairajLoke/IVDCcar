from cv2 import VideoCapture
import numpy as np
import cv2
  
# Reading image
# font = cv2.FONT_HERSHEY_COMPLEX

# # img_path = r'C:\Users\Sairaj Loke\Downloads\file\content\RPIIMG\contourtest..jpg'
# img_path = r'C:\Users\Sairaj Loke\Downloads\file\content\RPIIMG\st_lanes.jpg'


# img2 = cv2.imread(img_path, cv2.IMREAD_COLOR)
# cv2.imshow('myimg' ,img2)


# # Reading same image in another 
# # variable and converting to gray scale.
# img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
  
# # Converting image to a binary image
# # ( black and white only image).
# _, thresholdimg = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY)
  
# # Detecting contours in image.
# contours, _ = cv2.findContours(thresholdimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
# # print(_)

# # cv2.imshow('_', _)
# count = 0 
# # Going through every contours found in the image.
# for cnt in contours :
  

#     print(f"contour {count} : length: {len(contours[count])}    cnt {contours[count]}")

#     approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True)  , True)
  
#     # draws boundary of contours.
#     cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 
  
#     # Used to flatted the array containing
#     # the co-ordinates of the vertices.
#     n = approx.ravel() 
#     i = 0
  
#     for j in n :
#         if(i % 2 == 0):
#             x = n[i]
#             y = n[i + 1]
  
#             # String containing the co-ordinates.
#             string = str(x) + " " + str(y) 
  
#             if(i == 0):
#                 # text on topmost co-ordinate.
#                 cv2.putText(img2, "Arrow tip", (x, y),
#                                 font, 0.5, (255, 0, 0)) 
#             else:
#                 # text on remaining co-ordinates.
#                 cv2.putText(img2, string, (x, y), 
#                           font, 0.5, (0, 255, 0)) 
#         i = i + 1
  
#     count += 1 
# # Showing the final image.
# cv2.imshow('image2', img2) 
  
# # Exiting the window if 'q' is pressed on the keyboard.
# if cv2.waitKey(0) & 0xFF == ord('q'): 
#     cv2.destroyAllWindows()


#Testing
    # if self.testAllConfigs:
    #     if self.stage == 0:
    #         self.get_logger().info("\nPublishing lines Left to Right, points NOT switched")
    #         self.sortRightToLeft=False
    #         self.switchVectorPoints=False
    #         self.startTime = self.timeStamp
    #         self.stage = 1
    #     elif (((self.timeStamp - self.startTime) > 30*1e6) and (self.stage == 1)):
    #         self.sortRightToLeft=False
    #         self.switchVectorPoints=True
    #         self.stage = 2
    #         self.get_logger().info("\nPublishing lines Left to Right, points ARE switched")
    #     elif (((self.timeStamp - self.startTime) > 40*1e6) and (self.stage == 2)):
    #         self.sortRightToLeft=True
    #         self.switchVectorPoints=False
    #         self.stage = 3
    #         self.get_logger().info("\nPublishing lines Right to Left, points NOT switched")
    #     elif (((self.timeStamp - self.startTime) > 50*1e6) and (self.stage == 3)):
    #         self.sortRightToLeft=True
    #         self.switchVectorPoints=True
    #         self.stage = 4
    #         self.get_logger().info("\nPublishing lines Right to Left, points ARE switched")
    
    # img_rgb = cv2.imread('right.png')
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # template = passedImage
    # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # w, h = template.shape[::-1]
    # res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF_NORMED)
    # threshold = 0.40
    # loc = np.where( res >= threshold)
    # r=0
    # for pt in zip(*loc[::-1]):
    #     r=r+1
    
    # if(r>0):
    #     answer = answer + 1.0
    


# img_path = r'C:\Users\Sairaj Loke\Downloads\file\content\RPIIMG\contourtest..jpg'
img_path = r'C:\Users\Sairaj Loke\Downloads\file\content\RPIIMG\st_lanes.jpg'


img2 = cv2.imread(img_path, cv2.IMREAD_COLOR)
cv2.imshow('myimg' ,img2)

# passedImage = img2

# vid = VideoCapture(0)

(pX0,pY0, pX1, pY1) = (0,1,2,3)





def findLines(passedImage):

    #convert image to grayscale
    passedImageGray = cv2.cvtColor(passedImage,cv2.COLOR_BGR2GRAY)
    
    #Image dimensions
    imageHeight, imageWidth = passedImageGray.shape[:2]
    
    #Threshold image black and white
    passedImageGrayThresh = cv2.bitwise_not(cv2.threshold(
        passedImageGray, 80, 255, cv2.THRESH_BINARY)[1])
    
    
    # lower_lanes = np.array([0,0,50])
    # upper_lanes = np.array([0,0,65])
    # hsv = cv2.cvtColor(passedImage, cv2.COLOR_BGR2HSV)
    # maskOurs = cv2.inRange(hsv, lower_lanes, upper_lanes)
    # #h,s,v1 = cv2.split(maskOurs)
    
    # lower_right = np.array([29, 253, 253])
    # upper_right = np.array([31,255,255])

    # maskRight = cv2.inRange(hsv, lower_right, upper_right)

    # if not cv2.countNonZero(maskRight) == 0:
    #     answer = answer + 10.0
        
    # lower_bumpy = np.array([25, 130, 139])
    # upper_bumpy = np.array([31, 136, 148])        

    # hsv_bumpy = cv2.cvtColor(passedImage , cv2.COLOR_BGR2HSV)
    # mask_bumpy = cv2.inRange(hsv , lower_bumpy, upper_bumpy)

    # if not cv2.countNonZero(mask_bumpy) == 0:
    #     answer = answer + 100.0
        
    # lower_blue = np.array([95, 168, 155])
    # upper_blue = np.array([108, 180, 165])
    # mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    # if not cv2.countNonZero(mask_blue) == 0:
    #     answer = answer + 1000.0
        
    # lower_green = np.array([43,190,245])
    # upper_green = np.array([50,210,255])
    # hsv = cv2.cvtColor(passedImage, cv2.COLOR_BGR2HSV)
    # mask_green = cv2.inRange(hsv, lower_green, upper_green)
    # if not cv2.countNonZero(mask_green) == 0:
    #     answer = answer + 10000.0
        
    # (self.flag).data = answer 
    
    
    # #Create image mask background
    # maskWhite = np.ones(passedImageGrayThresh.shape[:2], dtype="uint8") * 255
    
    # #calculate points to be masked based on provided ratio
    # maskVehicleBoxTopLeftXY = (0,0)
    
    # #calculate points to be masked based on provided ratio
    # maskVehicleBoxBottomRightXY = (int(imageWidth), 
    #     int(imageHeight/2))
    
    # maskVehicle = cv2.rectangle(maskWhite,maskVehicleBoxTopLeftXY,
    #     maskVehicleBoxBottomRightXY,color=0,thickness=-1)
    
    # #Mask out the area of the vehicle
    # passedImageGrayThreshMasked = cv2.bitwise_and(maskOurs, 
    #     maskOurs, mask=maskVehicle)
    cv2.imshow("passedImageGrayThresh", passedImageGrayThresh )
    #Find contours
    cnts, hierarchy = cv2.findContours(passedImageGrayThresh.copy(),
        cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    returnedImageDebug=passedImage

    # print(cnts)
    print(len(cnts))

    # count = 0 
#     for cnt in cnts :
  
# # cnt {cnts[count]}
#         print(f"contour {count} : length: {len(cnts[count])}    ")
#         count += 1 
    # Max number of found contours to process based on area of return, largest returned first
    maxCnt = 2
    print("done\n\n")
    if len (cnts) < maxCnt:
        maxCnt = len(cnts)
    cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0:maxCnt]


    count = 0 
    print(len(cnt))
    print(f"contour {0} : length: {len(cnt[0])}")
    print(f"contour {1} : length: {len(cnt[1])}")
    

    sortRightToLeft = True
    # Take largest contours and sort left to right
    if len (cnts) > 1:
        boundingBoxes = [cv2.boundingRect(c) for c in cnt]
        (cnt, boundingBoxes) = zip(*sorted(zip(cnt, boundingBoxes),
            key=lambda b:b[1][0], reverse= sortRightToLeft))

    # #Initialize and/or clear existing found line vector array
    pixyScaledVectorArray = np.empty([0,4], int)

    # #Used to determine what line is mapped in message from debug image
    lineNumber=0

    # #Loop through contours
    for cn in cnt:

        # if self.debug:
            #Paint all the areas found in the contour
        cv2.fillPoly(returnedImageDebug,pts=[cn],color=(0,0,255))
        
    #     #Find lines from contours using least square method/// draw a line approximating contour line
        [vectorX,vectorY,linePointX,linePointY] = cv2.fitLine(cn,cv2.DIST_L2,0,0.01,0.01)
        
        print("\n")
        print(vectorX, vectorY , linePointX ,linePointY , end=" ")
        if (linePointX >= 1.0) and (linePointY >= 1.0):
            
            #Easy avoid divide by zero
            if vectorY == 0:
                print("vectorY is zero")
                vectorY = 1e-4
            if vectorX == 0:
                print("vectorX is zero")
                vectorX = 1e-4

            #Calculate line points to see if they exceeds any bounds of the image, correct if they do
            topLeftX = int((-linePointY*vectorX/vectorY)+linePointX)
            bottomRightX = int(((imageHeight-linePointY)*vectorX/vectorY)+linePointX)
            topLeftY = 0
            bottomRightY = imageHeight
            lineMethodUsed = 0
            
            if (topLeftX <= 0) and (bottomRightX > imageWidth):
                lineMethodUsed = 1
                topLeftY = int(((-linePointX)*vectorY/vectorX)+linePointY)
                bottomRightY = int(((imageWidth-linePointX)*vectorY/vectorX)+linePointY)
                topLeftX = 0
                bottomRightX = imageWidth

            elif (topLeftX > imageWidth) and (bottomRightX < 0):
                lineMethodUsed = 2
                topLeftY = int(((imageWidth-linePointX)*vectorY/vectorX)+linePointY)
                bottomRightY = int(((-linePointX)*vectorY/vectorX)+linePointY)
                topLeftX = imageWidth
                bottomRightX = 0

            elif (topLeftX <= 0) and (bottomRightX < imageWidth):
                lineMethodUsed = 3
                topLeftY = int(((-linePointX)*vectorY/vectorX)+linePointY)
                bottomRightY = imageHeight
                topLeftX = 0
                bottomRightX = int(((imageHeight-linePointY)*vectorX/vectorY)+linePointX)

            elif (topLeftX > 0) and (bottomRightX > imageWidth):
                lineMethodUsed = 4
                topLeftY = 0
                bottomRightY = int(((imageWidth-linePointX)*vectorY/vectorX)+linePointY)
                topLeftX = int((-linePointY*vectorX/vectorY)+linePointX)
                bottomRightX = imageWidth

            elif (topLeftX > imageWidth) and (bottomRightX > 0):
                lineMethodUsed = 5
                topLeftY = imageHeight
                bottomRightY = int(((imageWidth-linePointX)*vectorY/vectorX)+linePointY)
                topLeftX = int(((imageHeight-linePointY)*vectorX/vectorY)+linePointX)
                bottomRightX = imageWidth

            elif (topLeftX < imageWidth) and (bottomRightX < 0):
                lineMethodUsed = 6
                topLeftY = int((-linePointX*vectorY/vectorX)+linePointY)
                bottomRightY = 0
                topLeftX = 0
                bottomRightX = int((linePointY)*(-vectorX/vectorY)+linePointX)
            
            
            #Extra safety
            if topLeftX < 0:
                topLeftX=0
            elif topLeftX > imageWidth:
                topLeftX=imageWidth
            if bottomRightX < 0:
                bottomRightX=0
            elif bottomRightX > imageWidth:
                bottomRightX=imageWidth
            if topLeftY < 0:
                topLeftY=0
            elif topLeftY > imageHeight:
                topLeftY=imageHeight
            if bottomRightY < 0:
                bottomRightY=0
            elif bottomRightY > imageHeight:
                bottomRightY=imageHeight

    #         #Add line method used to array count
            lineMethodsUsedCount = [0, 0, 0, 0, 0, 0, 0]

            lineMethodsUsedCount[lineMethodUsed]+=1

            pixyImageWidth = 320
            pixyImageHeight = 180


            #maybe not needed
    #         #Scale into Pixy camera units88888888888888888888
            topLeftXScaled = int(topLeftX*(pixyImageWidth/imageWidth))
            bottomRightXScaled = int(bottomRightX*(pixyImageWidth/imageWidth))
            topLeftYScaled = int(topLeftY*(pixyImageWidth/imageWidth))
            bottomRightYScaled = int(bottomRightY*(pixyImageWidth/imageWidth))

            # if self.lineFindPrintDebug:
            #     self.get_logger().info('\n\nlineMethodUsed:{:d},lineMethodsUsedCount:{:s}'.format(
            #         self.lineMethodUsed,str(self.lineMethodsUsedCount)))
            #     self.get_logger().info('vectorX:{:f},vectorY:{:f},linePointX:{:f},linePointY:{:f}'.format(
            #         float(vectorX),float(vectorY),float(linePointX),float(linePointY)))
            #     self.get_logger().info('topLeftX:{:d},topLeftY:{:d},bottomRightX:{:d},bottomRightY:{:d}'.format(
            #         topLeftX,topLeftY,bottomRightX,bottomRightY))
            #     returnedImageDebug = cv2.line(returnedImageDebug,(topLeftX,topLeftY),
            #         (bottomRightX,bottomRightY),(255,128,128),2)

    #         #Append found line points to pixy found line vector array
            pixyScaledVectorArray = np.append(pixyScaledVectorArray,
                np.array([[topLeftXScaled,topLeftYScaled,bottomRightXScaled,bottomRightYScaled]]),axis=0)
            #Increment line number
            lineNumber += 1
    
    # #Testing
    # if self.useBogusData:
    #     if self.sortRightToLeft:
    #         self.bogusDataTest=[[int((self.pixyImageWidth*0.8)+
    #             self.bogusOffsetNumber),0,
    #             int(self.pixyImageWidth*0.8),self.pixyImageHeight],
    #             [int((self.pixyImageWidth*0.2)-self.bogusOffsetNumber),0,
    #             int(self.pixyImageWidth*0.2),self.pixyImageHeight]]
    #     else:
    #         self.bogusDataTest=[[int((self.pixyImageWidth*0.2)+
    #             self.bogusOffsetNumber),0,
    #             int(self.pixyImageWidth*0.2),self.pixyImageHeight],
    #             [int((self.pixyImageWidth*0.8)-self.bogusOffsetNumber),0,
    #             int(self.pixyImageWidth*0.8),self.pixyImageHeight]]

    #     if self.switchVectorPoints:
    #         (self.pX0, self.pY0, self.pX1, self.pY1) = (2,3,0,1)
    #     else:
    #         (self.pX0, self.pY0, self.pX1, self.pY1) = (0,1,2,3)

    #     pixyScaledVectorArray = np.array(self.bogusDataTest)

    # if self.debug:
        #Border for vehicle mask
        # returnedImageDebug = cv2.rectangle(returnedImageDebug,maskVehicleBoxTopLeftXY,
        #     maskVehicleBoxBottomRightXY, color=(128,128,0),thickness=3)

        #Calcualte background for pixy image space
    debugPixyMessageTopLeftXY = (int((imageWidth/2)-(pixyImageWidth/2)),
        int((imageHeight/2)-(pixyImageHeight/2)))

    #Create background for pixy image space
    returnedImageDebug = cv2.rectangle(returnedImageDebug,debugPixyMessageTopLeftXY,
        ((debugPixyMessageTopLeftXY[0]+pixyImageWidth),
        (debugPixyMessageTopLeftXY[1]+pixyImageHeight)),(0,255,0),-1)
        
    # cv2.imshow('returnedImageDebug',returnedImageDebug)
    
    for lineNumber in range(len(pixyScaledVectorArray)):
        #Draw the found line in image space
        returnedImageDebug = cv2.line(returnedImageDebug,
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][0],
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][1]),
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][2],
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][3]),
            (0,0,0),1)

        # cv2.imshow('returnedImageDebugAfterLine', returnedImageDebug)
            
            #Draw box point for top left XY for Pixy space debug image
        returnedImageDebug = cv2.rectangle(returnedImageDebug,
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][0]-1, 
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][1]-1),
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][0]+1, 
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][1]+1),
            (0,0,255),-1)
            
        # cv2.imshow( 'rect-returnedImageDebug' , returnedImageDebug)
        #Draw box point for bottom right XY for Pixy space debug image
        returnedImageDebug = cv2.rectangle(returnedImageDebug,
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][2]-1,
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][3]-1),
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][2]+1, 
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][3]+1),
            (0,0,255),-1)
            
        # cv2.imshow( 'br-rect-returnedImageDebug', returnedImageDebug)
    #         #Write text for top left XY for Pixy space debug image
        returnedImageDebug = cv2.putText(
            returnedImageDebug, '{:d},{:d}'.format(
            pixyScaledVectorArray[lineNumber][0],pixyScaledVectorArray[lineNumber][1]), 
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][0]-20+(20*lineNumber), 
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][1]), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255,0,0), 1, cv2.LINE_AA)
            
    #         #Write text for bottom right XY for Pixy space debug image
        returnedImageDebug = cv2.putText(returnedImageDebug, '{:d},{:d}'.format(
            pixyScaledVectorArray[lineNumber][2],pixyScaledVectorArray[lineNumber][3]),
            (debugPixyMessageTopLeftXY[0]+pixyScaledVectorArray[lineNumber][2]-20+(20*lineNumber), 
            debugPixyMessageTopLeftXY[1]+pixyScaledVectorArray[lineNumber][3]), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255,0,0), 1, cv2.LINE_AA)

    #         #Write the line number for message
        returnedImageDebug = cv2.putText(returnedImageDebug, 'm{:d}'.format(
            lineNumber),
            (int((pixyScaledVectorArray[lineNumber][0]+
            pixyScaledVectorArray[lineNumber][2])/2.0+
            debugPixyMessageTopLeftXY[0]-20+(20*lineNumber)),
            int((pixyScaledVectorArray[lineNumber][1]+
            pixyScaledVectorArray[lineNumber][3])/2.0+
            debugPixyMessageTopLeftXY[1])), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,255), 1, cv2.LINE_AA)


    cv2.imshow( 'final-img', returnedImageDebug)
    # #Pixy message for publication
    if (len(pixyScaledVectorArray) == 0):
        
        m0_x0 = 0
        m0_y0 = 0
        m0_x1 = 0
        m0_y1 = 0
        m1_x0 = 0
        m1_y0 = 0
        m1_x1 = 0
        m1_y1 = 0
        
    if (len(pixyScaledVectorArray) > 0):
        m0_x0 = int(pixyScaledVectorArray[0][pX0])
        m0_y0 = int(pixyScaledVectorArray[0][pY0])
        m0_x1 = int(pixyScaledVectorArray[0][pX1])
        m0_y1 = int(pixyScaledVectorArray[0][pY1])
        m1_x0 = 0
        m1_y0 = 0
        m1_x1 = 0
        m1_y1 = 0                                           #publishSecondVector is true so neglect it
        if (len(pixyScaledVectorArray) > 1)  :  #publishSecondVector
            m1_x0 = int(pixyScaledVectorArray[1][pX0])
            m1_y0 = int(pixyScaledVectorArray[1][pY0])
            m1_x1 = int(pixyScaledVectorArray[1][pX1])
            m1_y1 = int(pixyScaledVectorArray[1][pY1])

    cv2.imshow('finally', returnedImageDebug)
    return(returnedImageDebug)




while (1):

    # _, frame = vid.read()
    print("inside while")
    findLines(img2)

# Exiting the window if 'q' is pressed on the keyboard.
if cv2.waitKey(0) & 0xFF == ord('q'): 
    cv2.destroyAllWindows()