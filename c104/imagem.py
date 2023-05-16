import cv2

img = cv2.imread("butterfly.jpg")
cv2.imshow("Borboleta", img)
#print(img)
pbimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Borboleta", pbimg)
print(pbimg)
cv2.waitKey(0)