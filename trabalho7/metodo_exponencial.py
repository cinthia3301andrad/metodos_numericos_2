from newton_cotes import funcao_geral_integracao

def metodo_exponencial(a, b, epson, f , f_type_exponencial):
    c = 1
    interacoes = 0
    resultadoAnterior = 0
    resultado = 0
    valorMaxC = 0.01
    new_f = f_type_exponencial(f, a, b)
    while True:
        interacoes += 1
        integral = 0
        integral = funcao_geral_integracao(-c, c, epson, new_f)
        c *= 1.1
        resultadoAnterior = resultado
        resultado = integral
        erro = abs(resultadoAnterior - resultado)
        if (erro < valorMaxC): 
            break
    print(c)
    return interacoes, resultado
