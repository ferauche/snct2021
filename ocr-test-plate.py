import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import re

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(1.2)

camera.capture(rawCapture, format="bgr")
image = cv2.cvtColor(rawCapture.array, cv2.COLOR_BGR2GRAY) 

print("Lendo...")
opt = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
opt += " --oem 3 --psm 6"

text = pytesseract.image_to_string(image, config = opt)
print(text)
print(re.sub(r'[^a-zA-Z0-9]','',text))
