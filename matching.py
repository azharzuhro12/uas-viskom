import cv2
import matplotlib.pyplot as plt

img1_color = cv2.imread("dataset/original.jpg")
img2_color = cv2.imread("dataset/dark.jpg")

img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append(m)

sift_match = cv2.drawMatches(img1_color,kp1,img2_color,kp2,good,None,flags=2)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches, key=lambda x:x.distance)

orb_match = cv2.drawMatches(img1_color,kp1,img2_color,kp2,matches[:50],None,flags=2)

plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.title("SIFT Matching")
plt.imshow(cv2.cvtColor(sift_match, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2,1,2)
plt.title("ORB Matching")
plt.imshow(cv2.cvtColor(orb_match, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
