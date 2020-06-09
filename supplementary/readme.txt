----------------------------
   Supplementary Materials
----------------------------

The materials found here is a condensed version of our github repo: https://github.com/wendell-hom/SuperResFaceNet
and has been cleaned up, renamed, and simplified so that the reader can get a general gist of the salient parts of the project.
Please note that the code here is incomplete; folder structures have been changed for purposes of simplicity to the reader.

Folder structure is as follows:

- scripts/              Contains scripts used for data augmentation and calculating psnr and ssim statistics + other utilities
- data/                 Contains a very tiny set from the training/val set so users can see the types of images we are dealing with
- images/               Contains some of the images we used in our final report, and some images we found interesting
- logs/                 Contains the tensorboard log from training our ESRGAN model for deblurring images
- face_recognition.py   Our jupyter notebook which handles our facial recognition pipeline

