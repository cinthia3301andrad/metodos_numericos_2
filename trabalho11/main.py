import potencia_regular

# Algoritmo 1: Método da Potência Regular

CYAN  = "\033[1;36m"

BOLD    = "\033[;1m"

def main(): 
    print(CYAN +"-------------- BEM VINDO AO PROGRAMA --------------")
    print(BOLD + "            Método da potência regular")
    print(CYAN + "---------------------------------------------------\n")
    v0_a1 = [1, 0, 0]
    v0_a2 = [1, 0, 0, 0, 0]
    a1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]
    a2 = [[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]]
    lambda1_a1, x1_a1 = potencia_regular.Potencia_Regular(a1, v0_a1, 0.00001)
    lambda1_a2, x1_a2 = potencia_regular.Potencia_Regular(a2, v0_a2, 0.00001)


    print(BOLD +"Respostas da matriz A1")
    print("matriz A1: [[5, 2, 1], [2, 3, 1], [1, 1, 2]]")
    print(CYAN +"lambda: {}, x1: ({}, {}, {})".format(lambda1_a1, x1_a1[0], x1_a1[1], x1_a1[2]))
    print("\r")
    print(BOLD +"Respostas da matriz A2")
    print("matriz A2: [[40, 8, 4, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2], [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]]")
    print(CYAN +"lambda: {}, x2: ({}, {}, {}, {}, {})".format(lambda1_a2, x1_a2[0], x1_a2[1], x1_a2[2],x1_a2[3], x1_a2[4]))  

main()