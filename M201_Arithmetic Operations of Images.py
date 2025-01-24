import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Reading the image ('Santorini.jpg')
image = 'Santorini.jpg'
img = cv2.imread(image, cv2.IMREAD_COLOR)

# Creating a matrix of ones (with data type float64)
matrix_ones = np.ones((10,10), dtype = 'float64')
print(matrix_ones)

# Create two higher contrast images using the 'scale' option with factors of 1.1 and 1.2 (without overflow fix)

contr_img_higher1  = np.ones(img.shape)*1.1
contr_img_higher2  = np.ones(img.shape)*1.2

img_high1= np.uint8(cv2.multiply(np.float64(img), contr_img_higher1))
img_high2= np.uint8(cv2.multiply(np.float64(img), contr_img_higher2))

# Displaying the images (original, higher (1.1x) , high (1.2x))

plt.figure(figsize=[18,5])
plt.subplot(131); plt.imshow(img[:, :, ::-1]);         plt.title('Original')
plt.subplot(132); plt.imshow(img_high1[:, :, ::-1]); plt.title('Higher (1.1x)')
plt.subplot(133); plt.imshow(img_high2[:, :, ::-1]); plt.title('Higher (1.2x)');

# Creating higher contrast images using scale factors of 1.1 and 1.2 (using np.clip() to clip high values to 255)

imgnc_high1= np.uint8(np.clip(cv2.multiply(np.float64(img), contr_img_higher1), 0, 255))
imgnc_high2= np.uint8(np.clip(cv2.multiply(np.float64(img), contr_img_higher2), 0, 255))

# Displaying the images (original, higher (1.1x) clipped , high (1.2x) clipped)
plt.figure(figsize = [18,5])
plt.subplot(131); plt.imshow(img[:, :, ::-1]);         plt.title('Original')
plt.subplot(132); plt.imshow(imgnc_high1[:, :, ::-1]); plt.title('Higher (1.1x): clipped')
plt.subplot(133); plt.imshow(imgnc_high2[:, :, ::-1]); plt.title('Higher (1.2x): clipped');

plt.show()

#CODE_END
