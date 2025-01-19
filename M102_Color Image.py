import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['image.cmap'] = 'gray'

# Reading the saved image above ('Emerald_Lakes_New_Zealand.jpg') as a color image.
img_rd=cv2.imread('Emerald_Lakes_New_Zealand.jpg', cv2.IMREAD_COLOR)

# Printing the image shape.
print('The size of the image is : ', img_rd.shape)
plt.figure(figsize = (10, 10))
plt.imshow(img_rd);
nimg_rd= img_rd[:, :, ::-1] #BGR channel was converted to RGB
plt.figure(figsize = (10, 10))
plt.imshow(nimg_rd);

# Converting the image to grayscale using cv2.cvtColor().
img_gray= cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)

# Printing the image shape and Displaying the image using matplotlib imshow()gray
print('The size of the image is : ', img_gray.shape)
plt.figure(figsize = (10, 10))
plt.imshow(img_gray);

# Splitting the image into the B,G,R components
r, g, b= cv2.split(nimg_rd)

plt.figure(figsize = (10, 10))
plt.subplot(141); plt.imshow(r); plt.title('Red Channel')
plt.subplot(142); plt.imshow(g); plt.title('Green Channel')
plt.subplot(143); plt.imshow(b); plt.title('Blue Channel')

# Merging the individual channels into a BGR image.
img_merged= cv2.merge((r,g,b))
plt.subplot(144); plt.imshow(img_merged); plt.title('Merged Channels')

# Changing to HSV Color Space
img_hsv= cv2.cvtColor(img_merged, cv2.COLOR_BGR2HSV)
h, s, v= cv2.split(img_hsv)

plt.figure(figsize = (10, 10))
plt.subplot(141); plt.imshow(h); plt.title('H Channel')
plt.subplot(142); plt.imshow(s); plt.title('S Channel')
plt.subplot(143); plt.imshow(v); plt.title('V Channel')

# Merging the individual channels into a BGR image.
img_hsv_mer= cv2.merge((h,s,v))
plt.subplot(144); plt.imshow(img_merged); plt.title('Original Image');

# Modifying Individual Color Channels
h_mod= h+5;
s_mod= s+10;
v_mod= v+15;

img_modhsv_merge= cv2.merge((h_mod,s_mod,v_mod))
img_mod= cv2.cvtColor(img_modhsv_merge, cv2.COLOR_HSV2BGR)
plt.figure(figsize=(10,10))
plt.subplot(141); plt.imshow(h_mod); plt.title('Modified H Channel')
plt.subplot(142); plt.imshow(s_mod); plt.title('Modified S Channel')
plt.subplot(143); plt.imshow(v_mod); plt.title('Modified V Channel')
plt.subplot(144); plt.imshow(img_mod); plt.title('Modified Image');

plt.show()

#END