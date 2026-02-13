import os, cv2

#print("Current working directory:", os.getcwd())

img_path = os.path.join('..', 'data/test.png')
img = cv2.imread(img_path)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()