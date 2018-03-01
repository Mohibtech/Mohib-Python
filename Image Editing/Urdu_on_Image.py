# -*- coding: utf-8 -*-
import arabic_reshaper
import unicodedata
from PIL import Image, ImageDraw, ImageFont

text_to_be_reshaped = 'اب تک'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)

# At this stage the text is reshaped, all letters are in their correct form
# based on their surroundings, but if you are going to print the text in a
# left-to-right context, which usually happens in libraries/apps that do not
# support Arabic and/or right-to-left text rendering, then you need to use
# get_display from python-bidi.
# Note that this is optional and depends on your usage of the reshaped text.

from bidi.algorithm import get_display
bidi_text = get_display(reshaped_text)

# At this stage the text in bidi_text can be easily rendered in any library
# that doesn't support Arabic and/or right-to-left, so use it as you'd use
# any other string. For example if you're using PIL.ImageDraw.text to draw
# text over an image you'd just use it like this...

image = Image.new('RGB', (100, 30), color = (73, 109, 137))
img = ImageDraw.Draw(image)
fnt = ImageFont.truetype(r'D:\Backup\Python\ImageHandling\tahoma.ttf',15)
img.text((10,10), bidi_text, font=fnt, fill=(255,255,255,0))

image.save('pil_urdu_font.png')
