'''
Author: sjhuang
Date: 2023-02-05 20:46:01
LastEditTime: 2023-02-05 20:49:00
FilePath: /landmark_detect_and_tracking/video_to_frames.py
'''

import cv2 as cv
import time
import os
import sys


def video2frame(
    video_path:str,
    save_img_dir:str
    ):
    # generate a fold
    if not os.path.exists(save_img_dir):
        os.makedirs(save_img_dir)

    # read video
    if not os.path.isfile(video_path):
        print(video_path + ' not exist')
        sys.exit(1)
    cap = cv.VideoCapture(video_path)

    # frame --> image
    has_frame = True
    idx = 0
    while has_frame:
        has_frame, frame = cap.read()
        if has_frame:
            file_name = f'{idx:06d}.jpg'
            cv.imwrite(os.path.join(save_img_dir, file_name), frame)
        idx += 1
    cap.release()
    print('Done processing.')

if __name__ == '__main__':
    v_p = '/Users/sjhuang/Documents/projects/landmark_detect_and_tracking/889232738_nb3-1-16.mp4'
    video2frame(v_p, save_img_dir = './frames/demo_1/')