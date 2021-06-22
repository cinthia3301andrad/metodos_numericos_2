import newtonCotes

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
    print(MARG + "              FÓRMULAS DE NEWTON-COTES")
    print(BOLD + "1 - Abordagem aberta")
    print(BOLD + "2 - Abordagem fechada")
    print(BOLD + "0 - Sair do programa")
    approach = input(RESET +'Qual abordagem você deseja? ')
    approach = int(approach)
    # while(intApproach < 0 and intApproach > 3):
    #     print(RED + "input inválido!")
    #     approach = input('Qual abordagem você deseja? ')
    if(approach==1):
        print(MARG + "\n              Abordagem aberta")
        print(BOLD + "1 - Polinômio de substituição de grau 1 [Regra do Trapézio]")
        print(BOLD + "2 - Polinômio de substituição de grau 2 [Regra de Simpson 1/3]")
        print(BOLD + "3 - Polinômio de substituição de grau 3 [Regra de Simpson 3/8]")
        print(BOLD + "4 - Polinômio de substituição de grau 4")
        print(BOLD + "0 - Sair do programa")
        methodIntegration = input(RESET +'Com qual polinômio você deseja integrar? ')
        methodIntegration = int(methodIntegration)
        if(methodIntegration == 1):
            grau1 = newtonCotes.funcao_geral_integracao(a, b, epson, "fechada1")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grau1[1])
            print(BOLD + "      Interações: " , grau1[0])
            print(BOLD + "     --------------------------------")
        elif(methodIntegration == 2):
            grau2 = newtonCotes.funcao_geral_integracao(a, b, epson, "fechada2")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grau2[1])
            print(BOLD + "      Interações: " , grau2[0])
            print(BOLD + "     --------------------------------")
        elif(methodIntegration == 3):
            grau3 = newtonCotes.funcao_geral_integracao(a, b, epson, "fechada3")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grau3[1])
            print(BOLD + "      Interações: " , grau3[0])
            print(BOLD + "     --------------------------------")
        elif(methodIntegration == 4):
            grau4 = newtonCotes.funcao_geral_integracao(a, b, epson, "fechada4")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grau4[1])
            print(BOLD + "      Interações: " , grau4[0])
            print(BOLD + "     --------------------------------")
    elif(approach==2):
        print(MARG + "\n              Abordagem fechada")
        print(BOLD + "1 - Polinômio de substituição de grau 1 [Regra do Trapézio Aberta]")
        print(BOLD + "2 - Polinômio de substituição de grau 2 [Fórmula de Milne]")
        print(BOLD + "3 - Polinômio de substituição de grau 3")
        print(BOLD + "4 - Polinômio de substituição de grau 4")
        print(BOLD + "0 - Sair do programa")
        methodIntegration = input(RESET +'Com qual polinômio você deseja integrar? ')
        methodIntegration = int(methodIntegration)
        if(methodIntegration == 1):
            grauAberta1 = newtonCotes.funcao_geral_integracao(a, b, epson, "aberta1")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grauAberta1[1])
            print(BOLD + "      Interações: " , grauAberta1[0])
            print(BOLD + "     --------------------------------")
        elif(methodIntegration == 2):
            grauAberta2 = newtonCotes.funcao_geral_integracao(a, b, epson, "aberta2")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grauAberta2[1])
            print(BOLD + "      Interações: " , grauAberta2[0])
            print(BOLD + "     --------------------------------")
        elif(methodIntegration == 3):
            grauAberta3 = newtonCotes.funcao_geral_integracao(a, b, epson, "aberta3")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grauAberta3[1])
            print(BOLD + "      Interações: " , grauAberta3[0])
            print(BOLD + "     --------------------------------")
        elif(methodIntegration == 4):
            grauAberta4 = newtonCotes.funcao_geral_integracao(a, b, epson, "aberta4")
            print(BOLD + "\n     --------------------------------")
            print(BOLD + "      Resultado: " , grauAberta4[1])
            print(BOLD + "      Interações: " , grauAberta4[0])
            print(BOLD + "     --------------------------------")
    if(approach==0):
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


    

