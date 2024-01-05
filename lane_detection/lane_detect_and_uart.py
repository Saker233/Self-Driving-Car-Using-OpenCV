import cv2
import numpy as np
import serial
import time

# Initialize serial communication
ser = serial.Serial('/dev/ttyS0', 9600)  


def map_angle(angle):

    return np.interp(angle, [-90, 90], [-100, 100])



video = cv2.VideoCapture(0)

while True:
    ret, orig_frame = video.read()

    
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_white = np.array([0, 0, 75])
    upper_white = np.array([255, 0, 255])
    mask = cv2.inRange(hsv, low_white, upper_white)
    edges = cv2.Canny(mask, 75, 150)

    
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    if lines is not None:
        
        slope = np.mean([(y2 - y1) / (x2 - x1) for line in lines for x1, y1, x2, y2 in line])

        
        steering_angle = np.arctan(slope) * (180 / np.pi)

        
        mapped_angle = map_angle(steering_angle)

        
        ser.write(f'{mapped_angle}\n'.encode())

    
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    cv2.imshow("mask", mask)

    
    key = cv2.waitKey(1)
    if key == 27:
        break


video.release()
ser.close()
cv2.destroyAllWindows()
