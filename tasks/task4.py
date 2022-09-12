from PIL import Image
import re

# function: Image Resizer
def img_resizer(img, h, w): 
    # 1. Print the given image
    pic = Image.open(img)
    pic.show()

    # 2. Print the H and W of given image
    height, width= pic.size
    print("Old Height:", height,"\nOld Width:", width)

    # 3. Resize the given image to the given H and W
    pic2= pic.resize((h,w))

    # 4. Print the resize image 
    pic2.show()

    # 5. Print the New H and W of resize image
    height2, width2= pic2.size
    print("New Height:", height2,"\nNew Width:", width2)

# Function: Check the Image path format 
def check_img_format(img):
     # Regex to check valid image file extension.
    regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    if (img == ""):
        print("Path can't be empty")
        exit()
    elif(re.search(p, img)):
        return True
    else:
        print("Wrong Path Format!")
        exit()

# calling functions
image= input("Give Image Path: ")

check_img_format(image)

height= input("Give Resize Height: ")
width= input("Give Resize Width: ")

if  height.isnumeric() == False or width.isnumeric() == False:
    print("Height & Width will only recognize as Numeric e.g. 400 x 400")
else:
    height= int(height) 
    width= int(width)
    img_resizer(image, height, width)