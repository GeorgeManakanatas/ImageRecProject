import cv2
import numpy as np
import random
from utils.utils import display_two_images

########################################################
# functions that process an image without modifying it #
########################################################

# calculate and return mean squared error of 2 provided images
def mean_squared_error(imageA, imageB):
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
    # return 	error value

	return err

# count the number of colors in an image
def count_image_colors (image):
    width = image.shape[0]
    height = image.shape[1]
    imageColorList = []
    # get list of colors in image
    for h in range(0, height):
        for w in range(0, width):
            # get pixel colors
            px = image[w,h]
            # turn to string so we avoid list in list comp issues
            pxvalue = str(px[0])+','+str(px[1])+','+str(px[2])
            # check if value exists in list already
            check = pxvalue in imageColorList
            # append to list if chek is tno true
            if check==False:
                imageColorList.append(pxvalue)
    print('number of discreet colors: ',len(imageColorList))

    return [len(imageColorList)]

# calculate image hash with image and hash size as inputs
def image_hash(image, hash_size):
	# resize the input image, adding a single column (w idth) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hash_size + 1, hash_size))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash
	difference_image = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

	return difference_image

# gradually rescale an image and compare hashes with image, hash size, % of
# rescaling and minimum size as inputs
def rescale_and_compare(image, hash_size, rescale_step, minimum_final_size):
  # array of matches
  match_array = []
  # calculate original hash
  original_image_hash = image_hash(image, hash_size)
  # image width and height
  width = image.shape[0]
  height = image.shape[1]
  # create a number of resized grayscale images
  for new_image_size_ratio in reversed(range(minimum_final_size,100+rescale_step,rescale_step)):
    # calculate new dimentions
    dimensions = (int(height*new_image_size_ratio/100), int(width*new_image_size_ratio/100))
    # perform the actual resizing of the image
    resized = resize_image_to(image, dimensions)
    # try computing the imagehash of both images
    new_image_hash = image_hash(resized, hash_size)
    # append the hash comparison result to array
    if original_image_hash == new_image_hash:
      result = 'hashes match for ratio of: '+str(new_image_size_ratio)+' %'
      match_array.append(result)
    else:
      result = 'hashes do not match for ratio of: '+str(new_image_size_ratio)+' %'
      # append to result array
      #match_array.append(result)

  return(match_array)


# match templates function. Meeds a main image, a secondary image to look for
# in the main image and and array of methods to use with cv.matchTemplate. Will
# display the result for each method, doesn't return anything for now
def match_templates(main_image, subimage, methods):
	# display_two_images('incomming', 'Subimage', 'main_image', subimage, main_image)
	# get the subimage dimentions
	w, h = subimage.shape[:-1]
    # looping over the methods
	for method in methods:
		currentMethod = eval(methods[0])
		# Apply template Matching
		res = cv2.matchTemplate(main_image,subimage,currentMethod)
		# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		# # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
		# if currentMethod in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		# 	top_left = min_loc
		# else:
		# 	top_left = max_loc
		# # settng the bottom corner
		# bottom_right = (top_left[0] + w, top_left[1] + h)
		# # draw box
		# print("rectangle at multiple: ",top_left, bottom_right,)
		# cv2.rectangle(main_image,top_left, bottom_right, 255, 2)

		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		min_threshold = min_val*0.9
		match_locations = np.where(res<=min_threshold)

		print("match_locations : ",len(match_locations),match_locations)
		print("min_val, max_val, min_loc, max_loc : ",min_val, max_val, min_loc, max_loc)
		# # loop through matches
		# for i in range(len(match_locations[0])):
		# 	print("for loop : ",match_locations[0][i],match_locations[1][i])
		# 	print("w, h : ",w," ",h)
		# 	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
		# 	if currentMethod in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		# 		top_left = min_loc
		# 	else:
		# 		top_left = (match_locations[0][i],match_locations[1][i])
		# 	# settng the bottom corner
		# 	bottom_right = (top_left[0] + w, top_left[1] + h)
		# 	cv2.rectangle(main_image,top_left, bottom_right, 255, 2)

		# display both images
		#display_two_images(method, 'Subimage', 'Detected Point', subimage, main_image)
