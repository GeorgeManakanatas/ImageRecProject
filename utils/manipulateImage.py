'''
'''
import cv2
import numpy as np
import imutils
import random
from matplotlib import pyplot as plt
from utils.display import display_two_images

###########################################
# functions that modify an existing image #
###########################################

# get greyscale image and blurr it
def blurr_image(grey_image):
	# blurring image
	blurred = cv2.GaussianBlur(grey_image, (5, 5), 0)

	return blurred

# get color image and return grayscale one
def convert_to_greyscale(colorImage):
	# this must recieve the image not the tuple
	greyscaleImage = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)

	return greyscaleImage


def resize_image_to(image, dimensions):
    '''
    Resize greyscale image to new dimentions

    Arguments
        image: the image to be resized, must be geyscale
        dimentions(tuple): the new dimentions in pixels

    Returns
        the resized image
    '''
    new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
    return new_image


def random_modifications_to_image(image, number_of_modifications,
                                  size_of_modifications):
    '''
    Generate random modifications to an image

    Arguments
        image :the image to be modified
        number_of_modifications(int): the number of modifications to be made
        size_of_modifications():
    moidifications and their size as inputs. Returns the modified image
    '''
    # get image height and width
    width = image.shape[0]
    height = image.shape[1]

    # make a number of alterations to image
    for value in range(0, number_of_modifications):
        # generating random coordinates
        rand_x = random.randint(size_of_modifications, width-1)
        rand_y = random.randint(size_of_modifications, height-1)
        # set color of random section
        image[rand_x-size_of_modifications:rand_x,
              rand_y-size_of_modifications:rand_y] = [0, 0, 236]

    return image


# rotate image by a certaing angle. Inputs are the angle of clockwise rotation
# and the image.
def rotate_image_by(angle, image):
	rotated = imutils.rotate_bound(image, angle)
	return rotated