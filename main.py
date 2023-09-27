import cv2
import numpy as np

def alterar_faixa_de_matizes(imagem_hsv, matiz_central, largura_faixa):
    # Crie uma máscara para os pixels cuja matiz esteja dentro da faixa especificada
    min_hue = (matiz_central - largura_faixa) % 180
    max_hue = (matiz_central + largura_faixa) % 180

    if min_hue < max_hue:
        mask = cv2.inRange(imagem_hsv, (min_hue, 0, 0), (max_hue, 255, 255))
    else:
        mask = cv2.inRange(imagem_hsv, (min_hue, 0, 0), (179, 255, 255))
        mask += cv2.inRange(imagem_hsv, (0, 0, 0), (max_hue, 255, 255))

    # Aplique a inversão das matizes dentro da faixa
    imagem_hsv[mask > 0, 0] = (imagem_hsv[mask > 0, 0] + 180) % 180

def main():
    # Carregue a imagem de entrada
    imagem = cv2.imread('sua_imagem.jpg')

    # Converta a imagem para o espaço de cores HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Defina os parâmetros
    matiz_central = 120  # Exemplo: matiz central
    largura_faixa = 20   # Exemplo: largura da faixa de matizes

    # Realize a alteração nas matizes
    alterar_faixa_de_matizes(imagem_hsv, matiz_central, largura_faixa)

    # Converta a imagem de volta para o espaço de cores BGR
    imagem_alterada = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

    # Salve a imagem alterada
    cv2.imwrite('imagem_alterada.jpg', imagem_alterada)

    # Mostre a imagem original e a imagem alterada
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem Alterada', imagem_alterada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
