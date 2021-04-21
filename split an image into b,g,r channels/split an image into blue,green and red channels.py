import numpy as np
import cv2
img=cv2.imread('garden.jpg')
b=img[:,:,0]
print(b)
g=img[:,:,1]
r=img[:,:,2]
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
