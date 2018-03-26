import cv2
import imagehash
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/Octocat.png',cv2.IMREAD_COLOR)

# # reading random pixel
# px = img[66,66]
# print(px)
# section = img[0:66,0:66]
# # set color of image section
# img[0:66,0:66] =  [255,255,255]
# print(img.shape)

def countColors ( ima ):
    width = ima.shape[0]
    height = ima.shape[1]
    imageColorList = []
    # get list of colors in image
    for h in range(0, height):
        for w in range(0, width):
            # get pixel colors
            px = ima[w,h]
            # turn to string so we avoid list in list comp issues
            pxvalue = str(px[0])+','+str(px[1])+','+str(px[2])
            # check if value exists in list already
            check = pxvalue in imageColorList
            # append to list if chek is tno true
            if check==False:
                imageColorList.append(pxvalue)
    print('number of discreet colors: ',len(imageColorList))
    return [len(imageColorList)]

def hashImage(image, hashSize=8):
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hashSize + 1, hashSize))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

print(countColors(img))
# convert to greyscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# resize grey image
# get ratio to avoid distortion
r = 300.0 / grey.shape[1]
dim = (300, int(grey.shape[0] * r))
# perform the actual resizing of the image
resized = cv2.resize(grey, dim, interpolation = cv2.INTER_AREA)
# try computing the imagehash of both images
greyscaleHash1 = hashImage(grey)
greyscaleHash2 = hashImage(resized)

# report if the hash matches
if greyscaleHash1 == greyscaleHash2:
    print('hashes match!!')
else:
    print('hashes do not match')

print(greyscaleHash1)
print(greyscaleHash2)
# cv2.imshow('showImage',img)
cv2.imshow('greyImage',grey)
cv2.imshow('resizedImage',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
