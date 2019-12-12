# -*- coding: utf-8 -*-
'''
main file to run things centrally, just random stuff for now.
'''
import json
# from spot_the_dif import identify_changes
from utils.processImage import imageColorList


def main():
    '''
    main finction, jusk stuff for now
    '''
    # load configuration into dictionary
    with open('config.json', 'r') as json_data_file:
        conf = json.load(json_data_file)

    image_path = conf["filepath_main"]+'RaspberryPi.png'

    # init the class
    image_color_list_raspberry_pi = imageColorList(image_path)
    image_color_list_octocat = imageColorList(conf["filepath_main"] +
                                              'Octocat.png')
    print('color count from RaspberryPi: ',
          image_color_list_raspberry_pi.image_color_count())
    print('color count from Octocat: ',
          image_color_list_octocat.image_color_count())

#    identify_changes(conf["filepath_main"]+conf["main_image"],
#                     conf["filepath_main"]+conf["flawed_image"])


if __name__ == '__main__':
    main()
