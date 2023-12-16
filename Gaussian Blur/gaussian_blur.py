import cv2

# Read the image
image = cv2.imread("../cat.jpg")

# Define the Gaussian kernel size and standard deviation (e.g., (5, 5), 1.0)
kernel_size = (17,17)
sigma_x = 1.0

# Apply Gaussian blur using cv2.GaussianBlur()
blurred_image = cv2.GaussianBlur(image, kernel_size, sigma_x)

# Show the original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
