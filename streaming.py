# Importa las bibliotecas y clases necesarias para el programa
import random  # Para generar números aleatorios
import json  # Para trabajar con archivos JSON
from cuenta import Cuenta  # Importa la clase 'Cuenta' desde el módulo 'cuenta'
from cancion import Cancion  # Importa la clase 'Cancion' desde el módulo 'cancion'
from cliente import Cliente  # Importa la clase 'Cliente' desde el módulo 'cliente'


# Define la clase 'Streaming' para el sistema de streaming
class Streaming:

    # Constructor de la clase
    def __init__(self):
        self.__clientes = []  # Lista para almacenar clientes con sus planes
        self.__catalogo = []  # Lista donde se guardarán las canciones del catálogo
        self.__anuncios = [  # Lista de anuncios para cuentas gratuitas
            # Lista de anuncios
        ]

    # Método que proporciona la lista de clientes
    def getClientes(self):
        return self.__clientes

    # Método que proporciona el catálogo de música
    def getCatalogo(self):
        return self.__catalogo

    # Método para agregar un nuevo cliente a la lista de clientes
    def setNuevoCliente(self, Cliente):
        self.__clientes.append(Cliente)

    # Método para cargar el contenido del archivo que contiene el catálogo
    def CargarCatalogo(self, nombre_archivo):
        # Abre el archivo en modo lectura
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()  # Lee el contenido del archivo

        if contenido:  # Verifica si el archivo no está vacío
            with open(nombre_archivo, "r") as archivo:
                objetos_recuperados = json.load(archivo)  # Carga los objetos desde el archivo JSON
                self.__catalogo = []  # Vacía el contenido del catálogo para actualizarlo posteriormente

                # Por cada objeto recuperado, crea instancias de canciones y las agrega al catálogo
                for cancion_dict in objetos_recuperados:
                    cancion = Cancion(**cancion_dict)
                    self.__catalogo.append(cancion)
        else:
            self.__catalogo = []  # Si el archivo está vacío, inicializa el catálogo como una lista vacía

    # Método para reproducir una canción, agregarla a la lista de reproducción de una cuenta, y mostrar anuncios
    def Reproductor(self, cancion, cuenta):
        salir_reproductor = False  # Variable para salir del reproductor

        while not salir_reproductor:
            numero_anuncio = random.randint(0, 9)  # Genera un número aleatorio para elegir un anuncio
            anuncio = cuenta.getAnuncio()  # Recibe si la cuenta debe ver anuncios

            if anuncio:  # Evalúa si la cuenta debe ver anuncios
                anuncio_imprimir = self.__anuncios[numero_anuncio]
                print(anuncio_imprimir)  # Imprime un anuncio
                print()

            # Reproduce la canción recibida
            cancion.Reproducir()
            print("Opciones")  # Menú de opciones para el reproductor
            print("1. Agregar a lista de reproducción")  # Opción para agregar a una lista de reproducción
            print("2. Stop")  # Opción para detener la reproducción
            print()

            try:  # Manejo de error si la variable no es un número entero
                opcion = int(input("Ingresa una opción: "))  # Recibe la opción del usuario
                print()

                if opcion == 1:  # Primera opción: agregar a lista de reproducción
                    cuenta.AgregarCancion(cancion)  # Llama al método de cuenta para agregar la canción
                elif opcion == 2:  # Segunda opción: detener reproducción
                    salir_reproductor = True
            except ValueError:  # Manejo de error si el usuario ingresa algo que no es un número
                print("Error: No has ingresado una opción válida, intenta de nuevo.")  # Muestra un mensaje de error
                print()

    # Método para mostrar el menú de la cuenta y permitir buscar y reproducir canciones
    def MenuCuenta(self, cuenta):
        cuenta_abierta = cuenta  # Cuenta abierta actualmente
        Salir_menu_cuenta = False  # Variable para salir del menú

        while not Salir_menu_cuenta:
            print("Menú cuenta" + "     Cuenta: " + cuenta.getNombre())  # Menú de la cuenta
            print("1. Buscar por Título")
            print("2. Buscar por Artista")
            print("3. Buscar por Álbum")
            print("4. Buscar en lista de reproducción")
            print("5. Crear lista de reproducción")
            print("6. Cerrar sesión")
            print()

            try:  # Manejo de error si la variable no es un número entero
                opcion = int(input("Ingresa una opción: "))  # Recibe la opción del usuario
                print()

                if opcion == 1:  # Opción 1: buscar por título
                    # Solicita el título de la canción a buscar
                    titulo_a_buscar = input("Ingresa el título de la canción: ")
                    print()
                    busqueda_existosa = False  # Variable para la búsqueda
                    # Itera entre las canciones del catálogo
                    for cancion in self.__catalogo:
                        titulo = cancion.getTitulo()  # Obtiene el título de la canción
                        if titulo_a_buscar.lower() == titulo.lower():  # Compara los títulos (sin importar mayúsculas/minúsculas)
                            cancion_encontrada = cancion  # Almacena la canción encontrada
                            busqueda_existosa = True  # Búsqueda exitosa

                    if busqueda_existosa:  # Si la canción se encontró, se reproduce
                        self.Reproductor(cancion_encontrada, cuenta_abierta)
                    else:
                        print("El título no se encuentra")  # Mensaje de fallo
                        print()

                # Opciones 2, 3 y 4: buscar por artista, álbum o en lista de reproducción
                elif opcion in [2, 3, 4]:
                    if opcion == 2:
                        busqueda_nombre = "artista"
                    elif opcion == 3:
                        busqueda_nombre = "álbum"
                    else:
                        busqueda_nombre = "lista de reproducción"

                    busqueda_exitosa = False  # Variable para la búsqueda
                    # Solicita el nombre del artista, álbum o lista de reproducción a buscar
                    nombre_a_buscar = input(f"Ingresa el nombre del {busqueda_nombre}: ")
                    print()

                    if opcion == 2:  # Búsqueda por artista
                        canciones_coincidentes = []
                        # Itera entre las canciones del catálogo
                        for cancion in self.__catalogo:
                            artista = cancion.getArtista()  # Obtiene el artista de la canción
                            if nombre_a_buscar.lower() == artista.lower():  # Compara los nombres (sin importar mayúsculas/minúsculas)
                                canciones_coincidentes.append(cancion)  # Agrega la canción coincidente a la lista

                        if len(canciones_coincidentes) > 0:
                            print(f"Canciones del artista {nombre_a_buscar}:")
                            for cancion_artista in canciones_coincidentes:
                                print(cancion_artista.getTitulo())  # Muestra los títulos de las canciones del artista
                            titulo_a_buscar = input(
                                "Ingresa el título de la canción: ")  # Solicita el título de la canción a encontrar
                            print()
                            busqueda_existosa = False  # Variable para la búsqueda por título
                            for cancion in canciones_coincidentes:
                                titulo = cancion.getTitulo()
                                if titulo_a_buscar.lower() == titulo.lower():  # Si se encuentra la canción, se almacena y se declara la búsqueda exitosa
                                    cancion_encontrada = cancion
                                    busqueda_existosa = True

                            if busqueda_existosa:
                                self.Reproductor(cancion_encontrada,
                                                 cuenta_abierta)  # Si se encontró la canción, se reproduce
                            else:
                                print("El título no se encuentra")
                                print()
                        else:
                            print(f"No se encontraron canciones del artista {nombre_a_buscar}")
                            print()

                    elif opcion == 3:  # Búsqueda por álbum
                        canciones_coincidentes = []
                        # Itera entre las canciones del catálogo
                        for cancion in self.__catalogo:
                            album = cancion.getAlbum()  # Obtiene el álbum de la canción
                            if nombre_a_buscar.lower() == album.lower():  # Compara los nombres (sin importar mayúsculas/minúsculas)
                                canciones_coincidentes.append(cancion)  # Agrega la canción coincidente a la lista

                        if len(canciones_coincidentes) > 0:
                            print(f"Canciones del álbum {nombre_a_buscar}:")
                            for cancion_album in canciones_coincidentes:
                                print(cancion_album.getTitulo())  # Muestra los títulos de las canciones del álbum
                            titulo_a_buscar = input(
                                "Ingresa el título de la canción: ")  # Solicita el título de la canción a encontrar
                            print()
                            busqueda_existosa = False  # Variable para la búsqueda por título
                            for cancion in canciones_coincidentes:
                                titulo = cancion.getTitulo()
                                if titulo_a_buscar.lower() == titulo.lower():  # Si se encuentra la canción, se almacena y se declara la búsqueda exitosa
                                    cancion_encontrada = cancion
                                    busqueda_existosa = True

                            if busqueda_existosa:
                                self.Reproductor(cancion_encontrada,
                                                 cuenta_abierta)  # Si se encontró la canción, se reproduce
                            else:
                                print("El título no se encuentra")
                                print()
                        else:
                            print(f"No se encontraron canciones del álbum {nombre_a_buscar}")
                            print()

                    elif opcion == 4:  # Búsqueda en lista de reproducción
                        listas_reproduccion = cuenta_abierta.getListasDeReproduccion()

                        if len(listas_reproduccion) > 0:
                            print("Listas disponibles:")
                            for lista in listas_reproduccion:
                                nombre_lista = lista.get("nombre")
                                print(nombre_lista)  # Muestra los nombres de las listas de reproducción

                            titulo_lista_a_buscar = input(
                                "Ingresa el título de la lista: ")  # Solicita el nombre de la lista de reproducción a buscar
                            print()
                            lista_reproduccion = cuenta_abierta.getListaReproduccion(titulo_lista_a_buscar)

                            if len(lista_reproduccion) > 0:
                                print("Canciones disponibles:")
                                for cancion in lista_reproduccion:
                                    titulo_cancion = cancion.getTitulo()
                                    print(
                                        titulo_cancion)  # Muestra los títulos de las canciones en la lista de reproducción
                                print()
                                titulo_a_buscar = input(
                                    "Ingresa el título de la canción: ")  # Solicita el título de la canción a encontrar
                                print()
                                busqueda_existosa = False  # Variable para la búsqueda por título
                                for cancion in lista_reproduccion:
                                    titulo = cancion.getTitulo()
                                    if titulo_a_buscar.lower() == titulo.lower():  # Si se encuentra la canción, se almacena y se declara la búsqueda exitosa
                                        cancion_encontrada = cancion
                                        busqueda_existosa = True

                                if busqueda_existosa:
                                    self.Reproductor(cancion_encontrada,
                                                     cuenta_abierta)  # Si se encontró la canción, se reproduce
                                else:
                                    print("El título no se encuentra")
                                    print()
                            else:
                                print("La lista de reproducción está vacía")
                                print()
                        else:
                            print("No hay listas de reproducción disponibles")
                            print()

                elif opcion == 5:  # Opción 5: crear lista de reproducción
                    cuenta_abierta.CrearListaDeReproducción()

                elif opcion == 6:  # Opción 6: cerrar sesión
                    Salir_menu_cuenta = True

                else:
                    print("Opción inválida, intenta de nuevo")
                    print()
            except ValueError:  # Manejo de error si el usuario ingresa algo que no es un número
                print("Error: No has ingresado un número entero válido.")  # Mensaje de error
                print()

    # Método para mostrar el menú del plan del cliente y permitir la creación de cuentas y el acceso a cuentas existentes
    def MenuPlan(self, Cliente):
        Salir = False  # Variable para salir del menú
        plan_activo = Cliente.getPaga()  # Verifica si el cliente tiene un plan de pago activo
        tipo_de_plan = Cliente.getTipoPlan()  # Obtiene el tipo de plan del cliente

        while not Salir:
            print(
                "Plan " + tipo_de_plan + "    Nombre Usuario: " + Cliente.getNombre())  # Muestra el tipo de plan y el nombre del usuario
            print("Menú Plan")
            print("1. Crear cuenta")
            print("2. Acceder a una cuenta existente")
            print("3. Salir")

            try:
                opcion = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción
                cuentas = Cliente.getCuentas()  # Obtiene la lista de cuentas del cliente

                if opcion == 1:  # Opción 1: crear una nueva cuenta
                    nombre_cuenta_nueva = input(
                        "Ingresa el nombre de la cuenta nueva: ")  # Solicita el nombre de la cuenta
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

                elif opcion == 2:  # Opción 2: acceder a una cuenta existente
                    if len(cuentas) > 0:  # Verifica si el cliente tiene cuentas existentes
                        nombre_cuenta_acceso = input(
                            "Ingresa el nombre de la cuenta: ")  # Solicita el nombre de la cuenta
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

    # Método para mostrar el menú de contratación de planes
    def MenúContratarPlan(self):
        Salir = False  # Variable para controlar la salida del bucle
        print()
        print("Planes disponibles:")
        print("1. Gratuito")
        print("     Una cuenta con anuncios")
        print("2. Individual")
        print("     Una cuenta, sin anuncios")
        print("3. Estudiantes")
        print("     Una cuenta, sin anuncios, descuento del 30%")
        print("4. Familiar")
        print("     Seis cuentas, sin anuncios")
        print()

        try:
            print()
            tipo_plan = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción

            if tipo_plan == 1:  # Contratación del plan gratuito
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Gratuito", 1,
                                        True)  # Crea un nuevo cliente con el plan Gratuito
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            elif tipo_plan == 2:  # Contratación del plan individual
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Individual", 1,
                                        False)  # Crea un nuevo cliente con el plan Individual
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            elif tipo_plan == 3:  # Contratación del plan para estudiantes
                nombre_cliente = input("Ingresa el nombre del usuario: ")  # Solicita el nombre del usuario
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Estudiantes", 1,
                                        False)  # Crea un nuevo cliente con el plan Estudiantes
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            elif tipo_plan == 4:  # Contratación del plan familiar
                nombre_cliente = input(
                    "Ingresa el nombre del usuario principal: ")  # Solicita el nombre del usuario principal
                print()
                cliente_nuevo = Cliente(nombre_cliente, "Familiar", 6,
                                        False)  # Crea un nuevo cliente con el plan Familiar (6 cuentas)
                self.__clientes.append(cliente_nuevo)  # Agrega el nuevo cliente a la lista de clientes
                print("Plan contratado")
                print()
            else:
                print()
                print("La opción es inválida, intenta de nuevo")
                print()
        except ValueError:
            print()
            print("Error: No has ingresado un número entero válido.")
            print()

    # Método principal para ejecutar el programa
    def Ejecutar(self):
        salir_programa = False  # Variable para controlar la salida del programa

        while not salir_programa:
            print("Menú Principal")
            print("1. Contratar Plan")
            print("2. Acceder a un Plan")
            print("3. Salir")
            print()

            try:
                opcion = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción

                if opcion == 1:  # Opción 1: contratar un plan
                    self.MenúContratarPlan()  # Ejecuta el menú de contratación de planes
                elif opcion == 2:  # Opción 2: acceder a un plan
                    nombre_usuario = input("Ingresa tu nombre de usuario: ")  # Solicita el nombre de usuario
                    print()
                    plan_encontrado = False

                    for cliente in self.__clientes:  # Itera entre los clientes
                        nombre_cliente = cliente.getNombre()  # Obtiene el nombre del cliente
                        if nombre_cliente.lower() == nombre_usuario.lower():  # Compara los nombres (sin importar mayúsculas/minúsculas)
                            tipo_plan = cliente.getTipoPlan()  # Obtiene el tipo de plan
                            print(f"Bienvenido {nombre_cliente} - Plan {tipo_plan}")  # Muestra un mensaje de bienvenida
                            print()
                            self.MenuPlan(cliente)  # Ejecuta el menú de planes para el cliente
                            plan_encontrado = True
                            break

                    if not plan_encontrado:  # Si no se encontró el plan, muestra un mensaje de error
                        print("Usuario no encontrado")
                        print()
                elif opcion == 3:  # Opción 3: salir del programa
                    salir_programa = True
                else:
                    print()
                    print("La opción es inválida, intenta de nuevo")
                    print()
            except ValueError:
                print()
                print("Error: No has ingresado un número entero válido.")
                print()

# Si tienes alguna pregunta específica sobre alguna parte del código o necesitas una explicación adicional, no dudes en preguntar.
