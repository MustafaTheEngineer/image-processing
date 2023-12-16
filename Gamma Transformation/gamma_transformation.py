import cv2

# Read the image
image = cv2.imread("../cat.jpg")

# Define the gamma value (e.g., 1.0 for linear, 2.2 for typical display, 0.5 for darker)
gamma = 3

# Apply gamma correction using pow()
corrected_image = cv2.pow(image / 255.0, gamma) * 255.0

# Show the original and corrected images
cv2.imshow("Original Image", image)
cv2.imshow("Gamma Corrected Image", corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
