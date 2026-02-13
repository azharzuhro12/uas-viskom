import cv2
import numpy as np
import os

os.makedirs("dataset", exist_ok=True)

img = cv2.imread("azhar.jpeg")
if img is None:
    print("Gambar input.jpg tidak ditemukan!")
    exit()

h, w = img.shape[:2]

M = cv2.getRotationMatrix2D((w/2,h/2),45,1)
rotated = cv2.warpAffine(img,M,(w,h))

scaled = cv2.resize(img,None,fx=0.6,fy=0.6)

blur = cv2.GaussianBlur(img,(11,11),0)

dark = (img * 0.4).astype(np.uint8)

pts1 = np.float32([[0,0],[w,0],[0,h],[w,h]])
pts2 = np.float32([[20,30],[w-20,0],[0,h],[w,h-50]])
M = cv2.getPerspectiveTransform(pts1,pts2)
persp = cv2.warpPerspective(img,M,(w,h))

cv2.imwrite("dataset/original.jpg",img)
cv2.imwrite("dataset/rotate.jpg",rotated)
cv2.imwrite("dataset/scale.jpg",scaled)
cv2.imwrite("dataset/blur.jpg",blur)
cv2.imwrite("dataset/dark.jpg",dark)
cv2.imwrite("dataset/perspective.jpg",persp)

print("Dataset berhasil dibuat!")
