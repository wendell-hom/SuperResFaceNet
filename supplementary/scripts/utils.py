import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os

def read_all_jpegs(jpeg_folder_path, count=20):
    filenames = os.listdir(jpeg_folder_path)
    results = {}
    for file in filenames[0:count]:
        if file[len(file) - 4:] == '.jpg':
            results[file[0:-4]] = read_jpeg(jpeg_folder_path + "/" + file)

    return results

def read_jpeg(jpeg_path):
    return mpimg.imread(jpeg_path)

def read_filenames(path):
    return os.listdir(path)
