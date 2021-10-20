import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.8)

camera.capture(rawCapture, format="bgr")
image = cv2.cvtColor(rawCapture.array, cv2.COLOR_BGR2GRAY) 

print("Lendo...")

text = pytesseract.image_to_string(image)
print(text)
