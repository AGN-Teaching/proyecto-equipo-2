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
            except ValueError:
                print("Error: No has ingresado un número entero válido.")
                print()
                opcion = 4
            
            cuentas = Cliente.getCuentas()
            if opcion == 1:
                nombre_cuenta_nueva = input("Ingresa el nombre de la cuenta nueva: ")
                if cuentas:
                    for cuenta in cuentas:
                        nombre_cuenta_almacenada = cuenta.getNombre()
                        if nombre_cuenta_almacenada.lower() == nombre_cuenta_nueva.lower():
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
                try:
                    nombre_cuenta_acceso = input("Ingresa el nombre de la cuenta: ")
                    print()
                    cuenta_encontrada = False
                    for cuenta in cuentas:
                        nombre_cuenta_almacenada = cuenta.getNombre()
                        if nombre_cuenta_almacenada.lower() == nombre_cuenta_acceso.lower():
                            cuenta_encontrada = True
                            cuenta_abierta = cuenta
                    if cuenta_encontrada:
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
                                
                                try:
                                    for cancion in self.__catalogo:
                                        titulo = cancion.getTitulo()
                                        if titulo_a_buscar.lower() == titulo.lower():
                                            cancion_encontrada = cancion
                                    if not cancion_encontrada:
                                        print("El titulo no se encuentra")
                                    salir_cancion = False
                                    while not salir_cancion:
                                        cancion_encontrada.Reproducir()
                                        print("Opciones")
                                        print("1. Agregar a lista de reproduccion")
                                        print("2. Stop")
                                        print()
                                        try:
                                            opcion = int(input("Ingresa una opcion"))
                                            print()
                                            if opcion == 1:
                                                cuenta_abierta.AgregarCancion(cancion_encontrada)
                                            elif opcion == 2:
                                                salir_cancion = True
                                        except ValueError:
                                            print("Error: No has ingresado una opcion valida, intenta de nuevo.")
                                except IndexError:
                                    print("El catalogo esta vacio.")
                                    
                                
                                        
                            elif opcion == 2:
                                artista_a_buscar = input("Ingresa el artista de la cancion: ")
                                canciones_artista = []
                                artista_encontrado = False
                                try:
                                    for cancion in self.__catalogo:
                                        artista = cancion.getArtista()
                                        if artista_a_buscar.lower() == artista.lower():
                                            canciones_artista.append(cancion)
                                            artista_encontrado = True
                                    if not canciones_artista:
                                        print("El Artista no se encontro")
                                except IndexError:
                                    print("El catalogo esta vacio.")
                                    print()
                                
                                
                                if artista_encontrado and canciones_artista:       
                                    print("Canciones disponibles ")
                                    for cancion_artista in canciones_artista:
                                        titulo = cancion_artista.getTitulo()
                                        print(titulo)
                                    titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                                    print()
                                    for cancion in canciones_artista:
                                        titulo = cancion.getTitulo()
                                        if titulo_a_buscar.lower() == titulo.lower():
                                            cancion_encontrada = cancion
                                    if not cancion_encontrada:
                                        print("El titulo no se encuentra")
                                    salir_cancion = False
                                    while not salir_cancion:
                                        cancion_encontrada.Reproducir()
                                        print("Opciones")
                                        print("1. Agregar a lista de reproduccion")
                                        print("2. Stop")
                                        print()
                                        try:
                                            opcion = int(input("Ingresa una opcion"))
                                            print()
                                            if opcion == 1:
                                                cuenta_abierta.AgregarCancion(cancion_encontrada)
                                            elif opcion == 2:
                                                salir_cancion = True
                                        except ValueError:
                                            print("Error: No has ingresado una opcion valida, intenta de nuevo.")
                                            
                            elif opcion == 3:
                                album_a_buscar = input("Ingresa el nombre del album: ")
                                print()
                                canciones_album = []
                                album_encontrado = False
                                try:
                                    for cancion in self.__catalogo:
                                        album = cancion.getAlbum()
                                        if album_a_buscar.lower() == album.lower():
                                            canciones_album.append(cancion)
                                            album_encontrado = True
                                    if not canciones_album:
                                            print("El Album no se encontro")
                                except IndexError:
                                    print("El catalogo esta vacio.")
                                    print()
                                
                                
                                if album_encontrado and canciones_album:       
                                    print("Canciones disponibles ")
                                    for cancion_album in canciones_album:
                                        titulo = cancion_album.getTitulo()
                                        print(titulo)
                                    titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                                    print()
                                    for cancion in canciones_album:
                                        titulo = cancion.getTitulo()
                                        if titulo_a_buscar.lower() == titulo.lower():
                                            cancion_encontrada = cancion
                                    if not cancion_encontrada:
                                        print("El titulo no se encuentra")
                                    salir_cancion = False
                                    while not salir_cancion:
                                        cancion_encontrada.Reproducir()
                                        print("Opciones")
                                        print("1. Agregar a lista de reproduccion")
                                        print("2. Stop")
                                        print()
                                        try:
                                            opcion = int(input("Ingresa una opcion"))
                                            print()
                                            if opcion == 1:
                                                cuenta_abierta.AgregarCancion(cancion_encontrada)
                                            elif opcion == 2:
                                                salir_cancion = True
                                        except ValueError:
                                            print("Error: No has ingresado una opcion valida, intenta de nuevo.")
                            elif opcion == 4:
                                titulo_lista_a_buscar = input("Ingresa el titulo de la lista: ")
                                print()
                                lista_reproduccion = cuenta_abierta.getListaReproduccion(titulo_lista_a_buscar)
                                if lista_reproduccion:
                                    titulo_a_buscar = input("Ingresa el titulo de la cancion: ")
                                    print()
                                    for cancion in lista_reproduccion:
                                        titulo = cancion.getTitulo()
                                        if titulo_a_buscar.lower() == titulo.lower():
                                            cancion_encontrada = cancion
                                    if not cancion_encontrada:
                                        print("El titulo no se encuentra")
                                    cancion_encontrada.Reproducir()
                                else:
                                    print("L alista de reproduccion esta vacia")
                                    print()
                                
                            elif opcion == 5:
                                cuenta_abierta.CrearListaDeReproduccion()
                            
                            elif opcion == 6:
                                Salir_menu_cuenta = True
                                
                            else:
                                print("opcion invalida, intenta de nuevo")
                                print()
                    else:
                        print("No existe una cuenta con ese nombre")
                        print()
                except IndexError:
                    print("No hay cuentas existentes")
                    print()
            elif opcion ==3:
                Salir = True
                
            else:
                print("La opcion es invalida, intenta de nuevo")
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
            