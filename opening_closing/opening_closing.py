import cv2
import numpy as np

# Load the image
image = cv2.imread('../cat.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element for morphology operations
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Perform opening (erosion followed by dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Perform closing (dilation followed by erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)  # Wait until a key is pressed

# Display the opening result
cv2.imshow('Opening Result', opening)
cv2.waitKey(0)  # Wait until a key is pressed

# Display the closing result
cv2.imshow('Closing Result', closing)
cv2.waitKey(0)  # Wait until a key is pressed

# Close all windows
cv2.destroyAllWindows()
