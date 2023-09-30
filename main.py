import cv2
import numpy as np

def alterar_faixa_de_matizes(imagem_hsv, matiz_central, largura_faixa):

    # Criando uma mask cuja matiz esteja dentro da faixa especificada
    min_hue = ((matiz_central - largura_faixa)/2) % 180
    max_hue = ((matiz_central + largura_faixa)/2) % 180

    if min_hue < max_hue:
        mask = cv2.inRange(imagem_hsv, (min_hue, 0, 0), (max_hue, 255, 255))  
    else:
        mask = cv2.inRange(imagem_hsv, (min_hue, 0, 0), (179, 255, 255))
        mask += cv2.inRange(imagem_hsv, (0, 0, 0), (max_hue, 255, 255))

    # Aplicando a inversão das matizes dentro da faixa
    imagem_hsv[mask > 0, 0] = (imagem_hsv[mask > 0, 0] + 90) % 180

def main(img, matiz, largura):
    # Carregando a imagem  e convertendo para o espaço de cores HSV
    imagem = cv2.imread(img)
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV).astype(np.uint16)

    matiz_central = matiz%359  # nossa matiz
    largura_faixa = int(largura)   # largura da faixa de matizes (valor inteiro x)

    alterar_faixa_de_matizes(imagem_hsv, matiz_central, largura_faixa)

    # Converta a imagem de volta para BGR
    imagem_alterada = cv2.cvtColor(imagem_hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    # Salvando a imagem alterada
    cv2.imwrite('imagem_original.jpg', imagem)
    cv2.imwrite('imagem_alterada.jpg', imagem_alterada)

    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem Alterada', imagem_alterada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main('imagens/circ.png', 0, 30)