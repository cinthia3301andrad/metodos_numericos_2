from math import sqrt
   
def Potencia_Regular(matriz, vetor, epson): # step 1
    tam = len(vetor)
    vk_novo = []
    vk_velho = []
    erro = 10
    lambda1_novo = 0   # step 2
    for i in range(tam):   # step 3
        vk_novo.append(vetor[i])
        vk_velho.append(0)
        
    while(erro > epson):
        lambda1_velho = lambda1_novo   # step 4
        vk_velho = vk_novo   # step 5
        x1_velho = normalizacao(vk_velho, tam)   # step 6
        vk_novo = matriz_x_vetor(x1_velho, matriz)   # step 7
        lambda1_novo = vetor_x_vetor(x1_velho, vk_novo, tam)   # step 8 aqui multiplicamos o novo vetor pelo vetor old normalizado e obtemos o lambda
        erro = abs((lambda1_novo-lambda1_velho)/lambda1_novo)   # step 9

    return [lambda1_novo, x1_velho]

def normalizacao(v, tam):
    aux = []
    s = sqrt(vetor_x_vetor(v, v, tam)) #aqui tiramos a norma do vetor: <3, 4> = raizQ de 3²+4² = 5
    for i in range(tam):
        aux.append(v[i]/s)
    return aux #<3/5, 4/5>

def matriz_x_vetor(v, matriz):
    x = []
    tam = len(matriz)
  
    for i in range(tam):
        s = vetor_x_vetor(matriz[i], v, tam) #faço a multiplicação da matriz pelo vetor e coloco no x
        x.append(s)
    return x

def vetor_x_vetor(v1, v2, tam):
    s = 0
    for i in range(tam):
        s = s + v1[i]*v2[i]
    
    return s