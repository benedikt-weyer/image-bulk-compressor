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
   
