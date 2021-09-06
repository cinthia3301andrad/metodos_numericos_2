import potencia_regular
import numpy as np


#metodo da potencia inversa nada mais é do que o metodo da potencia regular aplicada em cima da matriz inversa
def Potencia_inversa(matriz, vetor, epson):
    a1_inversa = np.linalg.inv(matriz) 
    lambda1_a1, x_dominante = potencia_regular.Potencia_Regular(a1_inversa, vetor, epson) #vai devolver o autovalor dominante da matriz inversa (lambda)
    x_n = x_dominante
    lambda_n_a1 = 1/lambda1_a1 #lambda N é o inverso do lambda dominante da matriz inversa
    return [lambda_n_a1, x_n] #autovalor e autovetor
