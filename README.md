# Image Encryption and Decryption using Pixel Manipulation

## Purpose
The purpose of this project is to demonstrate image encryption and decryption using pixel manipulation techniques in Python. The encryption method involves applying a simple mathematical operation to each pixel value, making the image unreadable without the decryption process.

## Description
This project allows users to encrypt and decrypt images using Python's PIL (Pillow) library. The encryption process involves flattening the image data, applying a simple operation (adding 50 and taking modulo 256), and reshaping it back to the original image dimensions. Decryption reverses this process to recover the original image.

## How It Works
1. **Encryption:**
   - Open an image and convert it into a numpy array.
   - Flatten the image data.
   - Apply a simple operation (add 50 and modulo 256) to each pixel value.
   - Reshape the modified data back to the original image shape and convert it back to an image format.

2. **Decryption:**
   - Convert the encrypted image into a numpy array.
   - Flatten the encrypted image data.
   - Reverse the simple operation to recover the original pixel values.
   - Reshape the decrypted data back to the original image shape and convert it back to an image format.

3. **User Interaction:**
   - Prompt the user to enter the path of the image to encrypt.
   - Display options to view the original image, encrypted image, and decrypted image.

## Output
- **Original Image:** Display the original image before encryption.
- **Encrypted Image:** Display the encrypted version of the image after applying the encryption operation.
- **Decrypted Image:** Display the decrypted version of the image after reversing the encryption operation.

## Installation and Setup
1. **Python Environment:**
   - Ensure Python is installed on your system.
   - Install necessary libraries: `numpy`, `Pillow`, and `matplotlib`.

2. **Execution:**
   - Save the script and run it in a Python environment or IDE.
   - Enter the path of the image file when prompted.

## Example Usage
1. **Encrypting an Image:**
   - Input Image: Any image file (e.g., `image.jpg`).
   - Output: Encrypted version of the image displayed using matplotlib.

2. **Decrypting an Image:**
   - Input: Encrypted image obtained from the encryption process.
   - Output: Decrypted version of the image displayed using matplotlib.

## Notes
- This script demonstrates basic image encryption and decryption techniques for educational purposes.
- Modify the encryption operation (`apply_simple_operation` and `reverse_simple_operation` functions) for different encryption strengths and effects.
