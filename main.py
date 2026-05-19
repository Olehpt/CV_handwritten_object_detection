import cv2, numpy as np
from src.contourDetection import contour_detection
from src.cropping import crop
from src.resizing import resize

file_paths = ['data/test1.png', 'data/test2.png', 'data/test3.png']

imgs = []
for path in file_paths:
    img = cv2.imread(path)
    if img is not None:
        imgs.append(img)
        print(f"Image {path} added")

contours = []
for img in imgs:
    contour = contour_detection(img)
    if not contour.size == 0: contours.append(contour)
    else : print(f'Empty contour from {img.path}')

cropped=[]
for i, img in enumerate(imgs):
    contour = contours[i]
    cropped_img = crop(img, points = contour)
    cropped.append(cropped_img)

resized=[]
for i, cropped_img in enumerate(cropped):
    resized_img = resize(cropped_img)
    resized.append(resized_img)

cv2.imshow('img1', resized[0])
cv2.imshow('img2', resized[1])
cv2.imshow('img3', resized[2])
print(resized[0].shape, resized[1].shape, resized[2].shape)
cv2.waitKey(0)