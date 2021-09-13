import argparse
import cv2

# ArgParse é usado para captar argumentos passados na chamada do .py no CMD
ap = argparse.ArgumentParser()
# Aqui definimos a label do argumento esperado
ap.add_argument("-i", "--image", required=True,
                help= "Path to the image")
# Criamos um dicionário que receberá os valores dos argumentos
# As chaves do dicionário serão as labels criadas no na definição do argumento
args = vars(ap.parse_args())

# Aqui lemos a imagem que é acessada através do caminho no disco passado como argumento.
# Acessamos o valor em args usando como chave do dicionário args o mesmo valor que a definição do argumento
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))
print("Matrix shape: {}".format(image.shape))

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)