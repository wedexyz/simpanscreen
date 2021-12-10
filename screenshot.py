import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time

#Take resolution from system automatically
w = GetSystemMetrics(0)
h =  GetSystemMetrics(1)
SCREEN_SIZE = (w,h)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("recording.mp4", fourcc, 20.0, (SCREEN_SIZE))
tim = time.time()
tp = int(input('How many times you want to record screen?->(Define value in Seconds): '))
tp = tp+tp
f = tim+tp
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    tu = time.time()
    if tu>f:
        break
cv2.destroyAllWindows()
out.release()