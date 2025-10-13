import cv2
import numpy as np
import os
import HandTrackingModule as htm

#######################
brushThickness = 25
eraserThickness = 100
########################

folderPath = "Header"   # must contain 5 images
myList = os.listdir(folderPath)
# print(myList)

overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)

print(len(overlayList))
header = overlayList[0]
drawColor = (0, 0, 255)   # default red

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()

        # 4. If Selection Mode – Two fingers up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")

            # Checking for the click in header area
            if y1 < 125:
                slot_width = 1280 // 5  # 256 px
                slot = x1 // slot_width

                header = overlayList[slot]

                if slot == 0:
                    drawColor = (0, 0, 255)   # Red
                elif slot == 1:
                    drawColor = (147, 20, 255)   # Pink (BGR approx)
                elif slot == 2:
                    drawColor = (255, 0, 0)   # Blue
                elif slot == 3:
                    drawColor = (0, 255, 0)   # Green
                elif slot == 4:
                    drawColor = (0, 0, 0)     # Eraser

            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing Mode – Index finger up
        if fingers[1] and fingers[2] == 0:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1

    # Merge canvas and webcam image
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Setting the header image
    img[0:125, 0:1280] = header

    # Display
    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imgCanvas)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
