import cv2
import numpy as np
from datetime import datetime

camera = cv2.VideoCapture(0)
i = 0
while i < 5:
    raw_input('Press Enter to capture the image: ')
    return_value, image = camera.read()
    cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss') + '.jpg', image)
    i=i+1
del(camera)
