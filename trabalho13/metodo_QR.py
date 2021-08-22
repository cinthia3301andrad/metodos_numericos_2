
from math import sin, cos, atan, fabs, pi
import numpy as np

class metodo_QR:
    def __init__(self, matriz, n, erro):
        self.a = matriz
        self.tam = n
        self.erro = erro

    
    def metodo(self):
        P = np.identity(self.tam, dtype=float)
        np.set_printoptions(suppress=True)
        val = 100
        A_velha = self.a
        A_nova = self.a
        lamb = [0] * self.tam
        
        while(val > self.erro):
            Q, R = self.decomposicaoQR(A_velha)
            A_nova = R.dot(Q)
            A_velha = A_nova
            P = P.dot(Q)
            val = self.somaDosQuadradosDosTermosAbaixoDaDiagonal(A_nova)
        
        lamb = np.diag(A_nova)
        return P, lamb, A_nova

    
    def decomposicaoQR(self, A):
        QT = np.identity(self.tam, dtype=float)
        R_velha = A
        R_nova = A
        
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                J_ij = self.matrizJacobi(R_velha, i, j)
                R_nova = J_ij.dot(R_velha)
                R_velha = R_nova
                QT = J_ij.dot(QT)
                print("Matriz R_nova da iteração ({},{})\n".format(i, j))
                print(R_nova)
                print("\n")

        Q = np.transpose(QT)
        return Q, R_nova


    def matrizJacobi(self, A, i, j):
        J_ij = np.identity(self.tam, dtype=float)
        ang = 0
        erro = 10**(-6)

        if(fabs(A[i][j]) <= erro):
            return J_ij
        
        if(fabs(A[j][j]) <= erro):
            if(A[i][j] < 0):
                ang = pi/2
            else:
                ang = -pi/2
        else:
            ang = atan(-A[i][j]/A[j][j])
        
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