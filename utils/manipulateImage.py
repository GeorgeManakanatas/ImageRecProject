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
class imageManipulation:
    '''
    A class to load and modify images
    '''
    def __init__(self, image_file_path):
        '''
        The constructor for imageManipulation class. Will read the image as
        np.array

        Parameters
            image_file_path(str) : the path to the image file that we want
                                    to work with
        '''
        self.image = cv2.imread(image_file_path)

    def blurr_image(self, ksize):
        '''
        Convert provided image to greyscale and apply Gaussian Blur

        Arguments
            grey_image(np.appray) : the image to be blurred
            ksize(tup) : Gaussian Kernel Size. (height, width)

        Returns
            the blurred image
        '''
        # self.blurred = cv2.GaussianBlur(self.grey_image, (5, 5), 0)
        self.blurred = cv2.GaussianBlur(self.convert_to_greyscale(), ksize, 0)

        return self.blurred

    def convert_to_greyscale(self):
        '''
        Convert provided image to greyscale
        '''
        self.grey_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        return self.grey_image

    def resize_image_to(self, dimensions):
        '''
        Resize image to new dimentions

        Arguments
            dimentions(tuple): the new dimentions in pixels

        Returns
            the resized image
        '''
        self.new_image = cv2.resize(self.convert_to_greyscale(),
                                    dimensions, interpolation=cv2.INTER_AREA)
        return self.new_image

    def random_squares_in_image(self, number_of_modifications,
                                size_of_modifications,
                                color_of_modifications):
        '''
        Generate random squares in the provided image

        Arguments
            number_of_modifications(int) : the number of squares to make
            size_of_modifications(int) : size of square
                modifications and their size as inputs
            color_of_modification(array) : the color of the mofdified area
                in rgb

        Returns
            a modified image
        '''
        self.width = self.image.shape[0]
        self.height = self.image.shape[1]
        color_of_modifications = [0, 0, 236]
        self.squares_image = self.image
        # make a number of alterations to image
        for value in range(0, number_of_modifications):
            # generating random coordinates
            self.rand_x = random.randint(size_of_modifications, self.width-1)
            self.rand_y = random.randint(size_of_modifications, self.height-1)
            # set color of random section
            self.squares_image[self.rand_x -
                               size_of_modifications:self.rand_x,
                               self.rand_y -
                               size_of_modifications:
                                   self.rand_y] = color_of_modifications

        return self.squares_image

    def rotate_image_by(self, angle):
        '''
        Provide rotated image by a certaing angle.

        Arguments
            angle(int) : the number of degrees to rotate

        Returns
            a rotated image
        '''
        self.rotated = imutils.rotate_bound(self.image, angle)
        return self.rotated
