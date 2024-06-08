import os
import glob


resize = r"augment_image\resize"
blur = r"augment_image\blur"
noise = r"augment_image\noise"
high_contrast = r"augment_image\high_contrast"
low_contrast = r"augment_image\low_contrast"
darkness = r"augment_image\darkness"
brightness = r"augment_image\brightness"
folders = [resize, blur, noise, high_contrast, low_contrast, darkness, brightness]

for folder in folders:
    files = glob.glob(os.path.join(folder, '*'))
    for file in files:
        os.remove(file)
