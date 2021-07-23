import math

def funcaoIntegrada_simples(a, b , x, type_func,a_origin, b_origin): #mudança de variavel para exeponencial simples
    newX = ((a_origin+b_origin)/2)+(((b_origin-a_origin)/2)*math.tanh(x)) 
    if(type_func == 1):
        resultado = (math.pow(newX, 2) ** (1/3)) * ( ((b_origin-a_origin) / 2) * (1/(math.pow(math.cosh(x), 2))))
    else:
        resultado  = (1/math.pow(4-(newX*newX), 2)) * ( ((b_origin-a_origin) / 2) * (1/(math.pow(math.cosh(x), 2))))
    return resultado
    
def funcaoIntegrada_dupla(a, b, x, type_func,a_origin, b_origin ):#mudança de variavel para exponencial dupla
    newX = (((a_origin+b_origin)/2)+((b_origin-a_origin)/2)*math.tanh(math.pi/2*math.sinh(x))) 
    if(type_func == 1):
        resultado = (math.pow(newX, 2) ** (1/3)) * ((b_origin-a_origin)/2) * ((math.pi/2)*math.cosh(x)/(math.cosh(math.pi/2*math.sinh(x)))**2)
    else:
        resultado = (1/math.pow(4-(newX*newX), 2)) * ((b_origin-a_origin)/2) * ((math.pi/2)*math.cosh(x)/(math.cosh(math.pi/2*math.sinh(x)))**2)
        
    return resultado
# a, b, epson, tipo == duplo ou simples, type_func = 1 ou 2
def funcao_geral_integracao(a, b, epson, tipo, type_func, a_origin, b_origin):
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
            integral += formula_4_aberta(Xi, Xf, tipo, type_func, a_origin, b_origin)
            print(integral, "ok")
           
        N = N*2
        resultadoAnterior = resultado
        resultado = integral
        erro = abs(resultadoAnterior - resultado)
       # print(a, b, type_func, erro, "FODASE")
        if (erro < epson): 
            break
    
    return  resultado

def formula_4_aberta(Xi, Xf, tipo, type_func, a_origin, b_origin ): #GRAU 4
    h = (Xf-Xi)/6
    if(tipo == "duplo"):
        return ((6*h)/20)*(11*funcaoIntegrada_simples(Xi, Xf, Xi+h,type_func,a_origin, b_origin) - 
                    14*funcaoIntegrada_simples(Xi, Xf, Xi+2*h, type_func,a_origin, b_origin) + 26*funcaoIntegrada_simples(Xi, Xf, Xi+3*h, type_func, a_origin, b_origin) - 
                    14*funcaoIntegrada_simples(Xi, Xf, Xi+4*h, type_func,a_origin, b_origin)+ 11*funcaoIntegrada_simples(Xi, Xf,Xi+5*h,type_func,a_origin, b_origin))
    elif(tipo == "simples"): 
        return ((6*h)/20)*(11*funcaoIntegrada_dupla(Xi, Xf, Xi+h, type_func,a_origin, b_origin) - 
                    14*funcaoIntegrada_dupla(Xi, Xf, Xi+2*h, type_func,a_origin, b_origin) + 26*funcaoIntegrada_dupla(Xi, Xf, Xi+3*h, type_func,a_origin, b_origin) - 
                    14*funcaoIntegrada_dupla(Xi, Xf, Xi+4*h, type_func,a_origin, b_origin)+ 11*funcaoIntegrada_dupla(Xi, Xf,Xi+5*h, type_func,a_origin, b_origin ))