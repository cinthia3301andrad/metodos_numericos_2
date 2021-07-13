import math
def function(x): #Calcula o quadrado
    return math.pow(x,2)

def f(x):
    e = math.pow(math.e,-function(x))
    formula= (math.sin(2*x) + 4*function(x) + 3*x)
    resultadoFinal = function(formula)

    return resultadoFinal

def gauss_Hermite_2pontos(): #Solução de Gauss-Hermite com 2 pontos.
    s = (1/math.sqrt(2))
    
    raizes_s = [-s, s]
   
    w = math.sqrt(math.pi)/2
  
    pesos_w = [w, w]
  
    return funcao_geral_integracao(2, pesos_w, raizes_s)

def gauss_Hermite_3pontos(): #Solução de Gauss-Hermite com 3 pontos.
    s = math.sqrt(3/2)
   
    raizes_s = [-s, 0, s]
    
    w = math.sqrt(math.pi)/6
 
    w_2 = 1.1816359
  
    pesos_w = [w, w_2, w]
    print("OS PESOS", pesos_w)
   
    return funcao_geral_integracao(3, pesos_w, raizes_s)

def gauss_Hermite_4pontos(): #Solução de Gauss-Hermite com 4 pontos.
    s = math.sqrt(3+math.sqrt(6))/math.sqrt(2)
    s_2 = math.sqrt(3-math.sqrt(6))/math.sqrt(2)
    raizes_s = [-s, -s_2, s_2, s]
    w = 0.08131283545
    w_2 = 0.80491409
    pesos_w = [w, w_2, w_2, w]

    return funcao_geral_integracao(4, pesos_w, raizes_s)

def funcao_geral_integracao(qtd_grau, pesos_w, raizes_s):
    #definindo as variaveis
    somatorio = 0
    for k in range(qtd_grau):
        somatorio += (pesos_w[k] * f(raizes_s[k]))
  
    return somatorio


teste = gauss_Hermite_2pontos()
teste2 = gauss_Hermite_3pontos()
teste3 = gauss_Hermite_4pontos()
print(teste, teste2, teste3)
