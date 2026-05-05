import cv2 as cv

def draw_dot_bounds(target_img, point, size, color):
    cv.rectangle(target_img, (point.x - size, point.y - size), (point.x + size, point.y + size), color)

def draw_line(target_img, point1, point2, thickness, color):
    cv.line(target_img, (point1.x, point1.y), (point2.x, point2.y), color = color, thickness = thickness)