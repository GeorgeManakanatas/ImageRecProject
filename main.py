# -*- coding: utf-8 -*-
'''
'''
import json
import cv2
import timeit
from spotTheDif import identify_changes
from utils.processImage import imageColorList, image_hash

def main():
    # load configuration into dictionary
    with open('config.json', 'r') as json_data_file:
        conf = json.load(json_data_file)
    
    image_path = conf["filepath_main"]+'RaspberryPi.png'

    # init the class
    imageColorList_RaspberryPi = imageColorList(image_path)
    imageColorList_Octocat = imageColorList(conf["filepath_main"]+ 
                                            'Octocat.png')
    print('color count from RaspberryPi: ',
          imageColorList_RaspberryPi.image_color_count())
    print('color count from Octocat: ',
          imageColorList_Octocat.image_color_count())

#    identify_changes(conf["filepath_main"]+conf["main_image"],
#                     conf["filepath_main"]+conf["flawed_image"])


if __name__ == '__main__':
    main()
