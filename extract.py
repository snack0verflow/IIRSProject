import os
folder = "//home//user//Pictures//"  
# Frame Extraction Module
import cv2
print(cv2.__version__)  # my version is 3.1.0
print "Processing please wait"
vidcap = cv2.VideoCapture('//home//user//Nikhil//test.mp4')
count = 0
while True:
    success,image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))
print "Complete"
raw_input()