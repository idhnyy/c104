import cv2

foguete = cv2.imread("poster.jpg")
recorte = foguete[120:360, 400:500]
foguete[0:240, 500:600] = recorte
texto = "Foguete"
cv2.putText(foguete, 
            texto, 
            (20,220), 
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.9,
            color = (30,70,255))
cv2.imshow("Imagem",foguete)
cv2.waitKey(0)