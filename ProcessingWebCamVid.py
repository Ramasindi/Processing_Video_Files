import numpy as np 
from cv2 import cv2 
  
# This will return video from the first webcam on the computer. 
cap = cv2.VideoCapture(0)   

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('CamREC.avi', fourcc, 20.0, (640, 480)) 
  

while(True): 

    ret, frame = cap.read()  

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      
    # output the frame 
    out.write(frame)  
      
    # The original input frame is shown in the window  
    cv2.imshow('Original', frame) 
  
    # The window showing the operated video stream  
    cv2.imshow('frame', hsv) 
  
      
    # Wait for 'a' key to stop the program  
    if cv2.waitKey(1) & 0xFF == ord('a'): 
        break
  
# Close the window / Release webcam 
cap.release() 

out.release()  

cv2.destroyAllWindows() 