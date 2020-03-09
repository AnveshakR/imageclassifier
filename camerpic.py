import cv2
import os
import calendar;
import time;
ts = calendar.timegm(time.gmtime())
camera = cv2.VideoCapture(0)
path = r'C:\Users\anves\OneDrive\Pictures\Saved Pictures'
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite(os.path.join(path , str(ts)+'.jpg'), image)
        break
camera.release()
cv2.destroyAllWindows()
