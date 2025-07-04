#Project #3
#Simple Image Simulation (Grayscale Matrix Project)

import numpy as np
from numpy import random

pixel_brightness=np.random.randint(0,256,size=(10,10))
avg_brightness=np.mean(pixel_brightness)
max_brightness=np.max(pixel_brightness)
min_brightness=np.min(pixel_brightness)
inverted_image=255-pixel_brightness
brighter_pixels=pixel_brightness>200
count_brighter_pixels=np.sum(brighter_pixels)


print(f"Orginal Image Matrix:\n\n{pixel_brightness}\n")
print(f"Inverted Image Matrix:\n\n{inverted_image}\n")
print(f"Brightness Stats:\n\nAverage Brightness: {avg_brightness}\nMaximum Brightness: {max_brightness}\nMinimum Brightness: {min_brightness}")
print(f"Pixels Brighter than 200: {count_brighter_pixels}")