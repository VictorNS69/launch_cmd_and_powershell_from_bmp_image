#!/usr/bin/env python3
from PIL import Image

# Create 6 pixel image
img = Image.new("RGB", (6, 1), "white")


# Fix each pixel value
pixels = [(10, 0, 0), 
	(13, 10, 13), 
	(100, 109, 99), 
	(120, 101, 46), 
	(0, 0, 101), 
	(0, 0, 0)]

# Put pixels into the image
img.putdata(pixels)
# Save image as .bmp
img.save('cmd_image.bmp', format='bmp')
