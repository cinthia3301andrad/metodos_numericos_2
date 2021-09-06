import metodo_exponencial
import math

def integral_problema_1(x):
    return 1/(math.pow(x, 2) ** (1/3))


def function_soluction_1(f, a_origin, b_origin):#aqui ja retona a função vezes a derivada
    x_s = lambda s: ((a_origin+b_origin)/2)+(((b_origin-a_origin)/2)*math.tanh(s)) 
    dx_s = lambda s: (((b_origin-a_origin) / 2) * (1/(math.pow(math.cosh(s), 2))))
    return lambda s: f(x_s(s))*dx_s(s)
    
def integral_problema_2(x):
    return 1/math.sqrt(4-math.pow(x,2))


def function_soluction_2(f, a_origin, b_origin):
    x_s = lambda s: (((a_origin+b_origin)/2)+((b_origin-a_origin)/2)*math.tanh(math.pi/2*math.sinh(s))) 
    dx_s = lambda s: ((b_origin-a_origin)/2) * ((math.pi * math.cosh(s)) / (2*(math.cosh(math.pi/2 * math.sinh(s))**2)))
    return lambda s: f(x_s(s))*dx_s(s)


problema_1 = metodo_exponencial.metodo_exponencial(-1, 0, 0.000001, integral_problema_1,function_soluction_1 )
problema_2 = metodo_exponencial.metodo_exponencial(-2, 0, 0.000001, integral_problema_2, function_soluction_2 )
print("Problema 1", problema_1[1]*2)
print("Problema 2", problema_2[1])

