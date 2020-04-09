import cv2.cv2 as cv2
from pynput.mouse import Button, Controller
import time

print('Iniciando...')
time.sleep(3)
mouse = Controller()

mouse.position = (755, 241)  # (579, 332)
initial_position = mouse.position

image = cv2.imread('download.png')

dimensions = (410, 320)
resized_image = cv2.resize(image, dimensions)

for linha, linha_de_pixel in enumerate(resized_image):
    mouse.position = (initial_position[0], initial_position[1] + linha)
    for n_pixel, pixel in enumerate(linha_de_pixel):
        if sum(pixel) / 3 < 127.5:
            time.sleep(0.00000001)
            # mouse.click(Button.left, 1)
            mouse.press(Button.left)
        else:
            mouse.release(Button.left)
        mouse.position = (initial_position[0] + n_pixel, initial_position[1] + linha)
