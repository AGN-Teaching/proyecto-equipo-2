# Se importan las bibliotecas que vamos a ocupar y las clases para crear las instancias
import random
import json
from cuenta import Cuenta
from cancion import Cancion
from cliente import Cliente

# Clase del sistema de streaming 
class Streaming:
    
    # Metodo constructor de la clase
    def __init__(self):
        self.__clientes = [] # lista para guardar los clientes con sus respectivos planes
        self.__catalogo = [] # Lista donde se guardaran las canciones del catalogo
        # Lista que contiene los anuncios para las cuentas gratuitas
        self.__anuncios = [
            "¡Gran venta de verano! ¡Descuentos de hasta un 50%% en toda la tienda!",
            "¿Necesitas un nuevo teléfono? ¡Descubre los últimos modelos con la mejor tecnología!",
            "Oferta especial: Compra uno y llévate otro gratis en todos los pantalones vaqueros.",
            "¡Restaurante XYZ te ofrece un 2x1 en platillos selectos este viernes!",
            "¡Inscríbete en nuestro gimnasio hoy y obtén un mes de membresía gratuito!",
            "¡Liquidación de fin de temporada! Ropa, zapatos y accesorios a precios increíbles.",
            "Obtén un 10%% de descuento en tu primera compra cuando te registres en nuestra tienda en línea.",
            "Clases de yoga gratuitas todos los sábados a las 10 a. m. ¡Únete a nosotros!",
            "Oferta especial de aniversario: todos los pasteles al 20%% de descuento durante esta semana.",
            "¡Ven a nuestro evento de música en vivo el viernes a las 7 p. m.! Bebidas y aperitivos gratis."
        ]
        
    # Metodo que proporciona la lista de clientes 
    def getClientes(self):
        return self.__clientes
    
    # Metodo que proporciona el catalogo de musica
    def getCatalogo(self):
        return self.__Clientes
    
    # Metodo agrega un nuevo cliente a la lista de clientes
    def setNuevoCliente(self, Cliente):
        self.__clientes.append(Cliente)
        
    # Metodo para cargar el contenido del archivo que contiene el catalogo
    def CargarCatalogo(self, nombre_archivo):
        with open(nombre_archivo, "r") as archivo: # Abre el archivo en modo lectura
            contenido = archivo.read()  # Lee el contenido del archivo
        if contenido:  # Verifica si el archivo no está vacío
            with open(nombre_archivo, "r") as archivo:
                objetos_recuperados = json.load(archivo)  # Carga los objetos desde el archivo JSON
                self.catalogo = []  # Vacia el contenido del catalogo para posteriormente actualizarlo
                for cancion_dict in objetos_recuperados: # Por cada objeto recuperado recupera las instacias de las canciones
                    cancion = Cancion(**cancion_dict) # Crea instancias de Cancion 
                    self.__catalogo.append(cancion) #Agrega la cancion recuperada al catalogo               
        else:
            self.catalogo = []  # Si el archivo está vacio, inicializa el catalogo como una lista vacía
  
    # Metodo que recibe y reproduce una cancion,ademas la agrega a una lista de reproduccion de un objeto tipo cuenta
    def Reproductor(self, cancion, cuenta):
        
        salir_reproductor = False  # Variable para salir del reproductor
        while not salir_reproductor:
            numero_anuncio = random.randint(0, 9) # Genera un numero aleatorio para elegir un anuncio 
            anuncio = cuenta.getAnuncio() # Recibe si la cuenta debe ver anuncios
            if anuncio: # Evalua si la cuenta debe ver anuncios
                anuncio_imprimir = self.__anuncios[numero_anuncio]
                print(anuncio_imprimir) # imprime un anuncio
                print()
            # Reproduce la cancion recibida
            cancion.Reproducir()
            print("Opciones") # Menu de opciones para el reproductor
            print("1. Agregar a lista de reproduccion") # opcion para agregar a una lista de reproduccion
            print("2. Stop") # opcion para detener reproduccion
            print()
            try: # Manejo de error si la variable no es del tipo entero
                opcion = int(input("Ingresa una opcion: ")) # Rebice la opcion
                print()
                if opcion == 1: # Primera opcion
                    cuenta.AgregarCancion(cancion) # llama metodo de cuenta para agrega la cancion
                elif opcion == 2: # Segunda opcion
                    salir_reproductor = True
            except ValueError:# Recibe el error y manda mensaje de error
                print("Error: No has ingresado una opcion valida, intenta de nuevo.") # Mensaje de error
                print()


    # Metodo para desplegar menú de la cuenta para hacer busqueda y reproducir
    # Hace busqueda por titulo, artista, album y lista de reproduccion
    def MenuCuenta(self, cuenta): # Recibe objeto de tipo cuenta
        cuenta_abierta = cuenta # Cuenta abierta actualmente
        Salir_menu_cuenta = False # Variable para salir del menú
        while not Salir_menu_cuenta:
            print("Menú cuenta" + "     Cuenta: " + cuenta.getNombre()) # Menú de la cuenta
            print("1. Buscar por Titulo")
            print("2. Buscar por Artista")
            print("3. Buscar por album")
            print("4. Buscar en lista de reproduccion")
            print("5. Crear lista de reproduccion")
            print("6. Cerrar sesion")
            print()
            
            try: # Manejo de error si la variable no es del tipo entero
                print()
                opcion = int(input("Ingresa una opcion: ")) # Rebice la opcion
                print()
                if opcion ==1: # Opcion 1
                    print()
                    titulo_a_buscar = input("Ingresa el titulo de la cancion: ") # Recibe el titulo de la cancion a buscar
                    print()
                    busqueda_existosa = False # Variable de busqueda
                    for cancion in self.__catalogo: # itera entre las canciones del catalogo
                        titulo = cancion.getTitulo() # Obtiene el titulo de la cancion
                        if titulo_a_buscar.lower() == titulo.lower(): # Compara ambos titulos
                            cancion_encontrada = cancion # Guarda la cancion encontrada
                            busqueda_existosa = True # Variable de busqueda exitosa
                        
                    if  busqueda_existosa: # Si la cancion se encontro se reproduce la cancion
                        self.Reproductor(cancion_encontrada, cuenta_abierta)                    
                    else:
                        print("El titulo no se encuentra") # Mensaje de fallo
                        print()                  
                    
                            
                elif opcion == 2:
                    artista_a_buscar = input("Ingresa el artista de la cancion: ") # Recibe el artista de la cancion a buscar
                    print()
                    canciones_artista = [] # Lista que guarda las canciones con el mismo rtista 
                    busqueda_artista_exitosa = False # Variable de busqueda artista
                    for cancion in self.__catalogo: # Busca en el catalogo las canciones que ccompartan el mismo artista 
                        artista = cancion.getArtista()
                        if artista_a_buscar.lower() == artista.lower():
                            canciones_artista.append(cancion)
                            busqueda_artista_exitosa = True # Variable de busqueda por artista
                    if busqueda_artista_exitosa: # Evalua si se encontro el artista 
                        if len(canciones_artista) > 0:
                            print("Canciones disponibles: ") # imprime los titulos de las canciones que comparten artista 
                            for cancion_artista in canciones_artista:
                                titulo = cancion_artista.getTitulo()
                                print(titulo)
                            titulo_a_buscar = str(input("Ingresa el titulo de la cancion: ")) # pide el nombre de la cancion a encontrar
                            print()
                            busqueda_existosa = False # Variable de busqueda por titulo
                            for cancion in canciones_artista: # Busca en las canciones que comparten artista 
                                titulo = cancion.getTitulo()
                                if titulo_a_buscar.lower() == titulo.lower(): # Si encuentra la cancion la almacena y declara la busqueda de la cancion como exito
                                    cancion_encontrada = cancion
                                    busqueda_existosa = True
                                
                            if  busqueda_existosa: # si la cancion se enocontro reproduce la cancion
                                self.Reproductor(cancion_encontrada, cuenta_abierta)                    
                            else:
                                print("El titulo no se encuentra")
                                print()
                    else:    
                        print("El Artista no se encontro")
                        print()   
                                        
                elif opcion == 3:
                    album_a_buscar = st(input("Ingresa el nombre del album: "))
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
                            titulo_a_buscar = str(input("Ingresa el titulo de la cancion: "))
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
                                print() 
                    else:
                        print("El Album no se encontro")
                        print()
                            
                        
                elif opcion == 4:
                    listas_reproduccion = cuenta_abierta.getListasDeReproduccion()
                    if len(listas_reproduccion) > 0:
                        print("Listas disponibles")
                        for lista in listas_reproduccion:
                            nombre_lista = lista.get("nombre")
                            print(nombre_lista)
                    if len(listas_reproduccion) > 0:
                        titulo_lista_a_buscar = input("Ingresa el titulo de la lista: ")
                        print()
                        lista_reproduccion = cuenta_abierta.getListaReproduccion(titulo_lista_a_buscar)
                        
                        if len(lista_reproduccion) > 0:
                            print("Canciones disponibles: ")
                            for cancion in lista_reproduccion:
                                titulo_cancion = cancion.getTitulo()
                                print(titulo_cancion)
                            print()
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
                                print()
                        else:
                            print("La lista de reproduccion esta vacia")
                            print()
                    else: 
                        print("No hay listas de reproduccion ")
                        print()
                    
                elif opcion == 5:
                    cuenta_abierta.CrearListaDeReproduccion()
                
                elif opcion == 6:
                    Salir_menu_cuenta = True
                    
                else:
                    print("opcion invalida, intenta de nuevo")
                    print()
            except ValueError: # Recibe el error y manda mensaje de error
                print("Error: No has ingresado un número entero válido.") # Mensaje de error
                print()

                
            
            
    
    def MenuPlan(self, Cliente):
        Salir = False  # Variable para Salir del menú
        plan_activo = Cliente.getPaga()  # Verifica si el cliente tiene un plan de pago activo
        tipo_de_plan = Cliente.getTipoPlan()  # Obtiene el tipo de plan del cliente

        while not Salir:
            print("Plan " + tipo_de_plan + "    Nombre Usuario: " + Cliente.getNombre())  # Imprime el tipo de plan
            print("Menú Plan")
            print("1. Crear cuenta")
            print("2. Acceder a una cuenta existente")
            print("3. Salir")
            try:
                print()
                opcion = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción
                cuentas = Cliente.getCuentas()  # Obtiene la lista de cuentas del cliente

                if opcion == 1:  # Opción para crear una nueva cuenta
                    nombre_cuenta_nueva = input("Ingresa el nombre de la cuenta nueva: ")  # Solicita el nombre de la cuenta
                    print()
                    if len(cuentas) > 0:  # Verifica si el cliente ya tiene cuentas
                        cuenta_existe = False
                        for cuenta in cuentas:
                            nombre_cuenta_almacenada = cuenta.getNombre()
                            if nombre_cuenta_almacenada.lower() == nombre_cuenta_nueva.lower():
                                cuenta_existe = True
                        if cuenta_existe:
                            print("Ya hay una cuenta registrada con ese nombre")
                            print()
                        else:
                            if plan_activo:  # Comprueba si el cliente tiene un plan de pago activo
                                cuenta_nueva = Cuenta(nombre_cuenta_nueva, False)
                                Cliente.AgregarCuenta(cuenta_nueva)
                            else:
                                cuenta_nueva = Cuenta(nombre_cuenta_nueva, True)
                                Cliente.AgregarCuenta(cuenta_nueva)
                    else:
                        if plan_activo:
                            cuenta_nueva = Cuenta(nombre_cuenta_nueva, False)
                            Cliente.AgregarCuenta(cuenta_nueva)
                        else:
                            cuenta_nueva = Cuenta(nombre_cuenta_nueva, True)
                            Cliente.AgregarCuenta(cuenta_nueva)

                elif opcion == 2:  # Opción para acceder a una cuenta existente
                    if len(cuentas) > 0:  # Verifica si el cliente tiene cuentas existentes
                        nombre_cuenta_acceso = input("Ingresa el nombre de la cuenta: ")  # Solicita el nombre de la cuenta
                        print()
                        cuenta_encontrada = False
                        for cuenta in cuentas:
                            nombre_cuenta_almacenada = cuenta.getNombre()
                            if nombre_cuenta_almacenada.lower() == nombre_cuenta_acceso.lower():
                                cuenta_encontrada = True
                                cuenta_abierta = cuenta
                        if cuenta_encontrada:
                            self.MenuCuenta(cuenta_abierta)  # Accede al menú de la cuenta
                        else:
                            print("No existe una cuenta con ese nombre")
                            print()
                    else:
                        print()
                        print("No hay cuentas existentes")
                        print()
                elif opcion == 3:
                    Salir = True  # Termina el bucle si se selecciona la opción 3
                else:
                    print()
                    print("La opción es inválida, intenta de nuevo")
                    print()
            except ValueError:
                print()
                print("Error: No has ingresado un número entero válido.")
                print()

            
            
                
            
                        
                        
    def MenúContratarPlan(self):
        Salir = False  # Variable para controlar la salida del bucle
        print() # Menú para contratar un plan
        print("Planes disponibles: ")
        print("1. Gratuito")
        print("     Una cuenta con anuncios")
        print("2. Individual")
        print("     Una cuenta, sin anuncios")
        print("3. Estudiantes")
        print("     Una cuenta, sin anuncios, descuento del 30%")
        print("4. Familiar")
        print("     Seis cuentas, sin anuncios")
        print()
        try: # Manejo de error si la variable no es del tipo entero
            print()
            tipo_plan = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción
            if tipo_plan == 1:
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Gratuito", 1, True)  # Crea un nuevo cliente con el plan Gratuito
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            elif tipo_plan == 2:
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Individual", 1, False)  # Crea un nuevo cliente con el plan Individual
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            elif tipo_plan == 3:
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Estudiantes", 1, False)  # Crea un nuevo cliente con el plan Estudiantes
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            elif tipo_plan == 4:
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Familiar", 6, False)  # Crea un nuevo cliente con el plan Familiar
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            else:
                print("La opción es inválida")
                print()
        except ValueError:
            print("Error: La opcion es invalida.")# Muestra mensaje de error

            print()
          
        
            