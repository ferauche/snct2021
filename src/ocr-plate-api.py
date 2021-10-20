import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import re
import requests

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(1.2)

camera.capture(rawCapture, format="bgr")
image = cv2.cvtColor(rawCapture.array, cv2.COLOR_BGR2GRAY) 

print("Lendo...")
opt = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
opt += " --oem 3 --psm 6"

text = pytesseract.image_to_string(image, config = opt)
text = re.sub(r'[^a-zA-Z0-9]','',text)
print(text)

print("Enviando a planilha do GoogleSheets...")

url = "https://docs.google.com/forms/d/e/1FAIpQLSd0aT6g3_SIG797M9B2JKKYdSK-MZ3pXu-K1iGNBvjW5Yal9g/formResponse"

submission = {"entry.1123972501": text}

sent = requests.post(url, data=submission)

if sent:
	print("Enviado com sucesso!")
else:
	print("Ocorreu um erro")

