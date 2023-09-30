import cv2
import numpy as np

def alterar_faixa_de_matizes(imagem_hsv, matiz_central, largura_faixa):

    # Crie uma máscara para os pixels cuja matiz esteja dentro da faixa especificada
    min_hue = ((matiz_central - largura_faixa)/2) % 180
    max_hue = ((matiz_central + largura_faixa)/2) % 180
    print(min_hue*2, max_hue*2)
    if min_hue < max_hue:
        mask = cv2.inRange(imagem_hsv, (min_hue, 0, 0), (max_hue, 255, 255))  
    else:
        mask = cv2.inRange(imagem_hsv, (min_hue, 0, 0), (179, 255, 255))
        mask += cv2.inRange(imagem_hsv, (0, 0, 0), (max_hue, 255, 255))

    # Aplique a inversão das matizes dentro da faixa
    imagem_hsv[mask > 0, 0] = (imagem_hsv[mask > 0, 0] + 90) % 180

def main(img, matriz, largura):
    # Carregue a imagem de entrada
    imagem = cv2.imread(img)

    # Converta a imagem para o espaço de cores HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV).astype(np.uint16)

    # Defina os parâmetros
    matiz_central = matriz%359  # nossa matriz
    largura_faixa = int(largura)   # largura da faixa de matizes (valor inteiro x)
    print(matiz_central, largura_faixa)

    alterar_faixa_de_matizes(imagem_hsv, matiz_central, largura_faixa)

    # Converta a imagem de volta para BGR
    imagem_alterada = cv2.cvtColor(imagem_hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    # Salve a imagem alterada
    cv2.imwrite('imagem_alterada.jpg', imagem_alterada)

    # Mostre a imagem original e a imagem alterada
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem Alterada', imagem_alterada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main('circulo.png', 0, 30)