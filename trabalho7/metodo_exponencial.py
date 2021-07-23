from newton_cotes import funcao_geral_integracao

def metodo_exponencial(a, b, tipo, epson, type_func):
    c = 1
    interacoes = 0
    resultadoAnterior = 0
    resultado = 0
    valorMaxC = 0.000001
    
    while True:
        interacoes += 1
        integral = 0
        integral = funcao_geral_integracao(-c, c, epson, tipo, type_func, a, b)
        print(resultadoAnterior, integral)

        print("entrou")
        c += 1
        resultadoAnterior = resultado
        resultado = integral
        erro = abs(resultadoAnterior - resultado)
        if (erro < valorMaxC): 
            break
    print(c)
    return interacoes, resultado
