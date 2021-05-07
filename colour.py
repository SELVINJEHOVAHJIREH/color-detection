import cv2
import serial
import numpy as np
port = serial.Serial('/dev/ttyUSB1',9600)
vid = cv2.VideoCapture(0) 

while True: 

	# capturing the current frame 
	_, frame = vid.read() 

	# displaying the current frame 
	cv2.imshow("frame", frame) 

	# setting values for base colors 
	b = frame[:, :, :1] 
	g = frame[:, :, 1:2] 
	r = frame[:, :, 2:] 

	# computing the mean 
	b_mean = np.mean(b) 
	g_mean = np.mean(g) 
	r_mean = np.mean(r)

		# displaying the most prominent color 
	if (b_mean > g_mean and b_mean > r_mean): 
		print("Blue")
		data = 2
	if (g_mean > r_mean and g_mean > b_mean): 
		print("Green")
		data = 1
		port.write(str.encode('1'))
	if (r_mean > g_mean and r_mean >  b_mean): 
		print("Red")
		data = 0
		port.write(str.encode('0'))
		
while( port.isOpen()):

    if(data == 1):
        port.write(str.encode('1'))
    elif(data == 0):
        port.write(str.encode('0'))
    else:
        print('Invalid input!!!!')