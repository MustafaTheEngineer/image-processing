import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('../cat.jpg')

# Convert the image to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Function to add salt and pepper noise
def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    
    # Salt noise
    salt = np.random.rand(*image.shape[:2])
    noisy_image[salt < salt_prob] = [255, 255, 255]  # White
    
    # Pepper noise
    pepper = np.random.rand(*image.shape[:2])
    noisy_image[pepper < pepper_prob] = [0, 0, 0]  # Black
    
    return noisy_image

# Add salt and pepper noise to the image
salt_prob = 0.01  # Adjust the probability based on the desired noise level
pepper_prob = 0.01
noisy_image = salt_and_pepper_noise(image_rgb, salt_prob, pepper_prob)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title('Image with Salt and Pepper Noise')

plt.show()
