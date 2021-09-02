
from metodo_df_pvc1 import metodo_df_pvc1

def main():
    pontos = [0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875]
    sol = metodo_df_pvc1(8, pontos)
    
    sol_aprox, sol_exata = sol.metodo()
    
    print("Método de Diferenças Finitas - PVC1\n")
    print("------------------------------------------------------------------------------")
    print("|      |   Solução aproximada    |    Solução exata    |    Erro relativo    |")
    print("------------------------------------------------------------------------------")
    for i in range(7):
        print("|  y",i+1,  "|",   sol_aprox[i],    "|" ,sol_exata[i], "|", ((sol_aprox[i]-sol_exata[i])/sol_exata[i])*100)       

main()    