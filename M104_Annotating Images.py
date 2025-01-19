import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Reading the image ('Apollo-11-launch.jpg')
img= cv2.imread('Apollo-11-launch.jpg', cv2.IMREAD_COLOR) #Grayscale image was read in color format as it is needed for color annotation
ant_img= img.copy()

#Defining colors for annotations [BGR]
blue= (255, 0, 0)
green= (0, 255, 0)
red= (0, 0, 255)
yellow= (0, 255, 255)
purple= (255, 0, 255)

# Adding the following text to the dark area at the bottom of the image (centered on the image):
# 'Apollo 11 Saturn V Launch, July 16, 1969'.
text = 'Apollo 11 Saturn V Launch, July 16, 1969'
font_face = cv2.FONT_HERSHEY_COMPLEX
font_scale= 1.2
font_color= yellow
font_thickness= 2
ant_img= cv2.putText(ant_img, text, (200, 700), font_face, font_scale, font_color, font_thickness, cv2.LINE_AA)

# Drawing a red line on the black shaded area
ant_img= cv2.line(ant_img, (0,630), (1280,650), red, thickness=6, lineType=cv2.LINE_AA)

# Drawing a green circle in the center
cx=int(ant_img.shape[1]/2)
cy=int(ant_img.shape[0]/2)
#print(cx, cy)
ant_img= cv2.circle(ant_img, (cx, cy), 280, green, thickness=5, lineType=cv2.LINE_AA)

# Draw a purple rectangle that encompasses the rocket.
rect_color = purple
ant_img= cv2.rectangle(ant_img, (610, 100), (700, 570), rect_color, thickness= 5, lineType= cv2.LINE_8)
plt.figure(figsize=(10,10))
plt.imshow(ant_img[:,:,::-1]);
#print(ant_img.shape)

plt.show()

#CODE_END
