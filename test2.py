import os
import glob


resize = r"adjust_annotation\resize"
blur = r"adjust_annotation\blur"
noise = r"adjust_annotation\noise"
high_contrast = r"adjust_annotation\high_contrast"
low_contrast = r"adjust_annotation\low_contrast"
darkness = r"adjust_annotation\darkness"
brightness = r"adjust_annotation\brightness"

folders = [resize, blur, noise, high_contrast, low_contrast, darkness, brightness]

for folder in folders:
    files = glob.glob(os.path.join(folder, '*'))
    for file in files:
        os.remove(file)
