import os
from PIL import Image

# Prompt user for directory input
directory_path = input("Please enter the desired directory: ")

# Check if directory exists
if not os.path.exists(directory_path):
    print("The provided directory does not exist. Please check the path and try again.")
    exit()

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    # Check if the file has a .bmp extension
    if filename.endswith('.bmp'):
        # Create the full file path
        bmp_file_path = os.path.join(directory_path, filename)
        
        # Load the BMP image
        with Image.open(bmp_file_path) as img:
            # Create the output file path with .jpg extension
            jpg_file_path = os.path.join(directory_path, filename[:-4] + ".jpg")
            img.save(jpg_file_path, "JPEG")

        # Delete the .bmp file
        os.remove(bmp_file_path)

print("Conversion completed and original .bmp files deleted!")
