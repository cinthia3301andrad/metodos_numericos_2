
class metodo_preditor_corretor:

    def __init__(self, delta_t):
        self.v0 = 5.0 
        self.y0 = 200.0 
        self.k = 0.25 
        self.m = 2 
        self.g = 10 
        self.delta_t = delta_t


    def pontos_criticos(self):
        tempo = 0.0 
        v_ant = self.v0 
        y_ant = self.y0 
        y_atual = y_ant

        estados_ant = self.inicializacao()
       

        while(y_atual > 0): #critério de parada
            v_atual, y_atual = self.PredicaoCorrecao(estados_ant)
            tempo = tempo + self.delta_t

            if(v_atual*v_ant < 0): 
                if(y_ant > y_atual):
                    y_alt_max = y_ant 
                    t_alt_max = tempo - self.delta_t 
                else:
                    y_alt_max = y_atual 
                    t_alt_max = tempo 
            
            if(y_atual*y_ant < 0): 
                v_mar = v_ant 
                t_mar = tempo - self.delta_t 
            aux  = estados_ant[2:]
            aux.append(v_atual)
            aux.append(y_atual)
            estados_ant = aux

            v_ant = v_atual
            y_ant = y_atual
        
        return y_alt_max, t_alt_max, v_mar, t_mar


    def PredicaoCorrecao(self, estados_ant):
        auxiliar1 = self.auxiliar1(estados_ant[0]) 
        auxiliar2 = self.auxiliar1(estados_ant[2]) 
        auxiliar3 = self.auxiliar1(estados_ant[4]) 
        auxiliar4 = self.auxiliar1(estados_ant[6]) 
#fase de predição
        predicao = [0] * 2

        predicao[0] = estados_ant[6] + (self.delta_t/24)*(-9*auxiliar1[0] + 33*auxiliar2[0] - 59*auxiliar3[0] + 55*auxiliar4[0])#y4, usando o y3 pelo metodo explicito
        predicao[1] = estados_ant[7] + (self.delta_t/24)*(-9*auxiliar1[1] + 33*auxiliar2[1] - 59*auxiliar3[1] + 55*auxiliar4[1])
#fase de correção
        correcao = [0] * 2
        auxiliar_pred = self.auxiliar1(predicao[0]) 

        correcao[0] = estados_ant[6] + (self.delta_t/24)*(auxiliar2[0] - 5*auxiliar3[0] + 19*auxiliar4[0] + 9*auxiliar_pred[0])
        correcao[1] = estados_ant[7] + (self.delta_t/24)*(auxiliar2[1] - 5*auxiliar3[1] + 19*auxiliar4[1] + 9*auxiliar_pred[1])

        return correcao[0], correcao[1]

    def inicializacao(self):
        v_ant = self.v0
        y_ant = self.y0

        estados = self.sol_aproximada(v_ant, y_ant)

        return estados


    def auxiliar1(self, v_ant):
        result1 = [0] * 2 

        result1[0] = -self.g - ((self.k/self.m)*v_ant)
        result1[1] = v_ant

        return result1

    
    def auxiliar2(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)

        v_aux2 = v_ant + (self.delta_t/2)*auxiliar1[0]

        result2 = self.auxiliar1(v_aux2) 

        return result2

    def auxiliar3(self, v_ant):
        auxiliar2 = self.auxiliar2(v_ant)

        v_aux3 = v_ant + (self.delta_t/2)*auxiliar2[0]

        result3 = self.auxiliar1(v_aux3) 
        return result3

    def auxiliar4(self, v_ant):
        auxiliar3 = self.auxiliar3(v_ant)

        v_aux4 = v_ant + self.delta_t*auxiliar3[0]

        result4 = self.auxiliar1(v_aux4)

        return result4

    def sol_aproximada(self, v_ant, y_ant):
        estados = [0] * 8

        estados[0] = v_ant
        estados[1] = y_ant

        i=1
        while(i < 4):
            #precisa de 4 passos pelo metodo de runge kutta
            auxiliar1 = self.auxiliar1(v_ant)
            auxiliar2 = self.auxiliar2(v_ant)
            auxiliar3 = self.auxiliar3(v_ant)
            auxiliar4 = self.auxiliar4(v_ant)

            estados[i*2] = v_ant + (self.delta_t/6)*(auxiliar1[0] + 2*auxiliar2[0] + 2*auxiliar3[0] + auxiliar4[0])#metodo explicito de ordem 4
            estados[(i*2)+1] = y_ant + (self.delta_t/6)*(auxiliar1[1] + 2*auxiliar2[1] + 2*auxiliar3[1] + auxiliar4[1])

            v_ant = estados[i*2]
            y_ant = estados[(i*2)+1]
            
            i = i + 1

        return estados