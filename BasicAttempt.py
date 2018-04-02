import cv2
import imagehash
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/icons8-jenkins-500.png',cv2.IMREAD_COLOR)

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

# convert to greyscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hash original image
originalImageHash = hashImage(grey)
# array of matches
matchArray = []
# image width and height
width = img.shape[0]
height = img.shape[1]
# create a number of resized grayscale images
# 1% step here
for newImageSizeRatio in range(1,101):
    # calculate new dimentions
    dim = (int(height*newImageSizeRatio/100), int(width*newImageSizeRatio/100))
    # print(newImageSizeRatio,dim)
    # perform the actual resizing of the image
    resized = cv2.resize(grey, dim, interpolation = cv2.INTER_AREA)
    # try computing the imagehash of both images
    newImageHash = hashImage(resized)
    # append the hash comparison result
    if originalImageHash == newImageHash:
        result = 'hashes match for ratio of: '+str(newImageSizeRatio)+' %'
        matchArray.append(result)
    else:
        result = 'hashes do not match for ratio of: '+str(newImageSizeRatio)+' %'
        # matchArray.append(result)

print(matchArray)

# get number of colors in images
print(countColors(img))

# cv2.imshow('showImage',img)
# cv2.imshow('greyImage',grey)
# cv2.imshow('resizedImage',resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
