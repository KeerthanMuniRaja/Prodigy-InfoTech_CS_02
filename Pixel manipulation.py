import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt

def encrypt_image(image_path):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    data = np.array(image)
    # Get the shape of the image
    original_shape = data.shape
    # Flatten the image data
    flat_data = data.flatten()
    # Generate a random permutation of the indices
    permutation = np.random.permutation(flat_data.size)
    # Shuffle the flat data using the permutation
    encrypted_flat_data = flat_data[permutation]
    # Reshape the encrypted data back to the original shape
    encrypted_data = encrypted_flat_data.reshape(original_shape)
    # Convert the numpy array back to an image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    
    return encrypted_image, permutation

def decrypt_image(encrypted_image, permutation):
    # Convert the encrypted image to a numpy array
    encrypted_data = np.array(encrypted_image)
    # Get the shape of the encrypted image
    original_shape = encrypted_data.shape
    # Flatten the encrypted data
    flat_encrypted_data = encrypted_data.flatten()
    # Create an array to hold the decrypted data
    decrypted_flat_data = np.zeros_like(flat_encrypted_data)
    # Unshuffle the flat encrypted data using the permutation
    decrypted_flat_data[permutation] = flat_encrypted_data
    # Reshape the decrypted data back to the original shape
    decrypted_data = decrypted_flat_data.reshape(original_shape)
    # Convert the numpy array back to an image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    
    return decrypted_image

def apply_simple_operation(flat_data):
    # Simple operation: Add 50 to each pixel value and then mod by 256
    encrypted_flat_data = (flat_data + 50) % 256
    return encrypted_flat_data

def reverse_simple_operation(flat_data):
    # Reverse operation: Subtract 50 from each pixel value and then mod by 256
    decrypted_flat_data = (flat_data - 50) % 256
    return decrypted_flat_data

def encrypt_image_simple(image_path):
    # Open the image
    image = Image.open(image_path.strip('"'))  # Strip extra double quotes from path
    # Convert the image to a numpy array
    data = np.array(image)
    # Get the shape of the image
    original_shape = data.shape
    # Flatten the image data
    flat_data = data.flatten()
    # Apply a simple operation to the flat data
    encrypted_flat_data = apply_simple_operation(flat_data)
    # Reshape the encrypted data back to the original shape
    encrypted_data = encrypted_flat_data.reshape(original_shape)
    # Convert the numpy array back to an image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    
    return encrypted_image

def decrypt_image_simple(encrypted_image):
    # Convert the encrypted image to a numpy array
    encrypted_data = np.array(encrypted_image)
    # Get the shape of the encrypted image
    original_shape = encrypted_data.shape
    # Flatten the encrypted data
    flat_encrypted_data = encrypted_data.flatten()
    # Reverse the simple operation on the flat data
    decrypted_flat_data = reverse_simple_operation(flat_encrypted_data)
    # Reshape the decrypted data back to the original shape
    decrypted_data = decrypted_flat_data.reshape(original_shape)
    # Convert the numpy array back to an image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    
    return decrypted_image

while True:
    # Get the image path from the user
    image_path = input("\nEnter the image path (or 'q' to quit): ")
    if image_path.lower() == 'q':
        print("Exiting the program.")
        break

    # Encrypt the image
    encrypted_image = encrypt_image_simple(image_path)

    # Display options to the user
    while True:
        print("\nChoose an option to display the image:")
        print("1: Original Image")
        print("2: Encrypted Image")
        print("3: Decrypted Image")
        print("4: Terminate")
        option = int(input("Enter your choice (1, 2, 3, or 4): "))

        if option == 1:
            original_image = Image.open(image_path.strip('"'))  # Strip extra double quotes from path
            plt.imshow(original_image)
            plt.title("Original Image")
            plt.axis('off')
            plt.show()
        elif option == 2:
            plt.imshow(encrypted_image)
            plt.title("Encrypted Image")
            plt.axis('off')
            plt.show()
        elif option == 3:
            decrypted_image = decrypt_image_simple(encrypted_image)
            plt.imshow(decrypted_image)
            plt.title("Decrypted Image")
            plt.axis('off')
            plt.show()
        elif option == 4:
            print("Terminating the program.")
            exit()
        else:
            print("Invalid option! Please try again.")
