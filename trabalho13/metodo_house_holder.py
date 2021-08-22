from math import sqrt
import numpy as np

class metodo_house_holder:

    def __init__(self, matriz, tam):
        self.a = matriz
        self.tam = tam


    def metodo(self):
        H = np.identity(self.tam, dtype=float)
        np.set_printoptions(suppress=True)
        A_ant = self.a
        A_barra = self.a

        for i in range(self.tam - 2):
            H_i = self.matriz_householder(A_ant, i)
            aux1 = np.transpose(H_i).dot(A_ant)
            A_barra = aux1.dot(H_i)
            A_ant = A_barra
            H = H.dot(H_i)

        return A_barra, H


    def matriz_householder(self, matriz, i):
        w = [0] * self.tam
        w2 = [0] * self.tam
        n = [0] * self.tam 
        
        for indice in range(i + 1, self.tam):
            w[indice] = matriz[indice][i]
        
        w2[i + 1] = sqrt(self.vetor_x_vetor(w, w))
        N = np.subtract(w, w2)
        
        comp = sqrt(self.vetor_x_vetor(N, N))
        for indice2 in range(self.tam):
            n[indice2] = N[indice2]/comp
        
        I = np.identity(self.tam, dtype=float)
        aux1 = self.const_x_vetor(2, n)
        H = np.subtract(I, self.vetor_x_vetor2(aux1, n))
        return H
    

    def vetor_x_vetor(self, v1, v2):
        s = 0
        for i in range(self.tam):
            s = s + v1[i]*v2[i]
        return s

    
    def const_x_vetor(self, n, v):
        res = [0] * self.tam
        for i in range(self.tam):
            res[i] = n*v[i]
        return res

    
    def vetor_x_vetor2(self, v1, v2):
        mat = np.identity(self.tam, dtype=float)
        for i in range(self.tam):
            for j in range(self.tam):
                mat[i][j] = v1[i]*v2[j]
        return mat