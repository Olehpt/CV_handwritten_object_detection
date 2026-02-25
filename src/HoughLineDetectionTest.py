import cv2 as cv
import numpy as np
import os

import draw
import geometry as g

img_path = os.path.join('..', 'data/test2.png')
img = cv.imread(img_path)

img_post = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_post = cv.Canny(img_post, 75, 100)

h_result = cv.HoughLinesP(img_post, 1, np.pi/180, 30, maxLineGap = 10)

for line in h_result:
    x1, y1, x2, y2 = line[0]
    point1 = g.Point(x1, y1)
    point2 = g.Point(x2, y2)
    draw.draw_dot_bounds(img, point1, 5, (0, 255, 0))

cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()