from skimage.transform import rescale, resize, downscale_local_mean
import numpy as np
from skimage.io import imsave, imread
import yaml
import sys
import glob
import os

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

params = yaml.safe_load(open('params.yaml'))['resize']
width = params['width']
height = params['height']

print(height)

os.makedirs(os.path.join('data', 'resized'), exist_ok=True)

def resize_image(in_path, out_path):
    print("resizing {} to {}".format(in_path, out_path))
    img = imread(in_path)
    new_size = resize(img, (width, height))
    imsave(out_path, new_size)
    
for image in glob.glob(sys.argv[1]+"/*"):
    out_path = image.replace(sys.argv[1], sys.argv[2])
    resize_image(image, out_path)
