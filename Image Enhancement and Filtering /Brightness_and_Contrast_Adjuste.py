import cv2
import numpy as np

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    brightness = int((brightness / 100) * 127)
    contrast = int((contrast / 100) * 127)
    adjusted = cv2.convertScaleAbs(image, alpha=1 + (contrast / 127), beta=brightness)
    return adjusted

image_path = input("Enter the path to the image file: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image. Please check the file path.")
else:
    try:
        brightness = int(input("Enter brightness percentage (-100 to 100): "))
        contrast = int(input("Enter contrast percentage (-100 to 100): "))

        if brightness < -100 or brightness > 100 or contrast < -100 or contrast > 100:
            print("Error: Brightness and contrast values should be between -100 and 100.")
        else:
            adjusted_image = adjust_brightness_contrast(image, brightness, contrast)
            comparison = np.hstack((image, adjusted_image))

            # Display the images
            cv2.imshow("Adjusted Image", adjusted_image)
            cv2.imshow("Comparison (Original vs Adjusted)", comparison)

            # Save images
            cv2.imwrite("adjusted_image.jpg", adjusted_image)
            cv2.imwrite("comparison_image.jpg", comparison)
            print("Adjusted image saved as 'adjusted_image.jpg'")
            print("Comparison image saved as 'comparison_image.jpg'")

            # Close windows on any key press, checking frequently for interruptions
            while True:
                if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                    break

            cv2.destroyAllWindows()
    except ValueError:
        print("Error: Please enter valid integer values for brightness and contrast.")
