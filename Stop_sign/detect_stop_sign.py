import cv2


ss = cv2.CascadeClassifier('stop_sign.xml')

cap = cv2.VideoCapture(0)  


cap.set(4, 640)  
cap.set(3, 480)

k = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Screen", img)
    SS = ss.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,x) in SS:
        print("Stop Sign Detected", k)
        k+=1
        
    
    
    key = cv2.waitKey(30)
    
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
