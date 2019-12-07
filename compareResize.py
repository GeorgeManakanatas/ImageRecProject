from utils.manipulateImage import convert_to_greyscale
from utils.processImage import count_image_colors
from utils.display import display_image
from utils.processImage import image_hash
from utils.manipulateImage import resize_image_to
from utils.processImage import rescale_and_compare

################
# Prep section #
################

# the image filepath
filepath = './images/icons8-jenkins-500.png'
# read the image
img = cv2.imread(filepath)
# the hash size
h_size = 8
# step reduction in %
reduce_by = 1
# minimum level in %
reduce_to = 1

################
# Main section #
################

# display original image
display_image('original image',img)

# get number of colors in image
#count_image_colors(img)

# convert to greyscale
grescale_image = convert_to_greyscale(img)

# display grescale image
display_image('greyscale image',grescale_image)

# takes arguments greyscale image, hash size, step in % , end percentage
result_array = rescale_and_compare(grescale_image, h_size, reduce_by, reduce_to)

# print the array matches
print(result_array)
