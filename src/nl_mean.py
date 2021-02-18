from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np
from skimage.io import imsave, imread

import yaml
import sys
import glob
import os

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython nl_mean.py data-folder-in data-folder-out\n")
    sys.exit(1)

params = yaml.safe_load(open('params.yaml'))['nl-mean']
patch_size = params['patch_size']
patch_distance = params['patch_distance']
h = params['h']

os.makedirs(os.path.join('data', 'nl-mean'), exist_ok=True)

def nonlocal_means(in_path, out_path):
    out_path = out_path.replace(".jpg", "_{}.jpg".format(patch_size))
    noisy = imread(in_path)

    patch_kw = dict(patch_size=patch_size,  # 5x5 patches
                    patch_distance=patch_distance,  # 13x13 search area
                    multichannel=True)

    sigma_est = np.mean(estimate_sigma(noisy, multichannel=True))

    denoised = denoise_nl_means(noisy, h=(h+0.01) * sigma_est, sigma=sigma_est,
                                     fast_mode=True, **patch_kw)
    imsave(out_path, denoised)
    
for image in glob.glob(sys.argv[1]+"/*"):
    out_path = image.replace(sys.argv[1], sys.argv[2])
    nonlocal_means(image, out_path)



