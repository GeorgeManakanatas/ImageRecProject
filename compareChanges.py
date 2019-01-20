import cv2
import imagehash
import numpy as np
import matplotlib.pyplot as plt
#from skimage.measure import structural_similarity as ssim
from skimage.measure import compare_ssim as ssim

def mean_squared_error(imageA, imageB):
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
    # return 	error value

	return err

def convert_to_greyscale(colorImage):
	# this must recieve the image not the tuple
	greyscaleImage = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)

	return greyscaleImage


def compare_two_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mean_squared_error(imageA, imageB)
	s = ssim(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

def display_all_images(images):
	# initialize the figure
	fig = plt.figure("Images")

	# loop over the images
	for (i, (name, image)) in enumerate(images):
		# convert the image to grayscale
		image = convert_to_greyscale(image)
		# show the image
		ax = fig.add_subplot(1, 3, i + 1)
		ax.set_title(name)
		plt.imshow(image, cmap = plt.cm.gray)
		plt.axis("off")

	# show the figure
	plt.show()


def compare_one_to_all(target,images):
	# convert the target to grayscale
	greyTarget = convert_to_greyscale(target[1])
	# loop over the images
	for (i, (name, image)) in enumerate(images):
		# convert the image to grayscale
		image = convert_to_greyscale(image)
		# create title
		title = ""+target[0]+" vs "+name
		# compare
		compare_two_images(greyTarget, image, title)

################
# Main section #
################

# load the images
original = cv2.imread("images/Octocat.png")
opacity = cv2.imread("images/Octocat_opacity.png")
shopped = cv2.imread("images/Octocat_shoped.png")
# create tuples
images = ("Original", original), ("Opacity", opacity), ("Photoshopped", shopped)
# show all the images
display_all_images(images)
# compare all to specific image
compare_one_to_all(images[0],images)
