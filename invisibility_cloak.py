import cv2
import time
import numpy as np

#Para salvar a saída em um arquivo output.avi


#Iniciando a webcam
cap = cv2.VideoCapture(0)

#Permitindo que a webcam inicie fazendo o código hibernar por 2 segundos
time.sleep(2)
bg = 0

#Capturando fundo para 60 quadros


#Invertendo o fundo


#Lendo o quadro capturado até que a câmera esteja aberta
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Invertendo a imagem para obter consistência
    

    #Convertendo a cor de BGR para HSV
    

    #Gerando máscara para detectar cor vermelha (valores podem ser alterados)
    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255,255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask_1 = mask_1 + mask_2

    cv2.imshow("mask_1", mask_1)


    #Abra e expanda a imagem onde está a máscara 1 (cor)
    


    #Selecionando apenas a parte que não possui máscara um e salvando na máscara 2
   

    #Mantendo apenas a parte das imagens sem a cor vermelha
    

   
    #Mantendo apenas a parte das imagens com a cor vermelha
    

    #Gerando a saída final mesclando res_1 e res_2
    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
    output_file.write(final_output)
    
    #Exibindo a saída para o usuário
    cv2.imshow("magic", final_output)
    cv2.waitKey(1)


cap.release()
out.release()
cv2.destroyAllWindows()

