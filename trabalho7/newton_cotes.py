def funcao_geral_integracao(a, b, epson, f):
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
            integral += formula_4_aberta(Xi, Xf, f)
           
        N = N*2
        resultadoAnterior = resultado
        resultado = integral
        erro = abs(resultadoAnterior - resultado)
      
        if (erro < epson): 
            break
    
    return  resultado

def formula_4_aberta(Xi, Xf, f ): #GRAU 4
    h = (Xf-Xi)/6
    return ((6*h)/20)*(11*f(Xi+h)- 14*f(Xi+2*h) + 26*f( Xi+3*h) - 14*f(Xi+4*h)+ 11*f(Xi+5*h))
