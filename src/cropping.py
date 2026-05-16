from contourDetection import contour_detection
import cv2
from geometry import Point

def crop(img, offset = 5, points = None):
    if points is None: points = contour_detection(img)

    x0, y0 = points[0]

    p1 = Point(x0, y0)  # left
    p2 = Point(x0, y0)  # top
    p3 = Point(x0, y0)  # right
    p4 = Point(x0, y0)  # bottom
    for point in points:
        x, y = point
        if x < p1.x: p1 = Point(x, y)
        if y < p2.y: p2 = Point(x, y)
        if x > p3.x: p3 = Point(x, y)
        if y > p4.y: p4 = Point(x, y)

    p_low = Point(p1.x, p4.y)
    p_high = Point(p3.x, p2.y)

    cropped = img[p_high.y:p_low.y, p_low.x:p_high.x]

    cropped = cv2.copyMakeBorder(
        cropped,
        top=offset,
        bottom=offset,
        left=offset,
        right=offset,
        borderType=cv2.BORDER_CONSTANT,
        value=(255, 255, 255)
    )

    return cropped

if __name__ == "__main__":
    img = cv2.imread("../data/test3.png")
    print(img.shape)
    cropped = crop(img)
    cv2.imshow("test", cropped)
    cv2.waitKey(0)
