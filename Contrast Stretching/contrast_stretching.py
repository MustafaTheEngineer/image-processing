from PIL import Image

# Load the image
image = Image.open("../flower.jpg").convert("L")

# Get the minimum and maximum pixel values
min_val, max_val = image.getextrema()

# Define the desired contrast range
desired_min = 0
desired_max = 255

# Apply contrast stretching using point operation
stretched_image = image.point(lambda p: ((p - min_val) / (max_val - min_val)) * (desired_max - desired_min) + desired_min)

# Show the original and stretched images
image.show()
stretched_image.show()
