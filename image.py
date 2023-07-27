import os
import numpy as np
from skimage.io import imread, imshow, imsave
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import helper

import cProfile, pstats, io
from pstats import SortKey

def process(directoryName):
    pr = cProfile.Profile()
    pr.enable()

    for filename in os.listdir(directoryName):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filenamestr = filename.split('.')[0]
            extension  = filename.split('.')[1]
            img = imread(os.path.join(directoryName, filename))
            img_new = rgb2gray(img)
            fig = plt.figure() 
            ax1 = fig.add_subplot(221)
            imshow(img_new)
            plt.title('Grayscale Format') 
            imsave(os.getcwd() + "/output/" + filenamestr +"-" + helper.generateRandomName() + "_modified.jpeg", (img_new*255).astype(np.uint8))
        else:
            continue
        
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
