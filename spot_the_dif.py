'''
Module to identify differences between iamges
'''
import imutils
import cv2
from skimage.measure import compare_ssim
# from utils.manipulateImage import random_squares_in_image
from utils.manipulateImage.imageManipulation import convert_to_greyscale
# from utils.manipulateImage import resize_image_to
# import argparse


def identify_changes(filepath_1, filepath_2):
    '''
    Function for detecting differences between images and displaying them

    Arguments
        filepath1(str) : the filepath for the first image
        filepath2(str) : the filepath for the second image

    Returns
        nothing
    '''
    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-f", "--first", required=True,
    # 	help="first input image")
    # ap.add_argument("-s", "--second", required=True,
    # 	help="second")
    # args = vars(ap.parse_args())

    # # modify one image and spot changes
    # # the image filepath
    # filepath = "images/Octocat.png"
    # # load the two input images
    # imageA = cv2.imread(filepath)
    # imageB = cv2.imread(filepath)
    # # modify second image
    # color = [0, 0, 236]
    # imageB = random_squares_in_image(imageB, 3, 10, color)

    # load original and flawed image and spot changes
    # load the two input images

    image_a = cv2.imread(filepath_1)
    image_b = cv2.imread(filepath_2)
    print(type(image_b))
    # optional resize image
    # imageA = resize_image_to(imageA, (200, 200))
    # imageB = resize_image_to(imageB, (200, 200))

    # convert the images to grayscale
    gray_a = convert_to_greyscale(image_a)
    gray_b = convert_to_greyscale(image_b)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    score, diff = compare_ssim(gray_a, gray_b, full=True)
    diff = (diff * 255).astype("uint8")

    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 1, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for contour in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (pos_x, pos_y, width, height) = cv2.boundingRect(contour)
        cv2.rectangle(image_a, (pos_x, pos_y), (pos_x + width, pos_y +
                      height), (0, 0, 255), 2)
        cv2.rectangle(image_b, (pos_x, pos_y), (pos_x + width, pos_y +
                      height), (0, 0, 255), 2)

    # show the output images
    cv2.imshow("Original", image_a)
    cv2.imshow("Modified", image_b)
    cv2.imshow("Diff", diff)
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)


if __name__ == '__main__':
    identify_changes()
