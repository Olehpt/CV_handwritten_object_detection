import numpy as np, cv2
from contourDetection import contour_detection
from cropping import crop

img = cv2.imread('../data/test2.png')
cropped = crop(img)

voxel_resolution = 128

#resizing

h,w = cropped.shape[:2]

max_side = max(h,w)
scale_coef = max_side / voxel_resolution

new_w = int(w//scale_coef)
new_h = int(h//scale_coef)
resized = cv2.resize(cropped, (new_w, new_h))

fill_w = (voxel_resolution - new_w)//2
fill_h = (voxel_resolution - new_h)//2

resized = cv2.copyMakeBorder(resized, top = fill_h, bottom = fill_h, left = fill_w, right = fill_w, borderType = cv2.BORDER_CONSTANT, value = (255, 255, 255))
resized = cv2.resize(resized, (voxel_resolution, voxel_resolution))
