from ImgScanner import settings
import cv2
from skewCorrector import Correction
import os

path = "media/media/aetna_rotated.png"
img = cv2.imread(path)
A = Correction(img)
A.skewFix(img)