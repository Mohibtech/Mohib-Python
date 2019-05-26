# Rekhta Import
# Please make sure that you are not using scaling on your windows computer before running this script
# Running this script will cause partial images to be recorded
# Requires the selenium web driver. Check this link https://selenium-python.readthedocs.io/installation.html
# This script uses firefox. Please make sure you have firefox installed on your computer.

#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import argparse

#pip install Pillow
from PIL import Image
from io import BytesIO
import time
import os
import sys

def saveImage(driver, bookname, i):
    elem = driver.find_elements_by_id("actualRenderingDiv")
    element = elem[0]
    location = element.location
    size = element.size

    png = driver.get_screenshot_as_png()

    im = Image.open(BytesIO(png))

    left = location['x']
    top = location['y'] + 30
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom))

    filename = '{0:04d}'.format(i)
    im.save(f"{bookname}\{filename}.png") 
    elem.clear()

def clickNext(driver):
    nextButton = driver.find_element_by_css_selector(".left.pull-left.ebookprev")
        
    if not nextButton:
        return False
    else:
        nextButton.click()
        time.sleep(1)
        return True

def makeOutputFolder(bookname):
    directory = f"{bookname}"
    if not os.path.exists(directory):
        os.makedirs(directory)


def main(url, bookname):
    makeOutputFolder(bookname)

    driver = webdriver.Firefox()
    driver.set_window_position(0,0)
    driver.set_window_size(1000,1000)
    driver.get(url)

    index = 1
    while True:
        saveImage(driver, bookname, index)
        movedNext = clickNext(driver)
        if not movedNext:
            break 
        index = index + 1

    driver.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Script to Download books from rekhta.',
        usage='',
        epilog=''
    )

    parser.add_argument('--title', help='Title of book to be imported', required=True)
    parser.add_argument('--url', help='Url of book', required=True)

    args = parser.parse_args()

    main(args.url, args.title)
