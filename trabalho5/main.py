#Cinthia 471317
#Daniele 473257
import gauss_Legendre

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
    a = input(RESET +'Qual será o intervalo [a]? ')
    a = int(a)
    b = input(RESET +'Qual será o intervalo [b]? ')
    b = int(b)
    epson = input(RESET +'Qual será o erro aproximado? ex: 0.000001\n')
    epson = float(epson)
    print(MARG + "              Quadraturas de Gauss-Legendre")
    print(BOLD + "1 - Com dois pontos")
    print(BOLD + "2 - Com três pontos")
    print(BOLD + "3 - Com quatro pontos")
    print(BOLD + "0 - Voltar")
    response = input(RESET +'Qual abordagem você deseja? ')
    response = int(response)
   
    if(response==1):
        result_grau2 = gauss_Legendre.gauss_Legendre_2pontos(a, b, epson)
        print(BOLD + "\n     --------------------------------")
        print(BOLD + "      Resultado: " , result_grau2[1])
        print(BOLD + "      Interações: " , result_grau2[0])
        print(BOLD + "     --------------------------------")
       
    elif(response==2):
        result_grau3 = gauss_Legendre.gauss_Legendre_3pontos(a, b, epson)
        print(BOLD + "\n     --------------------------------")
        print(BOLD + "      Resultado: " , result_grau3[1])
        print(BOLD + "      Interações: " , result_grau3[0])
        print(BOLD + "     --------------------------------")

    elif(response==3):
            result_grau4 = gauss_Legendre.gauss_Legendre_4pontos(a, b, epson)
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , result_grau4[1])
            print(BOLD + "      Interações: " , result_grau4[0])
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


    

