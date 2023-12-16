import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
gray_image = cv2.imread('../cat.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur for smoothing
kernel_size = (5, 5)  # Adjust the kernel size as needed
blurred_image = cv2.GaussianBlur(gray_image, kernel_size, 0)

# Apply Laplacian filter for sharpening
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

# Convert laplacian to the same data type as gray_image
laplacian = np.uint8(np.abs(laplacian))

# Combine the original and sharpened images
sharpened_image = cv2.addWeighted(gray_image, 1.5, laplacian, -0.5, 0)

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')

plt.subplot(1, 3, 2)
plt.imshow(blurred_image, cmap='gray')
plt.title('Smoothed Grayscale Image')

plt.subplot(1, 3, 3)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Grayscale Image')

plt.show()
