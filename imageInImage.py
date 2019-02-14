from utils.utils import load_image_from
from utils.utils import display_image
from utils.manipulateImage import rotate_image_by
from utils.processImage import match_templates
from sound.notificationSounds import play_audio_file
from sound.notificationSounds import text_to_speech

# the image filepath
filepath_main = './images/RaspberryPi.png'
filepath_subimage_1 = './images/usb_a.png'
filepath_subimage_2 = './images/chipset.png'
# read the image
main_image = load_image_from(filepath_main)
subimage = load_image_from(filepath_subimage_2)

# list of comparison methods for wasy selection
# methods = ["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR",
#            "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"]
methods = ["cv2.TM_CCOEFF"]


# # start sound
# start = play_audio_file("./sound/Script_started.wav")
# start.play()
# start.close()
#
match_templates(main_image, subimage, methods)
# # end sound
# end = play_audio_file("./sound/Script_finished.wav")
# end.play()
# end.close()

# text_to_speech("this is text to speech")

# rotated_image = rotate_image_by(90, subimage)
# match_templates(main_image, rotated_image, methods)
# rotated_image = rotate_image_by(180, subimage)
# match_templates(main_image, rotated_image, methods)
# rotated_image = rotate_image_by(270, subimage)
# match_templates(main_image, rotated_image, methods)
