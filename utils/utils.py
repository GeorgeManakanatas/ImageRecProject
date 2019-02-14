import cv2
import random
from matplotlib import pyplot as plt

####################################
# random functions that get reused #
####################################

def generate_random_integer(bottom_end, top_end):
	return random.randint(bottom_end, top_end)

# load image from provided path (realtive or absolute)
def load_image_from(path):
	image = cv2.imread(path)

	return image

# get text and image and display them. Closes window after any key pressed
def display_image(text, image):
	cv2.imshow(text,image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# diplay 2 images for comparison. Inputs are the main and image texts and then
# the two images
def display_two_images(main_text,image1_text, image2_text, image1, image2):
	plt.subplot(121),plt.imshow(image1,cmap = 'gray')
	plt.title(image1_text), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(image2,cmap = 'gray')
	plt.title(image2_text), plt.xticks([]), plt.yticks([])
	plt.suptitle(main_text)
	plt.show()
