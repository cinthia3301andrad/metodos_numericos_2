import newtonCotes

grau1 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "fechada1")
grau2 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "fechada2")
grau3 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "fechada3")
grau4 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "fechada4")
grauAberta1 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "aberta1")
grauAberta2 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "aberta2")
grauAberta3 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "aberta3")
grauAberta4 = newtonCotes.funcao_geral_integracao(0, 1, 0.0000001, "aberta4")
print("---------FECHADA---------")
print(grau1)
print(grau2)
print(grau3)
print(grau4)
print("--------ABERTA----------")
print(grauAberta1)
print(grauAberta2)
print(grauAberta3)
print(grauAberta4)