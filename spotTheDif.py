from skimage.measure import compare_ssim
from utils.utils import load_image_from
from utils.manipulateImage import random_modifications_to_image
from utils.manipulateImage import convert_to_greyscale
from utils.manipulateImage import resize_image_to
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True,
# 	help="first input image")
# ap.add_argument("-s", "--second", required=True,
# 	help="second")
# args = vars(ap.parse_args())

################
# Main section #
################

# # modify one image and spot changes
# # the image filepath
# filepath = "images/Octocat.png"
# # load the two input images
# imageA = load_image_from(filepath)
# imageB = load_image_from(filepath)
# # modify second image
# imageB = random_modifications_to_image(imageB, 3, 10)

# load original and flawed image and spot changes
# load the two input images
imageA = load_image_from("images/RaspberryPi.png")
imageB = load_image_from("images/RaspberryPiFlaw2.png")

# optional resize image
#imageA = resize_image_to(imageA, (200, 200))
#imageB = resize_image_to(imageB, (200, 200))

# convert the images to grayscale
grayA = convert_to_greyscale(imageA)
grayB = convert_to_greyscale(imageB)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 1, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
