
from metodo_df_pvc2 import metodo_df_pvc2

def main():
    sol = metodo_df_pvc2(8, 4)
    
    sol_aprox = sol.metodo()
    
    print("Método das Diferenças Finitas - PVC1\n")

    print("|   SOLUÇÃO APROXIMADA    |")
    print("----------------------------------")
    for i in range(49):
        print("|  y{}  |   {:.8f}           |".format(i+1, sol_aprox[i]))
        print("----------------------------------")
main()