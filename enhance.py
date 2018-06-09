#Underwater Image Enhancement
#Don't alter the comments they are for testing purpose!
import cv2
import numpy as np
from PIL import Image,ImageFilter
import os
import cv2
import shutil
import time
import sys
#os.chdir('C:\\')

def phase2(img):
	b, g, r = cv2.split(img)
	b = cv2.equalizeHist(b)
	g = cv2.equalizeHist(g)
	r = cv2.equalizeHist(r)
	limg = cv2.merge((b,g,r))
	lab= cv2.cvtColor(limg, cv2.COLOR_BGR2LAB)
	l, a, b = cv2.split(lab)
	clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(1,1))
	cl = clahe.apply(l)
	limg = cv2.merge((cl,a,b))
	rgb = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
	#out = cv2.addWeighted(hls2bgr, 0.4, rgb, 0.4,0)
	#cv2.imshow("phase2",rgb)
	#cv2.waitKey(0)
	return rgb

def phase3(img):
	img3 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB) # RGB to YCbCr
	#cv2.imshow('Y channel', img3)
	#cv2.waitKey(0)
	return img3

def phase4(img):
	Y,Cb,Cr=cv2.split(img)
	Y = cv2.equalizeHist(Y)
	img=cv2.merge((Y,Cb,Cr))
	#Y=cv2.cvtColor(np.uint8(cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F)), cv2.COLOR_GRAY2BGR)
	#img4=cv2.merge((Y,Cb,Cr))
	img5 = cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)
	#cv2.imshow("y channel",img5)
	#cv2.waitKey(0)
	return img5
	

def main_process(img):
    #img = cv2.imread('test.png')
    #dst = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
    #cv2.imwrite('test1.png',dst)
    #img1=phase1(img)
    img1=phase2(img)	
    img3=phase3(img1)
    img5=phase4(img3)
    dst = cv2.resize(img5, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
    return dst
       
def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + ' ' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()
def progress_bar():
    total = 100
    i = 0
    while i <= total:
        progress(i, total)
        time.sleep(0.03)  # emulating long-playing job
        i += 1    
def main():
    
    src_dir = "//home//abid//op//"
    dist_dir = ("//home//abid//opp//")
    for filename in os.listdir(src_dir):
        if filename.endswith('.jpg'):
            shutil.copy( src_dir + filename, dist_dir)
		
    os.chdir("//home//abid//opp//")
    for files in os.listdir(dist_dir):
        if files.endswith(".jpg"):
            print ("Processing "+files)
            img=cv2.imread(files)
            fimg=main_process(img)
            progress_bar()
            
            cv2.imwrite(""+files,fimg)   
            #cv2.waitKey(0)


if __name__ == "__main__":
    main()



print "Processing Complete press enter to close this prompt"
raw_input()	