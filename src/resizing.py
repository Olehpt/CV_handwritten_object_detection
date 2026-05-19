import cv2

def resize(img, resolution = 128):
    h,w = img.shape[:2]
    max_side = max(h, w)
    scale_coef = max_side / resolution

    new_w = int(w // scale_coef)
    new_h = int(h // scale_coef)
    resized = cv2.resize(img, (new_w, new_h))

    fill_w = (resolution - new_w) // 2
    fill_h = (resolution - new_h) // 2

    resized = cv2.copyMakeBorder(resized, top=fill_h, bottom=fill_h, left=fill_w, right=fill_w,
                                 borderType=cv2.BORDER_CONSTANT, value=(255, 255, 255))
    resized = cv2.resize(resized, (resolution, resolution))
    return resized