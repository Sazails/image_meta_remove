import os
from PIL import Image
from tkinter import filedialog, Tk
import exifread

def select_image():
    root = Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png *.jpg")])
    while not os.path.isfile(image_path) or not image_path.lower().endswith(('.png', '.jpg')):
        print("Invalid image file. Please try again.")
        image_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png *.jpg")])
    return image_path

def print_metadata(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
    
    print("Existing metadata:")
    for tag, value in tags.items():
        print(f"{tag}: {value}")

def remove_metadata(image_path):
    image = Image.open(image_path)
    image_without_metadata = image.copy()
    image_without_metadata.info.clear()
    image_without_metadata.save(image_path)

def print_new_metadata(image_path):
    image = Image.open(image_path)
    metadata = image.info
    print("New metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

def main():
    image_path = select_image()
    print(f"Selected image: {image_path}")
    print_metadata(image_path)
    choice = input("Do you want to remove the metadata from this image? (yes/no): ")
    if choice.lower() in ["no", "n", "nope"]:
        print("Program closed.")
        return
    elif choice.lower() in ["yes", "y", "yeah"]:
        remove_metadata(image_path)
        print("Metadata removal done.")
        print_new_metadata(image_path)
    input("Press any key to quit the program.")

if __name__ == "__main__":
    main()
