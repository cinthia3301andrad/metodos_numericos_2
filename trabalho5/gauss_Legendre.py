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

def gauss_Legendre_2pontos(a_inicio, b_fim, erro_estimado): #Solução de Gauss-Legendre com 2 pontos.
    s = math.sqrt(1/3)
    raizes_s = [s, -s]
    w = 1
    pesos_w = [w, w]
    # return teste(pesos_w, raizes_s)

    return funcao_geral_integracao(2, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def funcao_geral_integracao(qtd_pontosInterpolacao, pesos_w, raizes_s, epson, a, b):
    #definindo as variaveis
    delta = 0
    xi = 0
    xf = 0
    erro = 0 #erro inicial para comparar com o epson dado
    resultadoAnterior = 0
    resultado = 0
    resultado_aux = 0 #precisamos desse para guardar o resultado anterior
    N = 1

    while True:
        resultadoAnterior = resultado
        resultado_aux = resultado
        resultado = 0
        interacoes = 0
        
        delta = (b - a) / N
        for i in range(N): # aqui vamos realizar o método de gauss por partição, começando com 1 depois N*2
            xi = a + i*delta
            xf = xi + delta
            somatorio = 0
            for k in range(qtd_pontosInterpolacao):
                somatorio += (pesos_w[k] * f(x(raizes_s[k], xi, xf))) #aqui fazemos o somatorio do próprio método de gauss com a quantidade de pontos especifico
            resultado  += ((xf - xi) / 2) * somatorio # interamos o resultado
            interacoes += 1
          
        N = N*2
        resultadoAnterior = resultado_aux
        print("CADA RESULTADO", resultado, resultadoAnterior)
        erro = abs((resultadoAnterior - resultado)/2)
        print("ERRO", erro, interacoes)
        print("============================================")
        if (erro < epson): 
            break
    print("FIM", resultado, interacoes)
    return interacoes, resultado

def teste(pesos_w, raizes_s):
    somatorio = 0
    for k in range(2):
        somatorio += (pesos_w[k] * f(x(raizes_s[k], 0, 1)))
        resultado  = ((1 - 0) / 2) * somatorio
        print("somatoriooo", resultado)