import math
def function(x): #Calcula o quadrado
    return math.pow(x,2)

def funcaoIntegrada(x):
    formula= math.sin(2*x) + 4*function(x) + 3*x
    resultadoFinal = function(formula)

    return resultadoFinal

# a, b, epson
def funcao_geral_integracao(a, b, epson, tipo):
    delta = 0
    Xi = 0
    erro = 0
    resultadoAnterior = 0
    interacoes = 0
    N = 1

    while True:
        delta = (b-a)/N
        resultado = 0
        for i in range(0, int(N)):
            Xi = a + i*delta
            Xf = Xi + delta
            if(tipo=="fechada1"):
                resultado += formula_1_fechada(delta, Xi)
            elif(tipo=="fechada2"):
                h = (b-a)/2
                resultado += formula_2_fechada(h, Xi)
            elif(tipo=="fechada3"):
                h = (b-a)/3
                resultado += formula_3_fechada(h, Xi)
            elif(tipo=="fechada4"):
                h = (b-a)/4
                resultado += formula_4_fechada(h, Xi)
            elif(tipo=="aberta1"):
                h = (b-a)/3
                resultado += formula_1_aberta(delta, h , Xi)
            elif(tipo=="aberta2"):
                h = (b-a)/4
                resultado += formula_2_aberta(h, Xi)
            elif(tipo=="aberta3"):
                h = (b-a)/5
                resultado += formula_3_aberta(h, Xi)
            elif(tipo=="aberta4"):
                h = (b-a)/6
                resultado += formula_4_aberta(h, Xi)
        erro = abs((resultado - resultadoAnterior)/ resultado)
        resultadoAnterior = resultado
        interacoes += 1
        N = N*2
        if (erro > epson): break
    
    return interacoes, resultado

def formula_1_fechada(delta, Xi): #GRAU 1
    return (delta)/2*(funcaoIntegrada(Xi)+funcaoIntegrada(Xi+delta))
    
def formula_2_fechada(h, Xi): #GRAU 2
    return (h)/3*(funcaoIntegrada(Xi) + 4*funcaoIntegrada(Xi+h) + funcaoIntegrada(Xi+2*h))

def formula_3_fechada(h, Xi): #GRAU 3
    return (3*(h)/8)*(funcaoIntegrada(Xi) + 3*funcaoIntegrada(Xi+h) + 3*funcaoIntegrada(Xi+2*h) +funcaoIntegrada(Xi+3*h))

def formula_4_fechada(h, Xi): #GRAU 4    
    return (2*(h)/45)*(7*funcaoIntegrada(Xi) + 32*funcaoIntegrada(Xi+h) + 12*funcaoIntegrada(Xi+2*h) +32*funcaoIntegrada(Xi+3*h)+7*funcaoIntegrada(Xi+4*h))
        
def formula_1_aberta(delta, h , Xi): #GRAU 1
    return (delta)/2*(funcaoIntegrada(Xi+h)+funcaoIntegrada(Xi+2*h))

def formula_2_aberta(h, Xi): #GRAU 2
    return ((4*h)/3)*(2*funcaoIntegrada(Xi+h) - funcaoIntegrada(Xi+2*h) + 2*funcaoIntegrada(Xi+3*h))   

def formula_3_aberta(h, Xi): #GRAU 3
    return ((5*h)/24)*(11*funcaoIntegrada(Xi+h) + funcaoIntegrada(Xi+2*h) + funcaoIntegrada(Xi+3*h) + 11*funcaoIntegrada(Xi+4*h))

def formula_4_aberta(h, Xi): #GRAU 4
    return ((6*h)/20)*(11*funcaoIntegrada(Xi+h) - 14*funcaoIntegrada(Xi+2*h) + 26*funcaoIntegrada(Xi+3*h) - 14*funcaoIntegrada(Xi+4*h)+ 11*funcaoIntegrada(Xi+5*h))