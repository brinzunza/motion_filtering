import cv2 as cv

#video = cv.VideoCapture(0) #for live video feed
video = cv.VideoCapture('bird.mp4') #for prerecorded videos
subtractor = cv.createBackgroundSubtractorMOG2(500, 50)

while(True):
    ret, frame = video.read()
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)
    
    if(cv.waitKey(5) == ord('x')):
        break
    #else:
     #   video = cv.VideoCapture('deer.mp4')

cv.destroyAllWindows()
video.release()
