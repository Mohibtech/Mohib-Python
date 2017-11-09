from matplotlib.pyplot import imshow
from PIL import Image
import numpy as np
import skimage.color as sc

# Downloading image using PowerShell
# iwr -URI https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/graeme2.jpg -Outfile img.jpg

i = np.array(Image.open('img.jpg'))
imshow(i)

# Changing image from color to grayscale
i_mono = sc.rgb2gray(i)
imshow(i_mono, cmap='gray')
i_mono.shape
