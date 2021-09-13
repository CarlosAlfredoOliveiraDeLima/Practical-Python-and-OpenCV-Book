import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# A imagem, apesar de estar em orientação de eixos X e Y, segue uma forma de leitura diferente
# O ponto (0, 0) corresponde ao canto superior esquerdo, iniciando dali e crescendo à medida que caminha para baixo e para a direita
(b, g, r) = image[0, 0]
print("Pixel ar (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel ar (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Diferente da forma matemática, onde a coordenada é acessada pela definição de (x, y)
# em OpenCV a imagem é acessada através da forma de (y, x)
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)

cv2.waitKey(0)