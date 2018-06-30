"""
Copyright (C) 2018 FireEye, Inc., created by Andrew Shay. All Rights Reserved.
"""

import PIL

from PIL import Image

percent = 30  # Percent for gauge
output_file_name = 'new_gauge.png'

# X and Y coordinates of the center bottom of the needle starting from the top left corner
#   of the image
x = 825
y = 825
loc = (x, y)

percent = percent / 100
rotation = 180 * percent  # 180 degrees because the gauge is half a circle
rotation = 90 - rotation  # Factor in the needle graphic pointing to 50 (90 degrees)

dial = Image.open('needle.png')
dial = dial.rotate(rotation, resample=PIL.Image.BICUBIC, center=loc)  # Rotate needle

gauge = Image.open('gauge.png')
gauge.paste(dial, mask=dial)  # Paste needle onto gauge
gauge.save(output_file_name)
