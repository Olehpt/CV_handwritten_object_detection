import cv2 as cv
import numpy as np
import os

img_path = os.path.join('..', 'data/test.png')
img = cv.imread(img_path)

#post processing

img_post = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_post = cv.Canny(img_post, 75, 100)

h_result = cv.HoughLinesP(img_post, 1, np.pi/180, 30, maxLineGap = 10)

h_lines = h_result.tolist()

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

lines = []
marker_size = 5
min_length = 20
min_angle = 15
min_distance = 20

for line in h_lines:
    x1, y1, x2, y2 = line[0]
    #ignoring micro-lines
    if is_close(x1, y1, x2, y2, min_length):
        print(f'line {x1}, {y1}, {x2}, {y2} destroyed')
        continue
    bool1 = True
    for other in h_lines:
        x3, y3, x4, y4 = other[0]
        if x1 == x3 and x2 == x4 and y1 == y3 and y2 == y4:
            continue
        #setting values: angles, centers, distance between
        dx1 = x2-x1
        dy1 = y2-y1
        angle1 = np.arctan2(dy1, dx1)
        angle1 = angle1 % np.pi
        dx2 = x4-x3
        dy2 = y4-y3
        angle2 = np.arctan2(dy2, dx2)
        angle2 = angle2 % np.pi
        center1 = ((x1+x2)/2, (y1+y2)/2)
        center2 = ((x3+x4)/2, (y3+y4)/2)
        dist = np.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)
        #filtering
        bool_angle = (angle1 - angle2) < min_angle
        bool_distance = dist < min_distance
        if bool_angle and bool_distance:
            bool1 = False
    if bool1:
        lines.append((x1, y1, x2, y2))

img_copy = img.copy()

for line in h_lines:
    x1, y1, x2, y2 = line[0]
    draw_dot_bounds(img, x1, y1, marker_size)
    draw_dot_bounds(img, x2, y2, marker_size)

for line in lines:
    x1, y1, x2, y2 = line
    draw_dot_bounds(img_copy, x1, y1, marker_size)
    draw_dot_bounds(img_copy, x2, y2, marker_size)

cv.imshow('copy', img_copy)
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()