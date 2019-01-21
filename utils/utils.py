import cv2
import numpy as np


def load_image_from(path):

	image = cv2.imread("images/Octocat.png")

	return image

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

def hash_image(image, hash_size):
	# resize the input image, adding a single column (w idth) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hash_size + 1, hash_size))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash
	difference_image = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
	return difference_image

def resize_image_to(image, dimensions):
    # resize to greyscale image to new dimensions
	new_image = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)

	return new_image

def display_image(text, image):
	cv2.imshow(text,image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def rescale_and_compare(image, hash_size, rescale_step, minimum_final_size):

  # array of matches
  match_array = []
  
  # calculate original hash
  original_image_hash = hash_image(image, hash_size)
  
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
    new_image_hash = hash_image(resized, hash_size)
    
    # append the hash comparison result to array
    if original_image_hash == new_image_hash:
      result = 'hashes match for ratio of: '+str(new_image_size_ratio)+' %'
      match_array.append(result)
    else:
      result = 'hashes do not match for ratio of: '+str(new_image_size_ratio)+' %'
      # potentially display image that does not match
      #display_image(result, resized)
      # append to result array
      #match_array.append(result)

  return(match_array)
