import cv2

img = cv2.imread("hakoda.jpg")

# Show
cv2.imshow("Standard", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Double the size
img = cv2.resize(img, (0,0), fx=2, fy=2)

# Show
cv2.imshow("Double size", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Un-double
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Rotate
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# Show
cv2.imshow("Rotated", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Un-rotate
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
