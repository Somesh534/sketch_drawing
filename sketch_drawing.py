import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def pencil_sketch(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (21, 21), sigmaX=0, sigmaY=0)

    # Create a pencil sketch effect
    sketch = cv2.divide(gray, 255 - blur, scale=255)

    # Resize images for side-by-side comparison
    img_resized = cv2.resize(img, (400, 400))
    sketch_resized = cv2.resize(cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR), (400, 400))

    # Stack images horizontally
    combined = np.hstack((img_resized, sketch_resized))

    # Show the images
    cv2.imshow("Original vs Pencil Sketch", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Open file dialog to select an image
def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    file_path = filedialog.askopenfilename(title="Select an image file", 
                                           filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    return file_path

# Get image path from user
image_path = select_image()

# Run the function if a file is selected
if image_path:
    pencil_sketch(image_path)
else:
    print("No file selected!")
