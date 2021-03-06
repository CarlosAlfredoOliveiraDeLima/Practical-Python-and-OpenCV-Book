import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

# Desenhando uma linha simples
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Desenhando uma linha com aumento de espessura, definida no quinto argumento de cv2.line
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

yellow = (0, 255, 255)
cv2.rectangle(canvas, (10, 10), (60, 60), yellow)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

purple = (255, 0, 255)
cv2.rectangle(canvas, (50, 200), (200, 225), purple, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (255, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for radius in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), radius, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    if i == 0:
        cv2.circle(canvas, tuple(pt), radius, color, -1)
    else:
        cv2.circle(canvas, tuple(pt), radius, color, 2)
    print(f'Color: {color}, Center Point: {tuple(pt)}')

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)