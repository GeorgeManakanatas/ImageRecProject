'''
Random visualisation functions that have no other place to go
'''
import cv2
from matplotlib import pyplot as plt


def display_image(text, image):
    '''
    Display text and image. Closes window after any key pressed

    Arguments
        text(str) : the included text
        image: the image to be displayed

    Returns
        nothing
    '''
    cv2.imshow(text, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def display_two_images(main_text, image1_text, image2_text, image1, image2):
    '''
    Display 2 images for comparison

    Arguments
        main_text(str) : main text for the indow
        image1_text(str) : text for image one
        image2_text(str) : text for image two
        image1 : image one
        image2 : image two

    Returns
        nothing
    '''
    plt.subplot(121), plt.imshow(image1, cmap='gray')
    plt.title(image1_text), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(image2, cmap='gray')
    plt.title(image2_text), plt.xticks([]), plt.yticks([])
    plt.suptitle(main_text)
    plt.show()
