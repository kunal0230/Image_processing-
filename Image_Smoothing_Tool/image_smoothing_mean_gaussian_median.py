import cv2
import numpy as np
import os

def apply_filter(image, filter_type, threshold):
    # Convert threshold percentage to actual size for the kernel
    kernel_size = max(1, int(threshold / 100 * 50))  # scale to max kernel size
    kernel_size = kernel_size + 1 if kernel_size % 2 == 0 else kernel_size  # Ensure odd kernel size

    if filter_type == 'mean':
        smoothed_image = cv2.blur(image, (kernel_size, kernel_size))
    elif filter_type == 'gaussian':
        smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    elif filter_type == 'median':
        smoothed_image = cv2.medianBlur(image, kernel_size)
    else:
        raise ValueError("Invalid filter type. Choose 'mean', 'gaussian', or 'median'.")
    
    return smoothed_image

def create_comparison_image(original, processed):
    # Concatenate images horizontally
    comparison_image = np.hstack((original, processed))
    return comparison_image

def main():
    # Get user input
    image_path = input("Enter the path to the image: ")
    filter_type = input("Select filter (mean, gaussian, median): ").lower()
    threshold = float(input("Enter threshold value (0-100): "))
    
    # Validate threshold value
    if not (0 <= threshold <= 100):
        print("Threshold must be between 0 and 100.")
        return
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Could not open or find the image.")
        return
    
    # Apply the selected filter
    smoothed_image = apply_filter(image, filter_type, threshold)

    # Create comparison image
    comparison_image = create_comparison_image(image, smoothed_image)

    # Generate output paths
    original_image_name = os.path.basename(image_path)
    processed_image_name = f"processed_{original_image_name}"
    comparison_image_name = f"comparison_{original_image_name}"

    # Save the processed and comparison images
    cv2.imwrite(processed_image_name, smoothed_image)
    cv2.imwrite(comparison_image_name, comparison_image)

    # Display the original, smoothed, and comparison images
    cv2.imshow('Original Image', image)
    cv2.imshow('Smoothed Image', smoothed_image)
    cv2.imshow('Comparison', comparison_image)

    # Wait for a key event and check if it's the escape key
    while True:
        key = cv2.waitKey(1)  # Wait for a short time (1 ms)
        if key == 27:  # Escape key ASCII code
            break

    cv2.destroyAllWindows()
    print("All windows closed.")

if __name__ == "__main__":
    main()
