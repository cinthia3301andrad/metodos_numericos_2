import math
def function(x): #Calcula o quadrado
    return math.pow(x,2)

def f(x): #função para ser utilizada nos métodos
    formula = math.sin(2*x) + 4*function(x) + 3*x
    resultadoFinal = function(formula)

    return resultadoFinal

def x(sk, xi, xf): #Cálculo do x(sk)
    x_final = (xi + xf) / 2 + ((xf - xi) / 2) * sk
    return x_final

def gauss_Legendre_2pontos():
    s = math.sqrt(1/3)
    raizes_s = [s, -s]
    w = 1
    pesos_w = [w, w]
    # return teste(pesos_w, raizes_s)
    # return raizes_s
    funcao_geral_integracao(2, pesos_w, raizes_s, 0.0001, 0, 1)


def funcao_geral_integracao(qtd_pontosInterpolacao, pesos_w, raizes_s, epson, a, b):
    delta = 0
    xi = 0
    xf = 0
    erro = 0
   
    resultadoAnterior = 0
    resultado = 0
    integral = 0
    N = 1

    while True:
        resultadoAnterior = resultado
        resultado = 0
        interacoes = 0
        
        delta = (b - a) / N
        for i in range(N):
            integral = resultado
            xi = a + i*delta
            xf = xi + delta
            somatorio = 0
            for k in range(qtd_pontosInterpolacao):
                somatorio += (pesos_w[k] * f(x(raizes_s[k], xi, xf)))
            resultado  += ((xf - xi) / 2) * somatorio
            interacoes += 1
          
        N = N*2
        resultadoAnterior = integral
        print("ENTROU NO FOR", resultado, N)
        erro = abs((resultadoAnterior - resultado)/2)
        print("ERRO", erro, interacoes)
        print("============================================")
        if (erro < epson): 
            
            break
    
    return interacoes, resultado

def teste(pesos_w, raizes_s):
    somatorio = 0
    for k in range(2):
        somatorio += (pesos_w[k] * f(x(raizes_s[k], 0, 1)))
        resultado  = ((1 - 0) / 2) * somatorio
        print("somatoriooo", resultado)