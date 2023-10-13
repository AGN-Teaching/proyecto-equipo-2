class Cliente():
    def __init__(self, nombre, tipo_plan, numero_cuentas_permitidas, paga):
        # Constructor: inicializa la información del cliente y su plan
        self.__numero_de_cuentas_almacenadas = 0  # Número de cuentas almacenadas actualmente
        self.__numero_de_cuentas_permitidas = numero_cuentas_permitidas  # Número máximo de cuentas permitidas
        self.__nombre = nombre  # Nombre del cliente
        self.__tipo_plan = tipo_plan  # Tipo de plan del cliente
        self.__paga = paga  # Indica si el cliente paga por el servicio
        self.__cuentas_plan = []  # Almacena las cuentas asociadas al cliente

    def getNumeroCuentas(self):
        # Método para obtener el número de cuentas almacenadas
        return self.__numero_de_cuentas_almacenadas

    def getNumeroCuentasPermitidas(self):
        # Método para obtener el número máximo de cuentas permitidas en el plan
        return self.__numero_de_cuentas_permitidas

    def getNombre(self):
        # Método para obtener el nombre del cliente
        return self.__nombre

    def getTipoPlan(self):
        # Método para obtener el tipo de plan del cliente
        return self.__tipo_plan

    def getPaga(self):
        # Método para determinar si el cliente paga por el servicio
        return self.__paga

    def getCuentas(self):
        # Método para obtener la lista de cuentas asociadas al cliente
        return self.__cuentas_plan

    def setPaga(self, paga):
        # Método para actualizar el estado de pago del cliente
        self.__paga = paga

    def AgregarCuenta(self, cuenta):
        # Método para agregar una cuenta a las cuentas del cliente
        if self.__numero_de_cuentas_almacenadas < self.__numero_de_cuentas_permitidas:
            self.__cuentas_plan.append(cuenta)  # Agregar la cuenta a la lista
            self.__numero_de_cuentas_almacenadas += 1  # Incrementar el contador de cuentas almacenadas
            print("¡Cuenta creada exitosamente!")
            print()
        else:
            print("Se alcanzó el límite de cuentas, no se puede crear una cuenta nueva")
            print()

    def EliminarCuenta(self, cuenta):
        # Método para eliminar una cuenta de las cuentas del cliente
        self.__cuentas_plan.remove(cuenta)  # Eliminar la cuenta de la lista
