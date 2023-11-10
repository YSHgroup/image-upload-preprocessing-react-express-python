# Image Preprocessing Python
> `This project` is a python script that performs image processing operations on a set of images in a specified directory. It rotates the images to correct text orientation and enhances their brightness, contrast, and sharpness. The processed images are then saved to an output directory.

>  `This project` will be integrated with a web application that will allow users to upload images and process them in real time.

> `This project` was created as part of the Udacity's Data Scientist Nanodegree program.

> `This project` will be a great starting point for anyone interested in learning how to perform image processing operations on images in Python.

## Information

- The code is written in Python 3.
- The code is written in a modular and reusable way.
- The code is well-organized and easy to read.
- The code is well-structured and easy to modify or extend in the future.
- The code is well-documented and easy to understand.
- The code is well-tested and easy to debug.
- The code is well-optimized and easy to maintain.
- The code is well-designed and easy to maintain.

## Installation and run
```
  pip install opencv-python
  pip install pytesseract
  pip install numpy
  pip install Pillow
  pip install imutils

  python main.py

```

### `Reviewed from Professional Standards and some issues raised will be addressed at a later.`

# Code Review

 - [My GitHub](https://github.com/YSHgroup/preprocessing-image-python/blob/master/main.py)

## Summary

 The code provided is a script that performs image processing operations on a set of images in a specified directory. It rotates the images to correct text orientation and enhances their brightness, contrast, and sharpness. The processed images are then saved to an output directory.

## Bug
There is a bug in the code. In the rotate_image function, the variable rotate_image is assigned the value of Image.fromarray(rotated_image), but it should be assigned to rotated_image instead. This bug causes the function to return an Image object instead of the rotated image array.

## Code Style
The code follows the PEP 8 style guide for Python code. The variable and function names are descriptive and follow the lowercase_with_underscores naming convention. The code is well-organized and easy to read.

## Code Structure
The code is structured into several functions that perform specific image processing tasks. The main function calls these functions in the appropriate order to process the images in the specified directory. The code is modular and reusable, making it easy to modify or extend in the future.

## Readability
- The code is generally readable and well-commented. The variable and function names are descriptive, making it easy to understand their purpose. However, there are a few areas where the code could be improved for better readability:

- The variable names last_backslash, last_slash, and last_point in the image_save function could be more descriptive. Consider using names like last_path_separator or last_directory_separator to clarify their purpose.

- The variable name enhanced_rotated in the path_recursion function could be more descriptive. Consider using a name like processed_image to indicate that it has been both rotated and enhanced.

- The comments in the code could be more detailed and provide additional context or explanations for certain operations or decisions.

## Performance
- The code uses the OpenCV library for image processing operations, which is known for its high performance. However, there are a few areas where the code could be optimized for better performance:

- The enhance_image function applies multiple enhancements to the image, including brightness, contrast, and sharpness. Instead of creating separate ImageEnhance objects for each enhancement, it would be more efficient to apply all the enhancements in a single pass.

- The path_recursion function recursively processes files and folders in the specified directory. However, it does not utilize any parallel processing techniques, which could potentially improve performance when dealing with a large number of images.

## Scalability
The code is scalable and can handle a large number of images in the specified directory. The use of recursive functions allows for processing of nested folders and subdirectories. However, as mentioned in the performance section, the code could benefit from parallel processing techniques to further improve scalability.

## Security
The code does not appear to have any security vulnerabilities. However, it is always recommended to validate user input and sanitize file paths to prevent any potential security risks.

## Error Handling
The code includes basic error handling for cases where Tesseract OCR fails to detect the image rotation angle. It catches the exception and assumes that the image is not tilted. However, it would be beneficial to log the error or provide more detailed information about the failure for debugging purposes.

## Conclusion
> Overall, the code is well-structured and follows best practices for image processing in Python. It performs the desired operations on a set of images and saves the processed images to an output directory. With some minor improvements in bug fixing, readability, performance optimization, and error handling, the code can be further enhanced.


### If you have any questions, please contact me at <EMAIL>david.dev100@outlook.com or <SKYPE>live:.cid.abe2f56b5909b6ab

> # Thank you!  David Wilson