import cv2 as cv
import numpy as np
import os

import draw
from geometry import Line, Point

def distance(point1, point2):
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def is_close(point1, point2, tolerance):
    return distance(point1, point2) < tolerance

img_path = os.path.join('..', 'data/test2.png')
img = cv.imread(img_path)

img_post = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_post = cv.Canny(img_post, 75, 100)

h_result = cv.HoughLinesP(img_post, 1, np.pi/180, 30, maxLineGap = 10)

lines = []


for h_line in h_result:
    x1, y1, x2, y2 = h_line[0]
    line = Line(Point(x1, y1), Point(x2, y2))
    lines.append(line)
    #draw.draw_dot_bounds(img, line.A, 5, (255, 0, 0))
    #draw.draw_dot_bounds(img, line.B, 5, (0, 0, 255))

tolerance_param = 20

for line in lines:
    for other in lines:
        if line == other:
            continue
        if is_close(line.A, other.A, tolerance_param) and is_close(line.B, other.B, tolerance_param):
            pass



cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()