import os, sys
sys.path.append(os.path.abspath(os.path.join('/data/linc9/3DUnetCNN/')))
from brats.preprocess import convert_brats_data
convert_brats_data("data/original", "data/preprocessed")