import cv2
import numpy as np

img1 = cv2.imread("car.jpg",0)

gamma = 2
img2 = np.power(img1,gamma)

gamma = 3
img3 = np.power(img1,gamma)

gamma = 4
img4 = np.power(img1,gamma)

cv2.imshow("input input",img1)
cv2.imshow("gamma 2",img2)
cv2.imshow("gamma 3",img3)
cv2.imshow("gamma 4",img4)

cv2.waitKey(1000000)
cv2.destroyAllWindows()