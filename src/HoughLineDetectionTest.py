import cv2 as cv
import numpy as np
import os

img_path = os.path.join('..', 'data/test.png')
img = cv.imread(img_path)

#post processing

img_post = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_post = cv.Canny(img_post, 75, 100)

lines = cv.HoughLinesP(img_post, 1, np.pi/180, 30, maxLineGap = 10)

print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow('test', img)
cv.imshow('img_post', img_post)
cv.waitKey(0)
cv.destroyAllWindows()