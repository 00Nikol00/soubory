import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/VSPS_logo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()