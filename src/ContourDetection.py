import cv2
import draw
import geometry
import os

img_path = os.path.join('..', 'data/test3.png')
img = cv2.imread(img_path, 0)

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

contour = max(contours, key=cv2.contourArea)

epsilon = 2.0
approx = cv2.approxPolyDP(contour, epsilon, True)

points = approx.reshape(-1, 2)

for(x,y) in points:
    draw.draw_dot_bounds(img, geometry.Point(x,y), 3, (150, 0, 0))

cv2.imshow('img', img)
cv2.waitKey(0)