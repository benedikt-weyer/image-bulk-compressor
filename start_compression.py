from PIL import Image
import os

#set paths
raw_images_path = 'raw-images'
compressed_images_path = 'compressed-images'

raw_images = []

valid_file_extensions = ['.jpg', '.jpeg',]

#load all images from input dir
for file_name in os.listdir(raw_images_path):
    file_extention = os.path.splitext(file_name)[1]
    
    #check vor valid file extension
    if file_extention.lower() not in valid_file_extensions:
        print(f'[WARN] File "{file_name}" not allowed because of not supported file extension. Skipping..')
        continue

    #load image and save in array
    raw_images.append(Image.open(os.path.join(raw_images_path, file_name)))

    print(f'[INFO] "{file_name}" loaded successfully!')

print(f'[INFO] All images loaded sucessfully!')


valid_input = False
image_quality = 100

while not valid_input:
    print(f'[PROMPT] Please enter new image quality between 0 and 100: ')

    #get image quality from console
    input_image_quality = input()

    #convert to int
    image_quality = int(input_image_quality)

    #validate input
    valid_input = image_quality > 0 and image_quality < 100


#compress and save loaded images
for raw_image in raw_images:
    raw_image.save(os.path.join(compressed_images_path, os.path.basename(raw_image.filename)), 'jpeg', optimize = True, quality = image_quality)

    print(f'[INFO] "{os.path.basename(raw_image.filename)}" compressed successfully!')

print(f'[INFO] Done!')