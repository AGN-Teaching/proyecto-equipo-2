from cuenta import Cuenta 

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
        
    def AgregarCuenta(self, cuenta): # verifica si se puede agregar una cuenta, de ser asi la agrega
        if self.__numero_de_cuentas_almacenadas < self.__numero_de_cuentas_permitidas:
            self.__cuentas_plan.append(cuenta)  # Agregar la cuenta a la lista
            self.__numero_de_cuentas_almacenadas += 1  # Incrementar el contador de cuentas almacenadas
            print("¡Cuenta creada exitosamente!")
            print()
        else:
            print("Se alcanzó el límite de cuentas, no se puede crear una cuenta nueva")
            print()

    def CrearCuenta(self): # crea cuenta y hace uso del metodo AgregarCuenta
        nombre_cuenta_nueva = input("Ingresa el nombre de la cuenta nueva: ")  # Solicita el nombre de la cuenta
        print()

        if len(self.__cuentas_plan) > 0:  # Verifica si el cliente ya tiene cuentas
            cuenta_existe = False
            for cuenta in self.__cuentas_plan:
                nombre_cuenta_almacenada = cuenta.getNombre()
                if nombre_cuenta_almacenada.lower() == nombre_cuenta_nueva.lower():
                    cuenta_existe = True
            if cuenta_existe:
                print("Ya hay una cuenta registrada con ese nombre")
                print()
            else:
                if self.__paga:  # Comprueba si el cliente tiene un plan de pago activo
                    cuenta_nueva = Cuenta(nombre_cuenta_nueva)
                    self.AgregarCuenta(cuenta_nueva)
                else:
                    cuenta_nueva = Cuenta(nombre_cuenta_nueva)
                    self.AgregarCuenta(cuenta_nueva)
        else:
            if self.__paga:
                cuenta_nueva = Cuenta(nombre_cuenta_nueva)
                self.AgregarCuenta(cuenta_nueva)
            else:
                cuenta_nueva = Cuenta(nombre_cuenta_nueva)
                self.AgregarCuenta(cuenta_nueva)
        
        # Método para agregar una cuenta a las cuentas del cliente
        

    def EliminarCuenta(self):
        hay_cuentas = False
        if len(self.__cuentas_plan) > 0:
            hay_cuentas = True
        else:
            print()
            print("No hay cuentas existentes")
            print()
        
        if hay_cuentas:
            print("Perfiles creados: ")
            for cuenta in self.__cuentas_plan:
                nombre_cuenta = cuenta.getNombre()
                print(nombre_cuenta)
            print()
            nombre_cuenta_a_borrar = str(input("Ingresa el nombre de la cuenta que desea borrar: "))
            cuenta_borrada = False
            for cuenta in self.__cuentas_plan:
                if cuenta.getNombre().lower() == nombre_cuenta_a_borrar.lower():
                    self.__cuentas_plan.remove(cuenta)  # Eliminar la cuenta de la lista
                    cuenta_borrada = True
                    self.__numero_de_cuentas_almacenadas = self.__numero_de_cuentas_almacenadas - 1
            if cuenta_borrada:
                print("¡Cuenta borrada!")
                print()
            else:
                print("La cuenta no se encontro")
                print()
        
