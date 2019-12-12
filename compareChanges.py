import imagehash
import matplotlib.pyplot as plt
from utils.manipulateImage import convert_to_greyscale
from utils.processImage import mean_squared_error
from skimage.measure import compare_ssim as ssim

def compare_two_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (mean_squared_error(imageA, imageB),
                                            ssim(imageA, imageB)))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
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
