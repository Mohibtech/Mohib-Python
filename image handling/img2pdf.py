import glob
import os
import re
 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, PageBreak
from reportlab.lib.units import inch
 
#----------------------------------------------------------------------
def sorted_nicely( l ): 
    """ 
    # http://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
 
    Sort the given iterable in the way that humans expect.
    """ 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
 
#----------------------------------------------------------------------
def create_comic(fname, front_cover, back_cover, path):
    """"""
    filename = os.path.join(path, fname + ".pdf")
    doc = SimpleDocTemplate(filename,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]
    width = 7.5*inch
    height = 9.5*inch    
 
    pictures = sorted_nicely(glob.glob(path + "\\*"))
 
    Story.append(Image(front_cover, width, height))
    Story.append(PageBreak())

    for pic in pictures:
        im = Image(pic, width, height)
        Story.append(im)
        Story.append(PageBreak())
 
        doc.build(Story)
        filename = os.path.join(path, page_nums[page_num] % fname)
        doc = SimpleDocTemplate(filename,
                                pagesize=letter,
                                rightMargin=72,leftMargin=72,
                                topMargin=72,bottomMargin=18)
        Story=[]

    Story.append(Image(back_cover, width, height))
    doc.build(Story)
    print( "%s created" % filename )
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    path = r"C:\BACKUPS\Python\urdu\shayad"
    front_cover = os.path.join(path, "001.jpg")
    back_cover = os.path.join(path, "309.jpg")
    create_comic("Shayad_", front_cover, back_cover, path)
