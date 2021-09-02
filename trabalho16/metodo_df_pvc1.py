
import numpy as np

class metodo_df_pvc1:
    def __init__(self, n: int, pontos):
        self.n = n
        self.pontos = pontos 


    def metodo(self):
        delta_x = 1.0/self.n
        tam = self.n-1

        centro = -(2/(delta_x**2) + 1)
        borda = 1/(delta_x**2)

        matrix_A = np.zeros((tam, tam))

        for i in range(tam):
            if i > 0:
                matrix_A[i][i-1] = borda
            
            matrix_A[i][i] = centro
            
            if i < tam-1:
                matrix_A[i][i+1] = borda

        matrix_b = [0] * tam
        matrix_b[tam-1] = -borda

        sol_aprox = np.linalg.solve(matrix_A, matrix_b) 
        sol_exata = self.sol_exata()

        return sol_aprox, sol_exata

    
    def sol_exata(self):
        sol_exata = [0] * (self.n-1)
        for i in range(self.n-1):
            x = self.pontos[i]
            sol_exata[i] = (np.exp(-x) - np.exp(x))/(np.exp(-1)-np.exp(1))

        return sol_exata