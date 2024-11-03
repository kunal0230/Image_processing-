import cv2
import matplotlib.pyplot as plt

# Load an example image in grayscale
image = cv2.imread("/Users/kunalchaugule/Documents/GITHUB/Edge Detection with OpenCV/x.jpg", cv2.IMREAD_GRAYSCALE)

# Binary Thresholding
_, binary_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding - Mean
adaptive_thresh_mean = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)

# Adaptive Thresholding - Gaussian
adaptive_thresh_gaussian = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# Display the images
titles = ['Original Image', 'Binary Thresholding', 'Adaptive Mean', 'Adaptive Gaussian']
images = [image, binary_thresh, adaptive_thresh_mean, adaptive_thresh_gaussian]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
