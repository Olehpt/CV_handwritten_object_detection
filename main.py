import cv2 as cv, os, numpy as np
from src.contourDetection import contour_detection

file_paths = ['data/test1.png', 'file2', 'file3']

imgs = []
for path in file_paths:
    img = cv.imread(path)
    if img is not None:
        imgs.append(img)
        print(f"Image {path} added")

contours = []
for img in imgs:
    contour = contour_detection(img)
    if not contour.empty(): contours.append(contour)
    else : print(f'Empty contour from {img.path}')
