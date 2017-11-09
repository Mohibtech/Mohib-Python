# Denoising with Filters

# Add Noise
import skimage
i_n = skimage.util.random_noise(i_eq)
imshow(i_n, cmap="gray")

# Use a Gaussian Filter
def gauss_filter(im, sigma = 10):
    from scipy.ndimage.filters import gaussian_filter as gf
    import numpy as np
    return gf(im, sigma = sigma)  
 
i_g = gauss_filter(i_n)
imshow(i_g, cmap="gray")

# Use a Median Filter
def med_filter(im, size = 10):
    from scipy.ndimage.filters import median_filter as mf
    import numpy as np
    return mf(im, size = size)   
  
i_m = med_filter(i_n)
imshow(i_m, cmap="gray")
