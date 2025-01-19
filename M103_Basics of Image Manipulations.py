import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#%matplotlib inline from IPython.display import Image
plt.rcParams['image.cmap'] = 'gray'

img= cv2.imread('New_Zealand_Boat.jpg', cv2.IMREAD_COLOR)
plt.figure(figsize= (10,10))
plt.imshow(img[:,:,::-1]);
copy_img=img.copy()

# Cropping the image to extract the region around the sale boat.
cr_img= copy_img[150:300, 290:440]
plt.figure(figsize=(6,6))
plt.imshow(cr_img[:,:,::-1]);

# Resizing the image up by a factor of 2x.
# Specifying Scaling Factor using fx and fy
res_imgsc= cv2.resize(cr_img, None, fx= 2, fy=2)
plt.figure(figsize=(6,6))
plt.imshow(res_imgsc[:,:,::-1]);
cv2.imwrite('cr_resimg_2x.png',res_imgsc)
#Image(filename= 'cr_resimg_2x.png')
#cr_resimg_2x= cv2.imread('cr_resimg_2x.png', cv2.IMREAD_UNCHANGED)
#cv2.imshow('Read Image',cr_resimg_2x)

# Resizing by Specifying Exact Size of the Output Image
desired_width= 450
desired_height= 150
dimension= (desired_width, desired_height)
res_imgexc= cv2.resize(cr_img, dsize= dimension, interpolation= cv2.INTER_AREA)
plt.figure(figsize=(6,6))
plt.imshow(res_imgexc[:,:,::-1])

# Resizing Dimension while Maintaining Aspect Ratio
desired_width= 400
aspect_ratio= cr_img.shape[0]/cr_img.shape[1]
desired_height= int(desired_width*aspect_ratio)
r_dimension= (desired_width, desired_height)
res_imgas=cv2.resize(cr_img, dsize=r_dimension, interpolation= cv2.INTER_AREA)
plt.figure(figsize=(10,10))
plt.imshow(res_imgas[:,:,::-1])

# Flipping the cropped/resized image horizontally, vertically, and both.
fh_img= cv2.flip(res_imgsc, 1)
fv_img= cv2.flip(res_imgsc, 0)
fb_img= cv2.flip(res_imgsc, -1)
plt.figure(figsize=(12,12))
plt.subplot(141); plt.imshow(fh_img[:,:,::-1]); plt.title('Horizontally Flipped')
plt.subplot(142); plt.imshow(fv_img[:,:,::-1]); plt.title('Vertically Flipped')
plt.subplot(143); plt.imshow(fb_img[:,:,::-1]); plt.title('Both Side Flipped')
plt.subplot(144); plt.imshow(res_imgsc[:,:,::-1]); plt.title('Original Image')

#Accessing image's individual pixel
px_img=cv2.imread('MNIST_3_18x18.png', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(5,5))
plt.imshow(px_img);

print(px_img[2,9]) #Printing individual pixel value
print(px_img[3,10]) #Printing individual pixel value
print(px_img[4,11]) #Printing individual pixel value
copy_px= px_img.copy()

copy_px[0,0]=100 # Modifying specific pixel
copy_px[1,1]=150 # Modifying specific pixel
copy_px[2,2]=200 # Modifying specific pixel
copy_px[3,3]=250 # Modifying specific pixel
copy_px[4,3]=250 # Modifying specific pixel
copy_px[5,2]=200 # Modifying specific pixel
copy_px[6,1]=150 # Modifying specific pixel
copy_px[7,0]=100 # Modifying specific pixel

copy_px[16,0:17]=199 # Using numPy array slicing to modify a group of pixels.
print(copy_px)

plt.figure(figsize=(5,5))
plt.imshow(copy_px);

plt.show()

#CODE_END