import math
def function(x): #Calcula o quadrado
    return math.pow(x,2)

def f(x): #função para ser utilizada nos métodos
    formula = math.sin(2*x) + 4*function(x) + 3*x
    resultadoFinal = function(formula)

    return resultadoFinal

def gauss_Laguerre_2pontos(): #Solução de Gauss-Laguerre com 2 pontos.
    s = 0.5857864376
    s_2 = 3.414213562

    raizes_s = [s, s_2]
    w = 0.8535533905
    w_2 = 0.1464466094
    pesos_w = [w, w_2]

    return funcao_geral_integracao(2, pesos_w, raizes_s)

def gauss_Laguerre_3pontos(): #Solução de Gauss-Laguerre com 3 pontos.
    raizes_s = [0.4157745568, 2.2942803603, 6.2899450829]
 
    pesos_w = [0.7110930099, 0.2785177336, 0.0103892565]

    return funcao_geral_integracao(3, pesos_w, raizes_s)

def gauss_Laguerre_4pontos(): #Solução de Gauss-Laguerre com 4 pontos.
    raizes_s = [0.32254, 1.74576, 4.53662, 9.39507]
 
    pesos_w = [0.60335, 0.35742, 0.03888, 0.00053]

    return funcao_geral_integracao(4, pesos_w, raizes_s)

def funcao_geral_integracao(qtd_grau, pesos_w, raizes_s):
    #definindo as variaveis
    somatorio = 0
    for k in range(qtd_grau):
        somatorio += (pesos_w[k] * f(raizes_s[k]))
    return somatorio

teste = gauss_Laguerre_2pontos()
teste2 = gauss_Laguerre_3pontos()
teste3 = gauss_Laguerre_4pontos()
print(teste, teste2, teste3)
