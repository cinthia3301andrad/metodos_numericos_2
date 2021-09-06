from math import sqrt
import numpy as np

class metodo_house_holder:

    def __init__(self, matriz, tam):
        self.a = matriz
        self.tam = tam


    def metodo(self):
        H = np.identity(self.tam, dtype=float)
        np.set_printoptions(suppress=True)#Se True, sempre imprime números de ponto flutuante usando notação de ponto fixo, caso em que números iguais a zero na precisão atual serão impressos como zero. Se for False, a notação científica será usada quando o valor absoluto do menor número for <1e-4 
        A_ant = self.a
        A_barra = self.a

        for i in range(self.tam - 2): #só precisamos fazer até n-2, já que na coluna n-1 não tem mais nenhum elemento para zerar;
            H_i = self.matriz_householder(A_ant, i)
            aux1 = np.transpose(H_i).dot(A_ant) #TRANSFORMAÇÃO DE SIMILARIDADE 
            A_barra = aux1.dot(H_i) #multiplica  aux1 pelo H_1; essa matriz A_barra já esta com a coluna i cheia de zeros
            A_ant = A_barra
            H = H.dot(H_i) #multiplica H pelo H_1 para acumular o produto das matrizes de HouseHolder

        return A_barra, H #A_barra é a matriz tridiagonal; e a H é o produto das matrizes construidas em cada passo
#para que serve essa matriz acumulada H?
#precisa do H para conseguir os autovetores da matriz inicial (A), que é h*autovaloresMatrizT 

#aula 20
    def matriz_householder(self, matriz, i):#matriz simetrica e coluna i
        w = [0] * self.tam #vetores nulos com tam elementos
        w2 = [0] * self.tam
        n = [0] * self.tam 
        
        for indice in range(i + 1, self.tam):#copia os elementos abaixo da diagonal da coluna i da matriz a
            w[indice] = matriz[indice][i] #para as respectivas posicoes do vetor w, isto é, da posição i+1 até o final
        
        w2[i + 1] = sqrt(self.vetor_x_vetor(w, w)) #aqui copiamos o comprimento do vetor w
        N = np.subtract(w, w2) #agora a gente subtrai o w pelo w'
        
        comp = sqrt(self.vetor_x_vetor(N, N)) #aqui a gente normaliza o vetor N
        for indice2 in range(self.tam):
            n[indice2] = N[indice2]/comp
        
        #montamos a matriz de HouseHolder H = I - 2*nntransposto
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