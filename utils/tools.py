import cv2

def flip(img,axes):
    if (axes == 0) :
        #vertical flip
        return cv2.flip( img, 0 )
    elif(axes == 1):
       #horizental flip
        return cv2.flip( img, 1 )
    elif(axes == -1):
        #both direction
        return cv2.flip( img, -1 ) 