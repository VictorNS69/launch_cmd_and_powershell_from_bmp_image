#!/usr/bin/env python3
from PIL import Image

# Create 6 pixel image
img = Image.new("RGB", (6, 1), "white")

# Fix each pixel value
pixels = [(10, 0, 0), 
	(13, 10, 13), 
	(119, 111, 112), 
	(115, 114, 101), 
	(108, 101, 104), 
	(0, 0, 108)]

# Put pixels into the image
img.putdata(pixels)

# Save image as .bmp
img.save("powershell_image.bmp", format="BMP")
