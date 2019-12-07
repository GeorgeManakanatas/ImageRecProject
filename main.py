# -*- coding: utf-8 -*-
'''
'''
import json
import cv2
import timeit
from spotTheDif import identify_changes
from utils.processImage import count_image_colors, count_image_colors2, count_image_colors3

def main():
    # load configuration into dictionary
    with open('config.json', 'r') as json_data_file:
        conf = json.load(json_data_file)
    
    image_path = conf["filepath_main"]+'RaspberryPi.png'
    time1 = timeit.default_timer()
    count_image_colors(cv2.imread(image_path))
    time2 = timeit.default_timer()
    print(time2-time1)
    count_image_colors2(cv2.imread(image_path))
    time3 = timeit.default_timer()
    print(time3-time2)
    count_image_colors3(cv2.imread(image_path))
    time4 = timeit.default_timer()
    print(time4-time3)
#    identify_changes(conf["filepath_main"]+conf["main_image"],
#                     conf["filepath_main"]+conf["flawed_image"])


if __name__ == '__main__':
    main()
