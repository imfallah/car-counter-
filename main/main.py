#importing=============================================================================
import cv2
import numpy as np

#cap run==============================================================================
cap = cv2.VideoCapture('C:/ordibehesht-pro/week-4\car counter/main/video.mp4')

#variables============================================================================
min_width_rect = 80
min_height_rect = 80
counter_line_postion = 550

algo = cv2.createBackgroundSubtractorMOG2()

#function===========================================================================
def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


detect = []
offset = 6
counter = 0


# cap starting webcam ===================================================================
while True:
    ret, frame1 = cap.read()
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    countershape, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, counter_line_postion), (1200, counter_line_postion), (255, 127, 0), 3)
    
    for (i, c) in enumerate(countershape):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_rect) and (h >= min_height_rect)
        
        if not validate_counter:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)
        
        for (x, y) in detect:
            if y < (counter_line_postion + offset) and y > (counter_line_postion - offset):
                counter += 1
            cv2.line(frame1, (25, counter_line_postion), (1200, counter_line_postion), (0, 127, 255), 3)
            detect.remove((x, y))
            print("Car Counter:" + str(counter))

#===============================================================================================
    cv2.putText(frame1, "COUNTER:" + str(counter), (500, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    #cv2.imshow('Detector', dilatada)
    cv2.imshow('video orginal', frame1)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

#==============================================================================================
cv2.destroyAllWindows()
cap.release()
