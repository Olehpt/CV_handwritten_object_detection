import draw, contourDetection
import numpy as np
import cv2
from geometry import Point
import math

img = cv2.imread("../data/test2.png")
points = contourDetection.contour_detection(img)
vox_resolution = 128

#cropping
centroid = Point(0,0)
for point in points:
    centroid.x += point[0]
    centroid.y += point[1]
centroid.x = centroid.x // len(points)
centroid.y = centroid.y // len(points)
print(centroid)
draw.draw_dot_bounds(img, centroid, 5, (0,255,0))

p1 = Point(centroid.x, centroid.y)#left
p2 = Point(centroid.x, centroid.y)#top
p3 = Point(centroid.x, centroid.y)#righd
p4 = Point(centroid.x, centroid.y)#bottom
for point in points:
        x, y = point
        draw.draw_dot_bounds(img, Point(x, y), 5, (255,0,0))
        if x < p1.x: p1 = Point(x,y)
        if y < p2.y: p2 = Point(x,y)
        if x > p3.x: p3 = Point(x,y)
        if y > p4.y: p4 = Point(x,y)

offset = 25
p_low = Point(p1.x - offset, p4.y + offset)
p_high = Point(p3.x + offset, p2.y - offset)

cropped = img[p_high.y:p_low.y, p_low.x:p_high.x]

draw.draw_dot_bounds(img, p_low, 5, (0,255,0))
draw.draw_dot_bounds(img, p_high, 5, (0,255,0))

cv2.imshow("img", cropped)
cv2.waitKey(0)

