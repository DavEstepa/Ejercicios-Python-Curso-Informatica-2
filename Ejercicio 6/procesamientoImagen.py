import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rgb2gray(rgb):
    aGris = np.zeros(rgb.shape, dtype = 'uint8')
    capa1 = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    aGris[:,:,0] = capa1
    aGris[:,:,1] = capa1
    aGris[:,:,2] = capa1
    return aGris

img=mpimg.imread('paisaje.jpg')
(f, c, m) = img.shape
nuevaImagen = np.zeros(img.shape, dtype = 'uint8')
color = [1, 2, 2, 1, 3, 5, 5, 3, 3, 5, 5, 3, 4, 2, 2, 4]
posicion = 0
imgplot = plt.imshow(img)

for i in range(4):
    for j in range(4):
        imgCOPY = img.copy()
        limInff = int(i*f/4)
        limSupf = int((i+1)*f/4)
        limInfc = int(j*c/4)
        limSupc = int((j+1)*c/4)
        if color[posicion] == 1: #COLOR ROJO
            imgCOPY[limInff:limSupf, limInfc:limSupc, 1:] = 0
        elif color[posicion] == 2: #COLOR AZUL
            imgCOPY[limInff:limSupf, limInfc:limSupc, 0:2] = 0
        elif color[posicion] == 3: #ESCALA GRISES
            imgCOPY = rgb2gray(imgCOPY)
        elif color[posicion] == 4: #COLOR VERDE
            imgCOPY[limInff:limSupf, limInfc:limSupc, 0] = 0
            imgCOPY[limInff:limSupf, limInfc:limSupc, 2] = 0
        else:                      #IGUAL A LA ORIGINAL
            pass
        nuevaImagen[limInff:limSupf, limInfc:limSupc, :] = imgCOPY[limInff:limSupf, limInfc:limSupc, :]
        if posicion > len(color)-1:
            pass
        else:
            posicion += 1

imgNEWplot = plt.imshow(nuevaImagen)
plt.imsave('paisaje2.jpg', nuevaImagen)