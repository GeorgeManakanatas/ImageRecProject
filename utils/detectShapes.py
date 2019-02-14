from cv2 import *

class DetectShapes:
    def __init__(self):
        # initialize shapes list
        vertices = [0, 1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
        shapes = ["error", "line", "crooked line", "triangle", "rectangle", "pentagon", "hexagon", "eptagon", "octagon", "nonagon", "decagon"]
        shape_tuple_list = list(zip(vertices,shapes))
        self.shape_tuple_list = shape_tuple_list
        pass

    def detect(self,c):
        shape = "NoShape"
        # compute perimeter
        perimeter = cv2.arcLength(c,True)
        # set max distance from contour to approximation
        epsilon = 0.04*perimeter
        # approximate the contour
        approxContour = cv2.approxPolyDP(c, epsilon, True)
        # get shape from list
        if len(approxContour) >= 10 :
            shape = ((11,"circle"))
        else :
            # print(" len(approxContour) ",len(approxContour))
            shape = list(filter(lambda tup: len(approxContour) in tup, self.shape_tuple_list))


        # if shape[0][1] == self.shape_tuple_list[4][1]:
        #     print("rectangle")
        #
        # if shape[0][1] == self.shape_tuple_list[3][1]:
        #     print("triangle")

        return shape[0][1]
