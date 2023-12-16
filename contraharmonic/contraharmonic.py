import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image, window_size, Q):
    padded_image = cv2.copyMakeBorder(image, window_size, window_size, window_size, window_size, cv2.BORDER_CONSTANT)
    filtered_image = np.zeros_like(image, dtype=np.float64)

    for i in range(window_size, padded_image.shape[0] - window_size):
        for j in range(window_size, padded_image.shape[1] - window_size):
            neighborhood = padded_image[i - window_size:i + window_size + 1, j - window_size:j + window_size + 1]
            numerator = np.sum(neighborhood ** (Q + 1))
            denominator = np.sum(neighborhood ** Q)
            
            if denominator != 0:
                filtered_image[i - window_size, j - window_size] = numerator / denominator
            else:
                filtered_image[i - window_size, j - window_size] = 0

    return np.uint8(filtered_image)

# Load the image
image = cv2.imread('../cat.jpg', cv2.IMREAD_GRAYSCALE)

# Define the window size and the order (Q) of the filter
window_size = 3
Q = 1.5

# Apply the contraharmonic mean filter
filtered_image = contraharmonic_mean_filter(image, window_size, Q)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Contraharmonic Mean Filtered Image')

plt.show()
