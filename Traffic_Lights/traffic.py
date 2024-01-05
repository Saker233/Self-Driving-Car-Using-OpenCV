import cv2
import numpy as np

def detect_traffic_lights(camera_index=0):
   
    cap = cv2.VideoCapture(camera_index)
    
    while True:
     
        ret, frame = cap.read()
        
       
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        
       
        mask = cv2.inRange(hsv, lower_red, upper_red)
        
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
       
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print("Traffic Light detetced")
       
        cv2.imshow('Traffic Lights Detection', frame)
        
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    cap.release()
    cv2.destroyAllWindows()


detect_traffic_lights()
