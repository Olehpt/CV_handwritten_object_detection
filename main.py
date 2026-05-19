import cv2, numpy as np
from src.contourDetection import contour_detection
from src.cropping import crop
from src.resizing import resize

from skimage.measure import marching_cubes
import trimesh

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

voxel_resolution = 128

resized=[]
for i, cropped_img in enumerate(cropped):
    resized_img = resize(cropped_img, voxel_resolution)
    resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    resized.append(resized_img)

voxels = np.zeros((voxel_resolution, voxel_resolution, voxel_resolution), dtype=bool)

for x in range(voxel_resolution):
    for y in range(voxel_resolution):
        for z in range(voxel_resolution):
            if (
                resized[0][y, x] == 0 and #front
                resized[1][y, z] == 0 and #side
                resized[2][z, x] == 0 #top
            ):
                voxels[x, y, z] = 1

#voxels to mesh?

verts, faces, normals, values = marching_cubes(
    voxels.astype(np.float32),
    level=0.5
)

mesh = trimesh.Trimesh(
    vertices=verts,
    faces=faces
)

mesh.export("result.obj")
