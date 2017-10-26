from PIL import Image
from PIL import ImageEnhance

def adjust_Image(input_image, output_image, factor,option):
    image = Image.open(input_image)

    if option == "brightness":
        enhancer_object = ImageEnhance.Brightness(image)
    elif option == "contrast":
        enhancer_object = ImageEnhance.Contrast(image)
    elif option == "sharpness":
        enhancer_object = ImageEnhance.Sharpness(image)

    out = enhancer_object.enhance(factor)
    out.save(output_image)

if __name__ == '__main__':
    adjust_Image('sweets.jpg',
                      'output/sweets_enhanced.jpg',
                      1.7, "sharpness")

    print("Job Finished")
                      
                      
