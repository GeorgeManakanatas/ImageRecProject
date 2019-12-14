# -*- coding: utf-8 -*-
'''
main file to run things centrally, just random stuff for now.
'''
import json
# from spot_the_dif import identify_changes
from utils.processImage import imageColorList
from sound.notification_sounds import PlayTheAudioFile, text_to_speech


def main():
    '''
    main finction, just random stuff for now
    '''
    text_to_speech('Initializing')
    # load configuration into dictionary
    with open('config.json', 'r') as json_data_file:
        conf = json.load(json_data_file)
    # Build image path
    image_path = conf["filepath_main"]+'RaspberryPi.png'
    # init the classes
    image_color_list_raspberry_pi = imageColorList(image_path)
    image_color_list_octocat = imageColorList(conf["filepath_main"] +
                                              'Octocat.png')
    start_notification = PlayTheAudioFile('sound/Script_started.wav')
    end_notification = PlayTheAudioFile('sound/Script_finished.wav')

    start_notification.play()
    start_notification.close()
    print('color count from RaspberryPi: ',
          image_color_list_raspberry_pi.image_color_count())
    text_to_speech(str(image_color_list_raspberry_pi.image_color_count()) +
                   ' colors in the RaspberryPi image')

    print('color count from Octocat: ',
          image_color_list_octocat.image_color_count())
    text_to_speech(str(image_color_list_octocat.image_color_count()) +
                   ' colors in the RaspberryPi image')
    end_notification.play()
    end_notification.close()
#    identify_changes(conf["filepath_main"]+conf["main_image"],
#                     conf["filepath_main"]+conf["flawed_image"])


if __name__ == '__main__':
    main()
