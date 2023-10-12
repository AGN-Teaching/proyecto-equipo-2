class Cliente():
    def __init__(self, nombre, tipo_plan, numero_cuentas_permitidas, paga):
        self.__numero_de_cuentas_almacenadas = 0
        self.__numero_de_cuentas_permitidas = numero_cuentas_permitidas
        self.__nombre = nombre
        self.__tipo_plan = tipo_plan
        self.__paga = paga
        self.__cuentas_plan = []
        
    def getNumeroCuentas(self):
        return self.__numero_de_cuentas_almacenadas
    
    def getNumeroCuentasPermitidas(self):
        return self.__numero_de_cuentas_permitidas
    
    def getNombre(self):
        return self.__nombre
    
    def getTipoPlan(self):
        return self.__tipo_plan
    
    def getPaga(self):
        return self.__paga
        
    def getCuentas(self):
        return self.__cuentas_plan
    
    def setPaga(self, paga):
        self.__paga = paga
        
    def AgregarCuenta(self, cuenta):
        self.__cuentas_plan.append(cuenta)
        self.__numero_de_cuentas_almacenadas = self.__numero_de_cuentas_almacenadas + 1
        
    def EliminarCuenta(self, cuenta):
        self.__cuentas_plan.remove(cuenta)