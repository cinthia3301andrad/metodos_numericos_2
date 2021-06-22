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
    resultado = 0
    interacoes = 0
    N = 2

    while True:
        interacoes += 1
        delta = (b-a)/N
        integral = 0
        for i in range(N):
            Xi = a + i*delta
            Xf = Xi + delta
            if(tipo=="fechada1"):
                integral += formula_1_fechada(Xi, Xf)
            elif(tipo=="fechada2"):
                integral += formula_2_fechada(Xi, Xf)
            elif(tipo=="fechada3"):
                integral += formula_3_fechada(Xi, Xf)
            elif(tipo=="fechada4"):
                integral += formula_4_fechada(Xi, Xf)
            elif(tipo=="aberta1"):
                integral += formula_1_aberta(Xi, Xf)
            elif(tipo=="aberta2"):
                integral += formula_2_aberta(Xi, Xf)
            elif(tipo=="aberta3"):
                integral += formula_3_aberta(Xi, Xf)
            elif(tipo=="aberta4"):
                integral += formula_4_aberta(Xi, Xf)
        N = N*2
        resultadoAnterior = resultado
        resultado = integral
        erro = abs(resultadoAnterior - resultado)
        
        if (erro < epson): 
            break
    
    return interacoes, resultado

def formula_1_fechada(Xi, Xf): #GRAU 1
    return (Xf-Xi)/2*(funcaoIntegrada(Xi)+funcaoIntegrada(Xf))
    
def formula_2_fechada(Xi, Xf): #GRAU 2
    h = (Xf-Xi)/2
    return (h)/3*(funcaoIntegrada(Xi) + 4*funcaoIntegrada(Xi+h) + funcaoIntegrada(Xi+2*h))

def formula_3_fechada(Xi, Xf): #GRAU 3
    h = (Xf-Xi)/3
    return (3*(h)/8)*(funcaoIntegrada(Xi) + 3*funcaoIntegrada(Xi+h) + 3*funcaoIntegrada(Xi+2*h) +funcaoIntegrada(Xi+3*h))

def formula_4_fechada(Xi, Xf): #GRAU 4 
    h = (Xf-Xi)/4
    return (2*(h)/45)*(7*funcaoIntegrada(Xi) + 32*funcaoIntegrada(Xi+h) + 12*funcaoIntegrada(Xi+2*h) +32*funcaoIntegrada(Xi+3*h)+7*funcaoIntegrada(Xi+4*h))
        
def formula_1_aberta(Xi, Xf): #GRAU 1
    h = (Xf-Xi)/3
    return (Xf-Xi)/2*(funcaoIntegrada(Xi+h)+funcaoIntegrada(Xi+2*h))

def formula_2_aberta(Xi, Xf): #GRAU 2
    h = (Xf-Xi)/4
    return ((4*h)/3)*(2*funcaoIntegrada(Xi+h) - funcaoIntegrada(Xi+2*h) + 2*funcaoIntegrada(Xi+3*h))   

def formula_3_aberta(Xi, Xf): #GRAU 3
    h = (Xf-Xi)/5
    return ((5*h)/24)*(11*funcaoIntegrada(Xi+h) + funcaoIntegrada(Xi+2*h) + funcaoIntegrada(Xi+3*h) + 11*funcaoIntegrada(Xi+4*h))

def formula_4_aberta(Xi, Xf): #GRAU 4
    h = (Xf-Xi)/6
    return ((6*h)/20)*(11*funcaoIntegrada(Xi+h) - 14*funcaoIntegrada(Xi+2*h) + 26*funcaoIntegrada(Xi+3*h) - 14*funcaoIntegrada(Xi+4*h)+ 11*funcaoIntegrada(Xi+5*h))