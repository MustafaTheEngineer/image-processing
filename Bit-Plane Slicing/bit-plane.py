import cv2
import numpy as np

# Read the input image.
img = cv2.imread('../car.jpg', 0)

# Create a list to store the bit planes.
bit_planes = []

# Iterate over the bit planes, from the LSB to the MSB.
for k in range(0, 8):
    # Create an image for each bit plane.
    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)

    # Execute bitwise AND operation to extract the bit plane.
    res = cv2.bitwise_and(plane, img)

    # Multiply by 255 for better visualization.
    x = res * 255

    # Append the bit plane to the list.
    bit_planes.append(x)

# Display the bit planes.
cv2.imshow("Bit Planes", np.hstack(bit_planes))
cv2.waitKey(0)

# Save the bit planes to disk.
for i in range(0, 8):
    cv2.imwrite('bit_plane_{}.jpg'.format(i), bit_planes[i])