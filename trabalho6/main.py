#Cinthia 471317
#Daniele 473257
import gauss_chebyshev
import gauss_hermite
import gauss_laguerre


RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
MARG = "\033[1;95m"
BACKGROUND_BLACK = "\033[1;40m"

isGetOut = False
print(CYAN +"-------------- BEM VINDO AO PROGRAMA --------------")
print(BOLD + "   fórmula base: f(x)=(sen(2x) + 4x^2 + 3x)^2")
print(CYAN + "---------------------------------------------------\n")
while (not isGetOut):
    print(MARG + "          Fórmulas de Gauss para integrações especiais.")
    print(BOLD + "1 - Gauss-Hermite")
    print(BOLD + "2 - Gauss-Laguerre")
    print(BOLD + "3 - Gauss-Chebyshev")
    response = input(RESET +'Qual método você deseja? ')
    response = int(response)
   
    if(response==1):
        grau2 = gauss_hermite.gauss_Hermite_2pontos()
        grau3 = gauss_hermite.gauss_Hermite_3pontos()
        grau4 = gauss_hermite.gauss_Hermite_4pontos()
        print(BOLD + "\n     --------------------------------")
        print(BOLD + "      Resultados: " )
        print(BOLD + "      Grau 2: ", grau2)
        print(BOLD + "      Grau 3: ", grau3)
        print(BOLD + "      Grau 4: ", grau4)
        print(BOLD + "     --------------------------------")
       
    elif(response==2):
        grauL2 = gauss_laguerre.gauss_Laguerre_2pontos()
        grauL3 = gauss_laguerre.gauss_Laguerre_3pontos()
        grauL4 = gauss_laguerre.gauss_Laguerre_4pontos()
        print(BOLD + "\n     --------------------------------")
        print(BOLD + "      Resultados: " )
        print(BOLD + "      Grau 2: ", grauL2)
        print(BOLD + "      Grau 3: ", grauL3)
        print(BOLD + "      Grau 4: ", grauL4)
        print(BOLD + "     --------------------------------")
    elif(response==3):
        grauC2 = gauss_chebyshev.gauss_Chebyshev_2pontos()
        grauC3 = gauss_chebyshev.gauss_Chebyshev_3pontos()
        grauC4 = gauss_chebyshev.gauss_Chebyshev_4pontos()
        print(BOLD + "\n     --------------------------------")
        print(BOLD + "      Resultados: " )
        print(BOLD + "      Grau 2: ", grauC2)
        print(BOLD + "      Grau 3: ", grauC3)
        print(BOLD + "      Grau 4: ", grauC4)
        print(BOLD + "     --------------------------------")
        
    if(response==0):
        isGetOut = True
    print(BOLD + "1 - Calcular novamente")
    print(BOLD + "0 - Sair do programa")
    isFinalish = input(RESET +'O que deseja fazer? ')
    isFinalish = int(isFinalish)
    if(isFinalish==1):
        print(CYAN + "---------------------------------------------------")
        print(BOLD + "   fórmula base: f(x)=(sen(2x) + 4x^2 + 3x)^2")
        print(CYAN + "---------------------------------------------------\n")
    else:
        isGetOut = True


    

