import draw, geometry, contourDetection
import numpy as np
import cv2

img = cv2.imread("../data/test3.png")
points = contourDetection.contour_detection(img)

for point in points:
    draw.draw_dot_bounds(img, geometry.Point(point[0], point[1]), 5, (0, 255, 0))

grid_size = 128
voxel_grid = np.zeros((grid_size, grid_size, grid_size), dtype = bool)