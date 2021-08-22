
from metodo_QR import metodo_QR
import numpy as np

def main():
    A = [[40, 8, 4, 2, 1],
         [8, 30, 12, 6, 2],
         [4, 12, 20, 1, 2],
         [2, 6, 1, 25, 4],
         [1, 2, 2, 4, 5]]

    obj = metodo_QR(A, 5, 0.0000001)
    P, lamb, A_nova = obj.metodo()
    
    print("Matriz diagonal\n")
    print(A_nova)
    print("\n")

    print("Matriz P\n")
    print(P)
    print("\n")
    
    P = np.transpose(P)
    
    print("Pares autovalor-autovetor\n")
    for i in range(obj.tam):
        print("{} -> {}".format(lamb[i], P[i]))
       

main()