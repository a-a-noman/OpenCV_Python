import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Reading image ('Apollo-11-launch.jpg') using OpenCV imread() as a grayscale image.
rd_img= cv2.imread('Apollo-11-launch.jpg', cv2.IMREAD_GRAYSCALE)

# Printing the image width, height, and datatype.
print('Size of the image is ', rd_img.shape)
print('Data type of the image is ', rd_img.dtype)

# Displaying the image using matplotlib imshow().
plt.figure(figsize = [5, 5])
plt.imshow(rd_img,cmap='gray')
plt.title('Apollo-11-launch', fontsize=20)
plt.show()
#cv2.imshow('Image', rd_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Saving the image as a PNG file using OpenCV imwrite().
cv2.imwrite('Test_Apollo-11-launch.png', rd_img)
