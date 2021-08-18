import potencia_inversa
import numpy as np


def Potencia_deslocamento(matriz, vetor, epson, deslocamento):
    novo_A = matriz - deslocamento * np.identity(len(matriz), dtype = int)
    [novo_autovalor, novo_autovetor] = potencia_inversa.Potencia_inversa(novo_A, vetor, epson)
    autovalor = novo_autovalor + deslocamento
    autovetor = novo_autovetor
    return [autovalor, autovetor] #autovalor e autovetor resultante do metodo do deslocamento
