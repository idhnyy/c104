import cv2
import numpy as np

screen = np.zeros([600,600])
#pixel = screen[:,2:3]
#print(pixel)
screen[200:400, 200:400] = 255
cv2.imshow("Tela",screen)
print(screen)
cv2.waitKey(0)