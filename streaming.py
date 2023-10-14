# Importa las bibliotecas y clases necesarias para el programa
import random  # Para generar números aleatorios
import json  # Para trabajar con archivos JSON
from cuenta import Cuenta  # Importa la clase 'Cuenta' desde el módulo 'cuenta'
from cancion import Cancion  # Importa la clase 'Cancion' desde el módulo 'cancion'
from cliente import Cliente  # Importa la clase 'Cliente' desde el módulo 'cliente'
from plan import Plan


# Define la clase 'Streaming' para el sistema de streaming
class Streaming:

    # Constructor de la clase
    def __init__(self):
        self.__clientes = []  # Lista para almacenar clientes con sus planes
        self.__catalogo = []  # Lista donde se guardarán las canciones del catálogo
        # Lista de anuncios para cuentas gratuitas
        self.__anuncios = [
            "¡Gran venta de verano! ¡Descuentos de hasta un 50% en toda la tienda!",
            "¿Necesitas un nuevo teléfono? ¡Descubre los últimos modelos con la mejor tecnología!",
            "Oferta especial: Compra uno y llévate otro gratis en todos los pantalones vaqueros.",
            "¡Restaurante XYZ te ofrece un 2x1 en platillos selectos este viernes!",
            "¡Inscríbete en nuestro gimnasio hoy y obtén un mes de membresía gratuito!",
            "¡Liquidación de fin de temporada! Ropa, zapatos y accesorios a precios increíbles.",
            "Obtén un 10% de descuento en tu primera compra cuando te registres en nuestra tienda en línea.",
            "Clases de yoga gratuitas todos los sábados a las 10 a. m. ¡Únete a nosotros!",
            "Oferta especial de aniversario: todos los pasteles al 20% de descuento durante esta semana.",
            "¡Ven a nuestro evento de música en vivo el viernes a las 7 p. m.! Bebidas y aperitivos gratis."
        ]
    # Método que proporciona la lista de clientes
    def getClientes(self):
        return self.__clientes

    # Método que proporciona el catálogo de música
    def getCatalogo(self):
        return self.__catalogo

    # Método para agregar un nuevo cliente a la lista de clientes
    def CrearNuevoCliente(self, opcion, plan):
        nombre_cliente = input("Ingresa el nombre del usuario: ")
        plan_asignado = plan.AsignarPlan(opcion)
        numero_cuentas = plan.AsignarNumeroCuentas(opcion)
        paga = plan.AsignarPaga(opcion)
        cliente = Cliente(nombre_cliente, plan_asignado, numero_cuentas, paga)
        self.__clientes.append(cliente)
        print()
        print("¡Usuario angregado correctamente!")
        print()

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
    def Reproductor(self, cancion, cuenta, cliente):
        salir_reproductor = False  # Variable para salir del reproductor

        while not salir_reproductor:
            numero_anuncio = random.randint(0, 9)  # Genera un número aleatorio para elegir un anuncio
            anuncio = cliente.getPaga()  # Recibe si la cuenta debe ver anuncios

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
    def MenuCuenta(self, cuenta, cliente):
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
                        self.Reproductor(cancion_encontrada, cuenta_abierta, cliente)
                    else:
                        print("El título no se encuentra")  # Mensaje de fallo
                        print()
                        
                elif opcion == 2:  # Búsqueda por artista
                    artista_a_buscar = input("Ingresa el nombre del artista: ")
                    print()
                    canciones_coincidentes = []
                    # Itera entre las canciones del catálogo
                    for cancion in self.__catalogo:
                        artista = cancion.getArtista()  # Obtiene el artista de la canción
                        if artista_a_buscar.lower() == artista.lower():  # Compara los nombres (sin importar mayúsculas/minúsculas)
                            canciones_coincidentes.append(cancion)  # Agrega la canción coincidente a la lista
                    contenido_en_lista = False
                    if len(canciones_coincidentes) > 0: # revisa si hay contenido en la lista 
                        contenido_en_lista = True # indica si hay contenido en la lista
                    else:
                        print(f"No se encontraron canciones del artista {artista_a_buscar}")
                        print()
                    
                    if contenido_en_lista: # revisa si hay contenido en la lista 
                        print(f"Canciones del artista {artista_a_buscar}:")
                        for cancion_artista in canciones_coincidentes:
                            print(cancion_artista.getTitulo())  # Muestra los títulos de las canciones del artista
                        print()
                        titulo_a_buscar = input("Ingresa el título de la canción: ")  # Solicita el título de la canción a encontrar
                        print()
                        busqueda_existosa = False  # Variable para la búsqueda por título
                        for cancion in canciones_coincidentes:
                            titulo = cancion.getTitulo()
                            if titulo_a_buscar.lower() == titulo.lower():  # Si se encuentra la canción, se almacena y se declara la búsqueda exitosa
                                cancion_encontrada = cancion
                                busqueda_existosa = True

                        if busqueda_existosa:
                            self.Reproductor(cancion_encontrada,cuenta_abierta, cliente)  # Si se encontró la canción, se reproduce
                        else:
                            print("El título no se encuentra")
                            print()

                elif opcion == 3:  # Búsqueda por álbum
                    album_a_buscar = input("Ingresa el nombre del album: ")
                    print()
                    canciones_coincidentes = []
                    # Itera entre las canciones del catálogo
                    for cancion in self.__catalogo:
                        album = cancion.getAlbum()  # Obtiene el álbum de la canción
                        if album_a_buscar.lower() == album.lower():  # Compara los nombres (sin importar mayúsculas/minúsculas)
                            canciones_coincidentes.append(cancion)  # Agrega la canción coincidente a la lista
                    contenido_en_lista = False
                    if len(canciones_coincidentes) > 0:# revisa si hay contenido en la lista 
                        contenido_en_lista = True # indica si hay contenido en la lista
                    else:
                        print(f"No se encontraron canciones del álbum {album_a_buscar}")
                        print()
                        
                    if contenido_en_lista: # revisa si hay contenido en la lista 
                        print(f"Canciones del álbum {album_a_buscar}:")
                        for cancion_album in canciones_coincidentes:
                            print(cancion_album.getTitulo())  # Muestra los títulos de las canciones del álbum
                        print()
                        titulo_a_buscar = input("Ingresa el título de la canción: ")  # Solicita el título de la canción a encontrar
                        print()
                        busqueda_existosa = False  # Variable para la búsqueda por título
                        for cancion in canciones_coincidentes:
                            titulo = cancion.getTitulo()
                            if titulo_a_buscar.lower() == titulo.lower():  # Si se encuentra la canción, se almacena y se declara la búsqueda exitosa
                                cancion_encontrada = cancion
                                busqueda_existosa = True

                        if busqueda_existosa:
                            self.Reproductor(cancion_encontrada,cuenta_abierta, cliente)  # Si se encontró la canción, se reproduce
                        else:
                            print("El título no se encuentra")
                            print()

                elif opcion == 4:  # Búsqueda en lista de reproducción
                    listas_reproduccion = cuenta_abierta.getListasDeReproduccion()

                    contenido_en_lista = False
                    if len(listas_reproduccion) > 0: # revisa si hay contenido en la lista 
                        contenido_en_lista = True
                    else:
                        print("No hay listas de reproducción disponibles")
                        print()
                    
                    if contenido_en_lista: # revisa si hay contenido en la lista 
                        print("Listas disponibles:")
                        for lista in listas_reproduccion:
                            nombre_lista = lista.get("nombre")
                            print(nombre_lista)  # Muestra los nombres de las listas de reproducción

                        titulo_lista_a_buscar = input(
                            "Ingresa el título de la lista: ")  # Solicita el nombre de la lista de reproducción a buscar
                        print()
                        lista_reproduccion = cuenta_abierta.getListaReproduccion(titulo_lista_a_buscar)

                        contenido_en_lista_repoduccion = False
                        if len(lista_reproduccion) > 0:# revisa si hay contenido en la lista 
                            contenido_en_lista_repoduccion = True
                        else:
                            print("La lista de reproducción está vacía")
                            print()
                        
                        if contenido_en_lista_repoduccion: # revisa si hay contenido en la lista 
                            print("Canciones disponibles:")
                            for cancion in lista_reproduccion:
                                titulo_cancion = cancion.getTitulo()
                                print(titulo_cancion)  # Muestra los títulos de las canciones en la lista de reproducción
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
                                self.Reproductor(cancion_encontrada, cuenta_abierta, cliente)  # Si se encontró la canción, se reproduce
                            else:
                                print("El título no se encuentra")
                                print()

                elif opcion == 5:  # Opción 5: crear lista de reproducción
                    cuenta_abierta.CrearListaDeReproduccion()

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
        tipo_de_plan = Cliente.getTipoPlan()  # Obtiene el tipo de plan del cliente

        while not Salir:
            
            print("Plan " + tipo_de_plan + "    Nombre Usuario: " + Cliente.getNombre())  # Muestra el tipo de plan y el nombre del usuario
            print()
            cuentas = Cliente.getCuentas()  # Obtiene la lista de cuentas del cliente
            if len(cuentas) > 0:
                print("Perfiles creados: ")
                for cuenta in cuentas:
                    nombre_cuenta = cuenta.getNombre()
                    print(nombre_cuenta)
                print()
            print("Menú Plan")
            print("1. Crear cuenta/perfil")
            print("2. Eliminar cuenta")
            print("3. Acceder a una cuenta existente")
            print("4. Salir")

            try:
                opcion = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción
                print()

                if opcion == 1:  # Opción 1: crear una nueva cuenta
                    Cliente.CrearCuenta()

                elif opcion == 2:
                    Cliente.EliminarCuenta()
                
                elif opcion == 3:  # Opción 2: acceder a una cuenta existente
                    if len(cuentas) > 0:  # Verifica si el cliente tiene cuentas existentes
                        print("Perfiles creados: ")
                        for cuenta in cuentas:
                            nombre_cuenta = cuenta.getNombre()
                            print(nombre_cuenta)
                        print()
                        nombre_cuenta_acceso = input("Ingresa el nombre de la cuenta: ")  # Solicita el nombre de la cuenta
                        print()
                        cuenta_encontrada = False
                        for cuenta in cuentas:
                            nombre_cuenta_almacenada = cuenta.getNombre()
                            if nombre_cuenta_almacenada.lower() == nombre_cuenta_acceso.lower():
                                cuenta_encontrada = True
                                cuenta_abierta = cuenta
                        if cuenta_encontrada:
                            self.MenuCuenta(cuenta_abierta, Cliente)  # Accede al menú de la cuenta
                        else:
                            print("No existe una cuenta con ese nombre")
                            print()
                    else:
                        print()
                        print("No hay cuentas existentes")
                        print()
                elif opcion == 4:
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
        plan = Plan()
        print()
        print("Planes disponibles:")
        print("1. Gratuito")
        print("     Una cuenta con anuncios")
        print("2. Individual")
        print("     Una cuenta, sin anuncios")
        print("3. Estudiantes")
        print("     Una cuenta, sin anuncios, descuento del 30%")
        print("4. Duo")
        print("     Dos cuentas")
        print("5. Familiar")
        print("     Seis cuentas, sin anuncios")
        print()

        try:
            print()
            opcion = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción
            lista_opciones = [1,2,3,4,5]
            if opcion in lista_opciones:  # busca en las opciones disponibles
                self.CrearNuevoCliente(opcion, plan) # funcion crear cliente nuevo
            else:
                print()
                print("La opción es inválida, intenta de nuevo")
                print()
        except ValueError:
            print()
            print("Error: No has ingresado un número entero válido.")
            print()
