import cv2
import numpy as np
import matplotlib.pyplot as plt

def exibir_imagem(imagem, titulo):
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.title(titulo)
    plt.axis('off')
    plt.show()


# Leitura da imagem de entrada
src = cv2.imread("D:\Programming\Grupo69\Trabalhos\Alexandra\Convexa\sample.jpg", 1)
if src is None:
    raise FileNotFoundError("The image file 'sample.jpg' was not found.")
exibir_imagem(src, 'Imagem Original')


# Conversão da imagem para escala de cinza
cinza = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
exibir_imagem(cinza, 'Imagem Cinza')


# Aplicação de um desfoque (blur) na imagem para remover ruído
blur = cv2.GaussianBlur(cinza, (5, 5), 0)
exibir_imagem(blur, 'Imagem com Desfoque')


# Binarização da imagem para identificar os pontos de interesse
_, binarizada = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
exibir_imagem(binarizada, 'Imagem Binarizada')


# Encontre os contornos (bordas) na imagem
contornos, _ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

resultado = np.zeros_like(src)

for contorno in contornos:
        # Aproximação do contorno
        epsilon = 0.05 * cv2.arcLength(contorno, True)
        aproximado = cv2.approxPolyDP(contorno, epsilon, True)

        # Encontre a envoltória convexa
        envoltoria = cv2.convexHull(contorno)

        # Desenhe o contorno em verde
        cv2.drawContours(resultado, [contorno], -1, (0, 255, 0), 2)

        # Desenhe a envoltória convexa em azul
        cv2.drawContours(resultado, [envoltoria], -1, (255, 0, 0), 2)

exibir_imagem(resultado, 'Contornos e Envoltórias Convexas')