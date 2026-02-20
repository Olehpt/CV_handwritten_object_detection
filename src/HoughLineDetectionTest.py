import cv2 as cv
import numpy as np
import os

img_path = os.path.join('..', 'data/test.png')
img = cv.imread(img_path)

#post processing

img_post = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_post = cv.Canny(img_post, 75, 100)

lines = cv.HoughLinesP(img_post, 1, np.pi/180, 30, maxLineGap = 10)
bound = 20

def is_close(x1, y1, x2, y2, margin):
    dist = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist < margin

def is_same_lines(line1, line2, margin):
    dot1 = is_close(line1[0], line1[1], line2[0], line2[1], margin)
    dot2 = is_close(line1[2], line1[3], line2[0], line2[1], margin)

def draw_bounds(img, x1, y1, x2, y2):
    cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

def draw_dot_bounds(img, x1, y1, margin):
    cv.rectangle(img, (x1 - margin, y1 + margin), (x1 + margin, y1 - margin), (0, 0, 255), 1)

print(lines[0])

draw_bounds(img, lines[0][0][0], lines[0][0][1], lines[0][0][2], lines[0][0][3])
draw_dot_bounds(img, lines[0][0][0], lines[0][0][1], bound)
draw_dot_bounds(img, lines[0][0][2], lines[0][0][3], bound)

cv.imshow('test', img)
cv.imshow('img_post', img_post)
cv.waitKey(0)
cv.destroyAllWindows()