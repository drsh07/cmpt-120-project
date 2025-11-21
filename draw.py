# Your header

import cmpt120image
cmpt120image.init()

# Helper functions

def is_white(pixel):
  if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
    return True

# Note: delete all `return False` lines as you complete each function!
def recolor_image(img, color):

  # Get the number of rows and collums this image has
  height = len(img)
  width = len(img[0])

  for row in range(height):
    for col in range(width):
      if is_white(img[row][col]) == False:
        img[row][col] = color

  # NEEDS TO BE CHECKED
  return False

def minify(img):
  # Add your code here
  return False
  
def mirror(img):
  # Add your code here
  return False
  
def draw_item(canvas, item, row, col):
  # Add your code here
  return False
  
def distribute_items(canvas, item, n):
  # Add your code here
  return False
