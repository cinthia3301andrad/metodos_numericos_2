import math

def funcao(x):
    equacao = 2.71828**(3*x)+4*(x**2)
    resposta = math.sqrt(equacao)
    return resposta

def derivada_segunda(x, delta_x):
    resposta = (1/delta_x**2)*((-1/12)*funcao(x+2*delta_x)+4/3*funcao(x+delta_x)-5/2*funcao(x)+4/3*funcao(x-delta_x)-1/12*funcao(x-2*delta_x))
    return resposta

print("DERIVADA SEGUNDA")

resposta_def_05 = derivada_segunda(2, 0.5)
resposta_def_25 = derivada_segunda(2, 0.25)
resposta_def_125 = derivada_segunda(2, 0.125)
resposta_def_0625 = derivada_segunda(2, 0.0625)
resposta_def_03125 = derivada_segunda(2, 0.03125)
print("derivada no ponto 2, delta 0.5:")
print(resposta_def_05)
print("derivada no ponto 2, delta 0.25:")
print(resposta_def_25)
print("derivada no ponto 2, delta 0.125:")
print(resposta_def_125)
print("derivada no ponto 2, delta 0.0625:")
print(resposta_def_0625)
print("derivada no ponto 2, delta 0.03125:")
print(resposta_def_03125)
