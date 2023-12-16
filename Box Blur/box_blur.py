import cv2

# Read the image
image = cv2.imread("../cat.jpg")

# Define the blur kernel size (e.g., 3 for 3x3 box blur)
kernel_size_3 = 3
kernel_size_4 = 4

# Apply box blur using cv2.blur()
blurred_image_3 = cv2.blur(image, (kernel_size_3, kernel_size_3))
blurred_image_4 = cv2.blur(image, (kernel_size_4, kernel_size_4))

# Show the original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image 3", blurred_image_3)
cv2.imshow("Blurred Image 4", blurred_image_4)
cv2.waitKey(0)
cv2.destroyAllWindows()
