import cv2
import numpy as np

# Read the image
image = cv2.imread("../cat.jpg")

# Calculate the Laplacian of the image
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Normalize the Laplacian values between 0 and 255 for visualization
laplacian = cv2.normalize(laplacian, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
laplacian = laplacian.astype(np.uint8)

# Apply a Gaussian blur (adjust kernel size as desired)
blurred_laplacian = cv2.GaussianBlur(laplacian, (5, 5), 0)

# Add a weighted contribution of the blurred Laplacian to the original image
blended_image = cv2.addWeighted(image, 0.5, blurred_laplacian, 0.5, 0)

# Show the original image, Laplacian output, and blended image
cv2.imshow("Original Image", image)
cv2.imshow("Laplacian Edges", laplacian)
cv2.imshow("Blurred Laplace + Original", blended_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



