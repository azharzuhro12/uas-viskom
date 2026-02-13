import cv2
import matplotlib.pyplot as plt

img = cv2.imread("dataset/original.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
sift_img = cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

orb = cv2.ORB_create(nfeatures=1500)
kp2, des2 = orb.detectAndCompute(gray,None)
orb_img = cv2.drawKeypoints(img,kp2,None,color=(0,255,0))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("SIFT Keypoints")
plt.imshow(cv2.cvtColor(sift_img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("ORB Keypoints")
plt.imshow(cv2.cvtColor(orb_img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
