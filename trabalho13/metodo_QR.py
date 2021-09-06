
from math import sin, cos, atan, fabs, pi
import numpy as np

class metodo_QR:
    def __init__(self, matriz, n, erro):
        self.a = matriz
        self.tam = n
        self.erro = erro

    
    def metodo(self):
        P = np.identity(self.tam, dtype=float)#matriz identidade
        np.set_printoptions(suppress=True)
        val = 100
        A_velha = self.a
        A_nova = self.a
        lamb = [0] * self.tam
        
        while(val > self.erro):
            Q, R = self.decomposicaoQR(A_velha)
            A_nova = R.dot(Q) #matriz R vezes a matriz Q
            A_velha = A_nova
            P = P.dot(Q) #autovetores vai ser esses acumulos
            val = self.somaDosQuadradosDosTermosAbaixoDaDiagonal(A_nova)#para quando essa matriz nova for uma matriz diagonal
            #ou seja, vamos checar se todas as matrizes abaixo da diagonal sao suficientemente proximos de zero
        
        lamb = np.diag(A_nova)
        return P, lamb, A_nova

    
    def decomposicaoQR(self, A):
        QT = np.identity(self.tam, dtype=float) #Esta matriz contém os produtos das matrizes ortogonais 
        R_velha = A#Na inicialização, R velha não tem a estrutura de uma matriz triangular superior
        R_nova = A
        
        for j in range(0, self.tam-1): #// loop das colunas
            for i in range(j+1, self.tam):#loop das linhas
                J_ij = self.matrizJacobi(R_velha, i, j) #// Construção da matriz de Jacobi Jij
                R_nova = J_ij.dot(R_velha)#Produto escalar de duas matrizes. Especificamente, Matriz modificada com elemento (i,j) zerado

                R_velha = R_nova #Salvar para o próximo passo.
                QT = J_ij.dot(QT) #Acumular o produto das matrizes de Jacobi como
                print("Matriz R_nova da iteração ({},{})\n".format(i, j))
                print(R_nova)
                print("\n")

        Q = np.transpose(QT)#QT é a transposta de Q. Note a ordem do produto
        return Q, R_nova #No final do loop externo, o formato da matriz R_nova é triangular superior.


    def matrizJacobi(self, A, i, j):
        J_ij = np.identity(self.tam, dtype=float)#Matriz identidade com n x n elementos
        ang = 0
        erro = 10**(-6)

        if(fabs(A[i][j]) <= erro):#//Considerar Aij= 0, retorna a matriz identidade
            return J_ij
        
        if(fabs(A[j][j]) <= erro): #Considerar (Aij velha) = 0 então
            if(A[i][j] < 0):#O numerador será positivo e assumimos tangente tende a +Inf
                ang = pi/2
            else:
                ang = -pi/2#// O numerador será negativo e assumimos tangente tende a -Inf
        else:
            ang = atan(-A[i][j]/A[j][j]) #Esta função já retorna um ângulo +/-
        
        J_ij[i][i] = cos(ang)
        J_ij[j][j] = cos(ang)
        J_ij[i][j] = sin(ang)        
        J_ij[j][i] = -sin(ang)

        return J_ij


    def somaDosQuadradosDosTermosAbaixoDaDiagonal(self, A):
        soma = 0
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                soma = soma + (A[i][j]*A[i][j])
        
        return soma