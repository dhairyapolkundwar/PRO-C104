import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img, "Sun", (50,20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 0, 255))
cv2.putText(img, "Mercury", (100, 150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, "Venus", (180, 175), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 255))
cv2.putText(img, "Earth", (270, 150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 0))
cv2.putText(img, "Mars", (380, 250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 125, 255))
cv2.putText(img, "Jupiter", (490, 50), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, "Saturn", (800, 360), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255, 255, 255))
cv2.putText(img, "Uranus", (950, 145), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(230, 200, 0))
cv2.putText(img, "Neptune", (1080, 135), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(230, 183, 0))

cv2.imshow("Solar System", img)
cv2.imwrite("Solar_System_With_Name.jpg", img)
cv2.waitKey(0)
