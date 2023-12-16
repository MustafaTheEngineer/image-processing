import cv2
import numpy as np
import matplotlib.pyplot as plt

def color_slice(image, lower_bound, upper_bound):
    lower_bound = np.array(lower_bound, dtype=np.uint8)
    upper_bound = np.array(upper_bound, dtype=np.uint8)

    mask = cv2.inRange(image, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)

    return result

# Load the image
image = cv2.imread('../car.jpg')

# Convert the image to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the color range for slicing (adjust these values based on your needs)
lower_bound = [39, 10, 4]  # Lower bound for green (adjust as needed)
upper_bound = [242, 99, 41]  # Upper bound for green (adjust as needed)

# Apply color slicing
sliced_image = color_slice(image_rgb, lower_bound, upper_bound)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(sliced_image)
plt.title('Color Sliced Image')

plt.show()
