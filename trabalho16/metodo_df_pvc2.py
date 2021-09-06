
import numpy as np

class metodo_df_pvc2:

    def __init__(self, n: int, fxy):
        self.n = n
        self.fxy = fxy
        

    def metodo(self):
        delta_x = 1.0/self.n 
        delta_y = 1.0/self.n 
        tam = (self.n-1)**2 

        borda_x = 1/(delta_x**2)
        centro = -2 * (1/(delta_x**2) + 1/(delta_y**2))
        borda_y = 1/(delta_y**2)

        matrix_A = np.zeros((tam, tam), dtype=float)
        k = 0
        y = 0
        for i in range(tam):
            if i > 0:
                k = k + 1
                if k%(self.n-1) != 0: 
                    matrix_A[i][i-1] = borda_y
                else:
                    matrix_A[i][i-1] = 0

            if i > (self.n-2):
                matrix_A[i][i-(self.n-1)] = borda_x

            matrix_A[i][i] = centro

            if i < tam-(self.n-1):
                matrix_A[i][i+(self.n-1)] = borda_x

            if i < tam-1:
                y = y + 1
                if y%(self.n-1) !=0: 
                    matrix_A[i][i+1] = borda_y
                else:
                    matrix_A[i][i+1] = 0

        matrix_B = np.empty((tam), dtype=float)
        matrix_B.fill(self.fxy)
        print("A aplicação da máscara sobre os nós das incógnitas gera as seguintes equações:", matrix_A)
        

        matrix_A_inv = np.linalg.inv(matrix_A)
        result = np.dot(matrix_A_inv, matrix_B)#Produto escalar de duas matrizes. Especificamente,
      
        return result