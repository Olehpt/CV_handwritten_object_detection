import cv2 as cv

def draw_dot_bounds(target_img, point, size, color):
    cv.rectangle(target_img, (point.x - size, point.y - size), (point.x + size, point.y + size), color)