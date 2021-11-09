### Author: Ridha Alkhabaz
## This script is to create the data set for our training 

import os
import numpy as np
import cv2
from glob import glob

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap=10):
    name1 = 'Train'
    name2 = 'Test'
    save_path1 = os.path.join(save_dir, name1)
    save_path2 = os.path.join(save_dir, name2)
    create_dir(save_path1)
    create_dir(save_path2)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break
        if idx > 1694:
            break 

        if idx == 0:
            cv2.imwrite(f"{save_path1}/F{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path2}/F{idx}.png", frame)
            else:
                cv2.imwrite(f"{save_path1}/F{idx}.png", frame)

        idx += 1

if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "frames"

    for path in video_paths:
        save_frame(path, save_dir, gap=9)