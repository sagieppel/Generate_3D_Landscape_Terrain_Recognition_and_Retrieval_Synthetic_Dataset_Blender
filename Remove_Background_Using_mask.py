# Assuming each jpg image have corresponding map with _MASK.png ending use the _MASK.png file to delete/blackended the jpg image bacground
import cv2
import os
import numpy
indir= r"Output_landscape_dataset//" # input folder with subfolders containing images and masks
outdir="Generated_Dataset_black_background//" # output folder for masks
if not os.path.exists(outdir): os.mkdir(outdir)
for sdr in os.listdir(indir):
   outpath=outdir+"//"+sdr
   dr = indir + "//" + sdr
   if not os.path.exists(outpath):
       os.mkdir(outpath)
   for fl in os.listdir(dr):
           inpt=dr+"//"+fl
           if ".jpg" in inpt:
               im=cv2.imread(inpt)
               mask=cv2.imread(inpt.replace(".jpg","_MASK.png"))
               im[mask<125]=0
               cv2.imwrite(outpath+"//"+fl,im)
               print(outpath+"//"+fl)
