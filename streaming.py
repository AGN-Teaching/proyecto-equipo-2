import json
from cuenta_usuario_gratuito import CuentaUsuarioGratuito
from cuenta_usuario_paga import Cuenta_usuario_paga
from cancion import Cancion
from cliente import Cliente

class Streaming:
    
    def __init__(self):
        self.__clientes = []
        self.__catalogo = []
        
    def getClientes(self):
        return self.__clientes
    
    def getCatalogo(self):
        return self.__Clientes
    
    def setNuevoCliente(self, Cliente):
        self.__clientes.append(Cliente)
        
    def CargarCatalogo(self, nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()  # Lee el contenido del archivo
        if contenido:  # Verifica si el archivo no está vacío
            with open(nombre_archivo, "r") as archivo:
                objetos_recuperados = json.load(archivo)  # Carga los objetos desde el archivo JSON
                self.catalogo = []  # Vacia el contenido del catalogo para posteriormente actualizarlo
                for cancion_dict in objetos_recuperados:
                    cancion = Cancion(**cancion_dict)
                    self.__catalogo.append(cancion)
                    # Crea instancias de Cancion        
        else:
            self.catalogo = []  # Si el archivo está vacio, inicializa el catalogo como una lista vacía
    
    def Reproductor(self, cancion, cuenta):
        salir_reproductor = False
        while not salir_reproductor:
            cancion.Reproducir()
            print("Opciones")
            print("1. Agregar a lista de reproduccion")
            print("2. Stop")
            print()
            try:
                opcion = int(input("Ingresa una opcion"))
                print()
                if opcion == 1:
                    cuenta.AgregarCancion(cancion)
                elif opcion == 2:
                    salir_reproductor = True
            except ValueError:
                print("Error: No has ingresado una opcion valida, intenta de nuevo.")

    def MenuCuenta(self, cuenta):
        cuenta_abierta = cuenta
        Salir_menu_cuenta = False
        while not Salir_menu_cuenta:
            print("Menú cuenta")
            print("1. Buscar por Titulo")
            print("2. Buscar por Artista")
            print("3. Buscar por album")
            print("4. Buscar en lista de reproduccion")
            print("5. Crear lista de reproduccion")
            print("6. Cerrar sesion")
            try:
                print()
                opcion = int(input("Ingresa una opcion: "))
                print()
            except ValueError:
                print("Error: No has ingresado un número entero válido.")
                print()
                opcion = 7
                
            if opcion ==1:
                titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                print()
                busqueda_existosa = False
                for cancion in self.__catalogo:
                    titulo = cancion.getTitulo()
                    if titulo_a_buscar.lower() == titulo.lower():
                        cancion_encontrada = cancion
                        busqueda_existosa = True
                    
                if  busqueda_existosa:
                    self.Reproductor(cancion_encontrada, cuenta_abierta)                    
                else:
                    print("El titulo no se encuentra")                   
                
                        
            elif opcion == 2:
                artista_a_buscar = input("Ingresa el artista de la cancion: ")
                print()
                canciones_artista = []
                busqueda_artista_exitosa = False
                for cancion in self.__catalogo:
                    artista = cancion.getArtista()
                    if artista_a_buscar.lower() == artista.lower():
                        canciones_artista.append(cancion)
                        busqueda_artista_exitosa = True
                if busqueda_artista_exitosa:
                    if len(canciones_artista) > 0:
                        print("Canciones disponibles ")
                        for cancion_artista in canciones_artista:
                            titulo = cancion_artista.getTitulo()
                            print(titulo)
                        titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                        print()
                        busqueda_existosa = False
                        for cancion in canciones_artista:
                            titulo = cancion.getTitulo()
                            if titulo_a_buscar.lower() == titulo.lower():
                                cancion_encontrada = cancion
                                busqueda_existosa = True
                            
                        if  busqueda_existosa:
                            self.Reproductor(cancion_encontrada, cuenta_abierta)                    
                        else:
                            print("El titulo no se encuentra")
                else:    
                    print("El Artista no se encontro")    
                                      
            elif opcion == 3:
                album_a_buscar = input("Ingresa el nombre del album: ")
                print()
                canciones_album = []
                busqueda_album_exitosa = False
                for cancion in self.__catalogo:
                    album = cancion.getAlbum()
                    if album_a_buscar.lower() == album.lower():
                        canciones_album.append(cancion)
                        busqueda_album_exitosa = True
                if busqueda_album_exitosa:
                    if len(canciones_album) > 0:
                        print("Canciones disponibles ")
                        for cancion_album in canciones_album:
                            titulo = cancion_album.getTitulo()
                            print(titulo)
                        titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                        print()
                        busqueda_existosa = False
                        for cancion in canciones_album:
                            titulo = cancion.getTitulo()
                            if titulo_a_buscar.lower() == titulo.lower():
                                cancion_encontrada = cancion
                                busqueda_existosa = True
                                
                        if busqueda_existosa:
                            self.Reproductor(cancion_encontrada, cuenta_abierta)
                        else:
                            print("El titulo no se encuentra") 
                else:
                    print("El Album no se encontro")
                          
                    
            elif opcion == 4:
                titulo_lista_a_buscar = input("Ingresa el titulo de la lista: ")
                print()
                lista_reproduccion = cuenta_abierta.getListaReproduccion(titulo_lista_a_buscar)
                
                if len(lista_reproduccion) > 0:
                    titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                    print()
                    busqueda_existosa = False
                    for cancion in lista_reproduccion:
                        titulo = cancion.getTitulo()
                        if titulo_a_buscar.lower() == titulo.lower():
                            cancion_encontrada = cancion
                            busqueda_existosa = True
                            
                    if busqueda_existosa:
                        self.Reproductor(cancion_encontrada, cuenta_abierta)
                    else:
                        print("El titulo no se encuentra")
                else:
                    print("La lista de reproduccion esta vacia")
                    print()
                
            elif opcion == 5:
                cuenta_abierta.CrearListaDeReproduccion()
            
            elif opcion == 6:
                Salir_menu_cuenta = True
                
            else:
                print("opcion invalida, intenta de nuevo")
                print()
            
    
    def MenuPlan(self, Cliente):
        Salir = False
        plan_activo = Cliente.getPaga()
        tipo_de_plan = Cliente.getTipoPlan()
        while not Salir:
            print("Plan " + tipo_de_plan)
            print("Menú Plan")
            print("1. Crear cuenta")
            print("2. Acceder a una cuenta existente")
            print("3. Salir")
            try:
                print()
                opcion = int(input("Ingresa una opcion: "))
                cuentas = Cliente.getCuentas()
                if opcion == 1:
                    nombre_cuenta_nueva = input("Ingresa el nombre de la cuenta nueva: ")
                    if len(cuentas) > 0:
                        cuenta_existe = False
                        for cuenta in cuentas:
                            nombre_cuenta_almacenada = cuenta.getNombre()
                            if nombre_cuenta_almacenada.lower() == nombre_cuenta_nueva.lower():
                                cuenta_existe = True
                        if cuenta_existe:
                            print("Ya hay una cuenta registrada con ese nombre ")
                            print()
                        else:
                            if plan_activo:
                                cuenta_nueva = Cuenta_usuario_paga(nombre_cuenta_nueva)
                                Cliente.AgregarCuenta(cuenta_nueva)
                        
                            else:
                                cuenta_nueva = CuentaUsuarioGratuito(nombre_cuenta_nueva)
                                Cliente.AgregarCuenta(cuenta_nueva)
                    else:
                        if plan_activo:
                            cuenta_nueva = Cuenta_usuario_paga(nombre_cuenta_nueva)
                            Cliente.AgregarCuenta(cuenta_nueva)
                            
                        else:
                            cuenta_nueva = CuentaUsuarioGratuito(nombre_cuenta_nueva)
                            Cliente.AgregarCuenta(cuenta_nueva)
                            
                elif opcion == 2:
                    if len(cuentas) > 0:
                        nombre_cuenta_acceso = input("Ingresa el nombre de la cuenta: ")
                        print()
                        cuenta_encontrada = False
                        for cuenta in cuentas:
                            nombre_cuenta_almacenada = cuenta.getNombre()
                            if nombre_cuenta_almacenada.lower() == nombre_cuenta_acceso.lower():
                                cuenta_encontrada = True
                                cuenta_abierta = cuenta     
                        if cuenta_encontrada:
                            self.MenuCuenta(cuenta_abierta)
                        else:
                            print("No existe una cuenta con ese nombre")
                            print()
                    else:
                        print("No hay cuentas existentes")
                        print()
                elif opcion ==3:
                    Salir = True
                    
                else:
                    print("La opcion es invalida, intenta de nuevo")
                    print()
            except ValueError:
                print("Error: No has ingresado un número entero válido.")
                print()
            
            
                
            
                        
                        
    def MenúContratarPlan(self):
        Salir = False
        print()
        print("Planes disponibles: ")
        print("1. Gratuito")
        print("     Una cuenta con anuncios")
        print("2. Individual")
        print("     Una cuenta, sin anuncios")
        print("3. Estudiantes")
        print("     Una cuenta, sin anuncios, decuento del 30%")
        print("4. Familiar")
        print("     Seis cuentas, sin anuncios")
        print()
        try:
            print()
            tipo_plan = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error: No has ingresado un número entero válido.")
            print()
            tipo_plan = 5
            
        if tipo_plan == 1:
            nombre_cliente = input("ingresa el nombre del usuario: ")
            print()
            cliente_nuevo = Cliente(nombre_cliente, "Gratuito", 1, True)
            self.__clientes.append(cliente_nuevo)
            print("Plan contratado")
            print()
        elif tipo_plan == 2:
            nombre_cliente = input("ingresa el nombre del usuario: ")
            print()
            cliente_nuevo = Cliente(nombre_cliente, "Individual", 1, False)
            self.__clientes.append(cliente_nuevo)
            print("Plan contratado")
            print()
        elif tipo_plan == 3:
            nombre_cliente = input("ingresa el nombre del usuario: ")
            print()
            cliente_nuevo = Cliente(nombre_cliente, "Estudiantes", 1, False)
            self.__clientes.append(cliente_nuevo)
            print("Plan contratado")
            print()
        elif tipo_plan == 4:
            nombre_cliente = input("ingresa el nombre del usuario: ")
            print()
            cliente_nuevo = Cliente(nombre_cliente, "Familiar", 1, False)
            self.__clientes.append(cliente_nuevo)
            print("Plan contratado")
            print()
        else:
            print("La opcion es invalida")
            print()
            