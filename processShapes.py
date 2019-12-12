from utils.detectShapes import DetectShapes
from utils.manipulateImage import convert_to_greyscale, resize_image_to, blurr_image
from utils.display import display_image
import argparse
import imutils
import cv2


# the image filepath
filepath = './images/Shapes.png'
# read the image
image = cv2.imread(filepath)
# display_image("Original", image)

# resizing image
# image = resize_image_to(image, (300, 300))
# display_image("Resized", image)

# greyscale image
grey_image = convert_to_greyscale(image)
# display_image("Grey", grey_image)

# blurr image
blurred = blurr_image(grey_image)
# display_image("Blurred", blurred)

# threshold image
thresh = cv2.threshold(blurred, 245, 255, cv2.THRESH_BINARY_INV)[1]
# display_image("Threshhold", thresh)

# find contours
conts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conts = imutils.grab_contours(conts)

greyWithConts = cv2.drawContours(grey_image, conts, -1, (30,255,0), 1)
display_image("greyWithConts", greyWithConts)

# initialize detet shapes
ds = DetectShapes()
# loop through the contours
for c in conts:
    # find shape for every contour
    detected_shape_is =ds.detect(c)
    # determine contour center
    imageMoments = cv2.moments(c)
    if imageMoments["m00"] :
        centerX = int(imageMoments["m10"] / imageMoments["m00"])
        centerY = int(imageMoments["m01"] / imageMoments["m00"])
    else :
        centerX = None
        centerY = None

    # draw outline
    cv2.drawContours(image, [c], -1, (30,255,0), 2)
    # place text in center
    cv2.putText(image, detected_shape_is, (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # determine color

# show image after processing
display_image("Contours", image)
