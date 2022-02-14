#Created by Seth Rotter
#Compresses png or jpg images from folder named "To Compress"
#Outputs results to folder named "Compressed Images"

from PIL import Image
import PIL
import os
import glob

def main(directory=False, quality=30):
    
    #If there is no directory called "To Compress", create one
    if not os.path.exists(str(".\\To Compress")):
        os.makedirs(str(".\\To Compress"))
    print(os.getcwd())

    #If there is no directory called "Compressed Images", create one
    if not os.path.exists(str(".\\Compressed Images")):
        os.makedirs(str(".\\Compressed Images"))

    #Change directory to "To Compress"
    os.chdir(str(".\\To Compress"))

    #Extract all of the .png and .jpeg files
    files = os.listdir()

    #Extract all of the images
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    #Loop over every image
    for image in images:
        print(image)

        #Open every image
        img = Image.open(image)

        #Compress every image and save it in the directory "Compressed Images"
        img.save("..\\Compressed Images\\"+image, optimize=True)

if __name__ == "__main__":
    main()