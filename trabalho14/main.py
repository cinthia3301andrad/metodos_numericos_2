from pvi_implicito import metodo_runge_kutta
CYAN  = "\033[1;36m"

BOLD    = "\033[;1m"

def main():
    print(CYAN, "Solução aproximada do PVI utilizando o método de Runge-Kutta de 3º ordem\n")
    print("--------------------------------------------------------------------------------------------------")
    print("|   delta_t(s)   |   alt_max(m)   |   temp_alt_max(s)   |   vel_final(m/s)   |   temp_final(s)   |")
    print("--------------------------------------------------------------------------------------------------")

    for i in range(1, 5):
        solucao = metodo_runge_kutta(10**(-i))
        y_alt_max, t_alt_max, v_mar, t_mar = solucao.pontos_criticos()
        print(10**(-i),"         ", y_alt_max  , "         ",t_alt_max, "         ",v_mar, "         ", t_mar)
  
        print("--------------------------------------------------------------------------------------------------")

main()