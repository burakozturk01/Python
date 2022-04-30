import cv2
import random as r

def show(img): # Show
   cv2.imshow("Image", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

img = cv2.imread("hakoda.jpg")

for i in range(0, img.shape[0]-4, 4):
   for j in range(0, img.shape[1]-4, 4):
      rand = [r.randint(0, 255) for _ in range(3)]
      img[i+0][j+0] = img[i+0][j+1] = img[i+0][j+2] = img[i+0][j+3] \
      = rand
      img[i+1][j+0] = img[i+1][j+1] = img[i+1][j+2] = img[i+1][j+3] \
      = rand
      img[i+2][j+0] = img[i+2][j+1] = img[i+2][j+2] = img[i+2][j+3] \
      = rand
      img[i+3][j+0] = img[i+3][j+1] = img[i+3][j+2] = img[i+3][j+3] \
      = rand
   
show(img)
