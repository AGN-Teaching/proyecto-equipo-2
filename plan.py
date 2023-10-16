# Clase Plan
class Plan:
    # Metodo constructor
    def __init__(self):
        self.__planes = ["Gratuito", "Individuial", "Estudiante", "Duo", "Familiar"] # lista que guarda los tipos de planes 
    
    # Metodo que proporciona la lista de planes 
    def getPlanes(self):
        return self.__planes

    # Asigna el plan usando el numero para buscar en lista 
    def AsignarPlan(self, numero):
        if numero == 1:
            plan = self.__planes[0]
        elif numero == 2:
            plan = self.__planes[1]
        elif numero == 3:
            plan = self.__planes[2]
        elif numero == 4:
            plan = self.__planes[3]
        elif numero == 5:
            plan = self.__planes[4]
        return plan
        
    # Asigna el numero de cuentas usando el numero para buscar en lista 
    def AsignarNumeroCuentas(self, numero):
        if numero == 1:
            num_cuentas = 1
        elif numero == 2:
            num_cuentas = 1
        elif numero == 3:
            num_cuentas = 1
        elif numero == 4:
            num_cuentas = 2
        elif numero == 5:
            num_cuentas = 6
        return num_cuentas
            
    # Asigna si el plan es de paga usando el numero para buscar en lista 
    def AsignarPaga(self, numero):
        if numero == 1:
            paga = False
        elif numero == 2:
            paga = True
        elif numero == 3:
            paga = True
        elif numero == 4:
            paga = True
        elif numero == 5:
            paga = True
        return paga