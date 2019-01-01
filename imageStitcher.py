# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 03:26:48 2018

@author: arshd
"""
import os
import cv2
 

def loadImages(imgFolder):
    print("loading Images")
    images = [] 
    for (rootDir, dirNames, fileNames) in os.walk(imgFolder):
        for file in fileNames:
            imgPath = os.path.join(imgFolder, file) 
            images.append(cv2.imread(imgPath))
    return images
def stitchImages(imgFolder,outFolder):
    imageList = loadImages(imgFolder)
    print("image loaded")
    print("stitching images")
    stitcher = cv2.createStitcher()
    (status, stitchedImg) = stitcher.stitch(imageList)
    if status == 0:
        cv2.imwrite(outFolder, stitchedImg)
        cv2.imshow("Stitched Image", stitchedImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
    	print("Image stitching failed with status",status)

imgFolder = "ip"
outFolder = "out/output.png"
stitchImages(imgFolder,outFolder)