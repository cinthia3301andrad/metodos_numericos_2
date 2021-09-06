from preditor_corretor import metodo_preditor_corretor

def main():
    print("Solução aproximada do PVI utilizando o método de Preditor-Corretor de 4º ordem\n")
    print("--------------------------------------------------------------------------------------------------")
    print("|   delta_t(s)   |   alt_max(m)   |   temp_alt_max(s)   |   vel_final(m/s)   |   temp_final(s)   |")
    print("--------------------------------------------------------------------------------------------------")

    for i in range(1, 5):
        sol = metodo_preditor_corretor(10**(-i))#essa entrada é meu h que é meus espaços, delta_t
        y_alt_max, t_alt_max, v_mar, t_mar = sol.pontos_criticos()
        print(10**(-i), '             ' ,y_alt_max, '             ', t_alt_max,  '             ',v_mar, t_mar, '             ')
        print("--------------------------------------------------------------------------------------------------")



main()