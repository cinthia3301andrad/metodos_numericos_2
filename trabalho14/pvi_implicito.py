class metodo_runge_kutta:
    
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

        while(y_atual > 0): 
            v_atual, y_atual = self.sol_aproximada(v_ant, y_ant)
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

            v_ant = v_atual
            y_ant = y_atual
        
        return y_alt_max, t_alt_max, v_mar, t_mar

    
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
        auxiliar1 = self.auxiliar1(v_ant)
        auxiliar2 = self.auxiliar2(v_ant)

        v_aux3 = v_ant + self.delta_t*(-auxiliar1[0] + 2*auxiliar2[0])

        result3 = self.auxiliar1(v_aux3) 

        return result3

    
    def sol_aproximada(self, v_ant, y_ant):
        auxiliar1 = self.auxiliar1(v_ant)
        auxiliar2 = self.auxiliar2(v_ant)
        auxiliar3 = self.auxiliar3(v_ant)

        result = [0] * 2 

 
        result[0] = v_ant + self.delta_t*((auxiliar1[0] + 4*auxiliar2[0] + auxiliar3[0])/6)
        result[1] = y_ant + self.delta_t*((auxiliar1[1] + 4*auxiliar2[1] + auxiliar3[1])/6)

        return result[0], result[1] 