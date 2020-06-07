import argparse
import os
import cv2
import numpy as np
from PIL import Image
from matplotlib import cm
from matplotlib import pyplot as plt
import csv
import sys, getopt
import utils

from PIL import ImageFilter

# qFactor is Quantize Factor
def quantizeImage(filename, qFactor = 4):
    im = Image.open(filename)
    im.show(filename)
    maxColor = np.max(im)
    imOut = im.quantize(colors=int(maxColor / qFactor), method=1)
    #imOut.show()
    return imOut

def downSampleImage(filename, dsFactorW = 1, dsFactorH = 1):
    im = Image.open(filename)
    H, W, _ = np.shape(im)
    WW = int(W/dsFactorW)
    HH = int(H/dsFactorH)
    imOut = im.resize((WW, HH), resample=Image.BICUBIC)
    imOut = imOut.resize((int(W), int(H)), resample=Image.BICUBIC)
    #imOut.show()
    return imOut

def barrelDistortImage(filename):
    im = Image.open(filename)
    H, W, _ = np.shape(im)
    pad = int((H-W)/2)
    im.resize((H, H), resample=Image.LANCZOS).show()
    padIn = np.array(im.resize((H, H), resample=Image.LANCZOS))
    #padIn = np.pad(temp, [(0, 0), (pad,pad), (0,0)])
    print("shape of padIn", np.shape(padIn))
    
    exponent = 2
    origin = int((H)/2)
    scale = 1
    
    x = np.arange(H)
    y = np.arange(H)

    x = (x - origin) / scale
    y = (y - origin) / scale
    R = np.sqrt(x**2+y**2)
    theta = np.arctan2(y, x)

    a = 1
    rmax = np.max(R[:])
    print("rmax", rmax)
    s1 = R + R**3 * (a/(rmax**2))
    x = scale * s1 * np.cos(theta) + origin
    y = scale * s1 * np.sin(theta) + origin
    x[x > 217] = 217
    x[x < 0] = 0
    x = np.array(x, dtype = int)
    y[y > 217] = 217
    y[y < 0] = 0
    y = np.array(y, dtype = int)
    print("x", x)
    out = np.zeros(np.shape(padIn))
    for i in range(H):
        for j in range(H):
            out[i, j, :] = padIn[x[i], y[j], :]
    imOut = Image.fromarray(np.uint8(out))
    imOut.show()
    return

def blurImage(filename, radius = 1):
    im = Image.open(filename)
    H, W, _ = np.shape(im)
    imOut = im.filter(ImageFilter.GaussianBlur(radius=radius))
    out = imOut.resize((int(W/4), int(H/4)), resample=Image.LANCZOS)
    #out.show()
    return out

def main(argv):
    imageDir = None
    outputDir = None
    dsFactorH = 1
    dsFactorW = 1
    filterChoice = int(0)
    radius = 1
    try:
      opts, args = getopt.getopt(argv,"hd:o:p:q:f:r:",["help","imageDir=","outputDir=","dsFactorH=","dsFactorW=","filter=","radius:"])
    except getopt.GetoptError:
      print('applyFilter.py -d <imageDir> -o <outputDir> -p <dsFactorH> -q <dsFactorW> -f <filter=0|DS, 1|blur> -r <blurRadius>')
      sys.exit(2)
    for opt, arg in opts:
      if opt in ('-h', '--help'):
         print('applyFilter.py -d <imageDir> -o <outputDir>')
         sys.exit()
      elif opt in ("-d", "--imageDir"):
         imageDir = arg
      elif opt in ("-o", "--outputDir"):
        outputDir = arg
      elif opt in ("-p", "--dsFactorH"):
        dsFactorH = int(arg)
      elif opt in ("-q", "--dsFactorW"):
        dsFactorW = int(arg)
      elif opt in ("-f", "--filter"):
        filterChoice = int(arg)
      elif opt in ("-r", "--blurRadius"):
        radius = int(arg)

    print('Input filedir is ', imageDir)
    print('Output filedir is', outputDir)
    
    if imageDir == None:
        print("Please provide inputDir path.")
        sys.exit(2)
    
    if outputDir == None:
        print("Please provide outputDir path.")
        sys.exit(2)
    
    filenames = utils.read_filenames(imageDir)

    for files in filenames:
        ext = os.path.splitext(files)[-1].lower()
        if ext in ('.png'):
            inputFileName = os.path.join(imageDir, files)
            outputFileName = os.path.join(outputDir, files)
            print('image name ', inputFileName, " in processing...")
            if filterChoice == 0:
                out = downSampleImage(inputFileName, dsFactorW, dsFactorH)
                out.save(outputFileName)
            elif filterChoice == 1:
                out = blurImage(inputFileName, radius = radius)
                out.save(outputFileName)

    return

if __name__ == '__main__':
    main(sys.argv[1:])
