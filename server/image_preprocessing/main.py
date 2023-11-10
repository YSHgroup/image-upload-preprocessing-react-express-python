import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import pytesseract
from imutils import rotate_bound
import sys

# Angle of rotation is detected using Tesseract OCR
def detect_tilted_image(image: Image):
    image = np.array(image)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the image
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Perform OCR on the thresholded image
    text = pytesseract.image_to_osd(threshold)

    # Extract the rotation angle from the OCR result
    text = text.split('Rotate: ')[-1].split('\n', 1)[0]
    angle = int(text.strip())
    return angle

# Rotate the image by the calculated angle to correct the text orientation
def rotate_image(image):
    # # Load the input image
    image = np.array(image)
    
    try:
        rotation_angle = detect_tilted_image(image)
        # Rotate the image by the calculated angle to correct the text orientation
        rotated_image = rotate_bound(image, rotation_angle)
        print('no error handled')
        rotate_image = Image.fromarray(rotated_image)
    except Exception as e:
        # If Tesseract can't detect the orientation, assume it's not tilted
        rotated_image = rotate_bound(image, 0)
        print(f"Error during image rotation: {e}")
        rotate_image = Image.fromarray(rotated_image)
    finally: 
        return rotate_image

# Enhance the image's brightness and contrast and sharpen the image
def enhance_image(image):
    image_array = np.array(image)
    
    blurred = cv2.GaussianBlur(image_array, (0, 0), 3)
    sharpened = cv2.addWeighted(image_array, 1.5, blurred, -0.5, 0)
    
    denoised_image_array = cv2.fastNlMeansDenoising(sharpened)
    denoised_image = Image.fromarray(denoised_image_array)
    image_array = np.array(denoised_image)
    image = Image.fromarray(np.uint8(image_array))
    
    # Create an ImageEnhance object and apply the enhancement
    enhancer = ImageEnhance.Sharpness(image)
    enhanced_image = enhancer.enhance(1.5)

    # Create an enhancer object
    enhancer = ImageEnhance.Brightness(image)
    # Increase the brightness by a factor of 1.5
    enhanced_image = enhancer.enhance(1.5)
    
    # Enhance the image's contrast
    enhancer_contrast = ImageEnhance.Contrast(image)
    image = enhancer_contrast.enhance(2)
    return enhanced_image

# Save the image to the output folder
def image_save(path: str, image):
    last_backslash = path.rfind('\\')
    last_slash = path.rindex('/')
    last_point = max(last_backslash, last_slash)
    sliced = path[:last_point]
    if not os.path.exists(sliced):
        os.makedirs(sliced)
    image.save(path)

# Recursive function to process files and folders in a specified path
def path_recursion(input_path: str):
    for item in os.listdir(input_path):
        # Combine the input path with the current item
        path_conbined = os.path.join(input_path, item)
        
        # If the item is a folder, print it and recursively call the function on that folder
        if os.path.isdir(path_conbined):
            print('in folder-->', path_conbined)
            path_recursion(path_conbined)
            
        # If the item is a file with a .jpg, .jpeg, or .png extension, perform image processing operations
        if item.endswith(('.jpg', '.jpeg', 'png')):
            print('file-->', path_conbined)
            
            if item in inputed_files:
                print('processing...', item)
                image = Image.open(path_conbined)
                enhanced_rotated = rotate_image(image)
                enhanced = enhance_image(enhanced_rotated)
                
                # Generate the output path by replacing the source directory with './output' in the original path
                output_path = 'E:/Images/output' + path_conbined.replace('E:/Images/Dataset', '')
                
                # Save the enhanced image to the output path
                image_save(output_path, enhanced)


# Main content of the script 
def main():
    input_folder = 'E:/Images/Dataset'
    output_folder = 'E:/Images/output'
    global inputed_files
    inputed_files = sys.argv[1:]
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    path_recursion(input_folder)

# Run this script
main()