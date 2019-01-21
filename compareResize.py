from utils.utils import convert_to_greyscale
from utils.utils import load_image_from
from utils.utils import count_image_colors
from utils.utils import display_image
from utils.utils import hash_image
from utils.utils import resize_image_to
from utils.utils import rescale_and_compare

# # reading random pixel
# px = img[66,66]
# print(px)
# section = img[0:66,0:66]
# # set color of image section
# img[0:66,0:66] =  [255,255,255]
# print(img.shape)

# the image filepath
filepath = './images/icons8-jenkins-500.png'

# the hash size
h_size = 8

# step reduction in %
reduce_by = 1

# minimum level in %
reduce_to = 1

# read the image
img = load_image_from(filepath)

# display original image
display_image('original image',img)

# get number of colors in images
print(count_image_colors(img))

# convert to greyscale
grescale_image = convert_to_greyscale(img)

# display grescale image
display_image('greyscale image',grescale_image)

# takes arguments greyscale image, hash size, step in % , end percentage
result_array = rescale_and_compare(grescale_image, h_size, reduce_by, reduce_to)

# print the array matches
print(result_array)
