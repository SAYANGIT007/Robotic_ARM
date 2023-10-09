
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject(digits=3, portNo="COM5")  # max 3 digits per data sent.
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
final = []
l = 0  # left hand
r = 1  # right hand
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]  # List of 21 Landmarks points
        handType = hand["type"]  # left or right hand
        fingers = detector.fingersUp(hand)  # finger detector.variable is a list
        #print(handType)

        if fingers == [1, 1, 0, 0, 0]:
            length, info, img = detector.findDistance(lmList[4], lmList[8], img)  # with draw
            length = int(length)  # distance between two fingers

            if handType == "Left":    # base servo
                pulse = int(np.interp(length, [30, 250], [95, 610]))  # converting the range to servo range
                final = [l, 8, pulse]
                print(final)  # [left,handPoint,pulseValue]
                arduino.sendData(final)

            if handType == "Right":  # claw
                pulse = int(np.interp(length, [30, 250], [105, 280]))  # converting the range to servo range
                final = [r, 8, pulse]
                print(final)  # [right,handPoint,pulseValue]
                arduino.sendData(final)

        if fingers == [1, 1, 1, 0, 0]:
            length, info, img = detector.findDistance(lmList[4], lmList[12], img)  # with draw
            length = int(length)  # distance between two fingers

            if handType == "Left":  # left servo
                pulse = int(np.interp(length, [30, 250], [95, 210]))  # converting the range to servo range
                final = [l, 12, pulse]
                print(final)  # [left,handPoint,pulseValue]
                arduino.sendData(final)

            if handType == "Right":  # right servo
                pulse = int(np.interp(length, [30, 250], [220, 580]))  # converting the range to servo range
                final = [r, 12, pulse]
                print(final)  # [left,handPoint,pulseValue]
                arduino.sendData(final)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
