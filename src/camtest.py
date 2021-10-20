from picamera import PiCamera
from time import sleep

if __name__ == '__main__':
	camera = PiCamera()
	camera.start_preview(alpha=192)
	sleep(1)
	camera.capture("/home/pi/camtest.jpg")
	camera.stop_preview()
