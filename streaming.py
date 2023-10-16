# Importa las bibliotecas y clases necesarias para el programa
import random  # Para generar números aleatorios
import json  # Para trabajar con archivos JSON
from cancion import Cancion  # Importa la clase 'Cancion' desde el módulo 'cancion'
from cliente import Cliente  # Importa la clase 'Cliente' desde el módulo 'cliente'
from plan import Plan


# Define la clase 'Streaming' para el sistema de streaming
class Streaming:

    # Constructor de la clase
    def __init__(self):
        self.__clientes = []  # Lista para almacenar clientes con sus planes
        self.__catalogo = []  # Lista donde se guardarán las canciones del catálogo
        # Lista de notificaciones
        self.__notificaciones_conciertos = [
            "¡No te pierdas el emocionante concierto de Taylor Swift en tu ciudad! Fecha: 15 de noviembre de 2023 en el Estadio Principal. ¡Consigue tus entradas ahora!",
            "Adele en concierto: Prepárate para una noche inolvidable el 10 de diciembre de 2023 en el Teatro Grande. ¡Compra tus boletos antes de que se agoten!",
            "Michael Jackson Experience: Un tributo inolvidable el 12 de abril de 2024 en el Anfiteatro. Ven y celebra el legado de Michael.",
            "Juan Gabriel en concierto: Revive sus éxitos el 25 de junio de 2024 en el Auditorio Principal. ¡No te lo pierdas!"
        ]
        # Lista de anuncios para cuentas gratuitas
        self.__anuncios = [
            "¡Gran venta de verano! ¡Descuentos de hasta un 50% en toda la tienda!",
            "¿Necesitas un nuevo teléfono? ¡Descubre los últimos modelos con la mejor tecnología!",
            "La música se ve mejor sin anuncios. Obtén una experiencia visual ininterrumpida con el Plan Individual.",
            "Opta por el plan Familiar y disfruta de música sin interrupciones con toda tu familia.",
            "El plan Duo te ofrece la posibilidad de ver música sin anuncios y compartirla con esa persona especial. ¡Únete ahora!",
            "Obtén acceso exclusivo a tu música favorita con una cuenta individual. Ve música sin anuncios y crea tus listas de reproducción personalizadas.",
            "Estudiantes, este plan es para ti. Disfruta de una cuenta premium con un descuento especial. Sin anuncios y con todas las ventajas de la suscripción estándar.",
            "Escuchar música es mejor cuando lo compartes. El plan Duo te permite tener dos cuentas premium para que tú y tu compañero puedan disfrutar de la música sin anuncios juntos.",
            "¡Música para todos! Nuestro plan Familiar es perfecto para familias. Con hasta 6 cuentas premium, todos en tu hogar pueden disfrutar de la música sin anuncios y crear listas de reproducción personalizadas.",
            "Tu música, tus reglas. Con el Plan Individual, disfruta de una cuenta premium sin anuncios y crea tus propias listas de reproducción.",
            "Estudia con ritmo. El Plan para Estudiantes te ofrece un 30% de descuento en una cuenta premium, sin anuncios",
            "Ahorra y disfruta de la música con el Plan para Estudiantes. Tu cuenta premium con un 30% de descuento te espera.",
            "Escucha en pareja con el Plan Duo. Dos cuentas premium por un precio más bajo, ideal para disfrutar juntos.",
            "Una suscripción para todos. El Plan Familiar ofrece acceso premium a todos los miembros de tu familia a un precio asequible.",
            "Unidos por la música. El Plan Familiar es la elección ideal para hogares llenos de amantes de la música. Hasta 6 cuentas premium incluidas.",
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
    
    def getNotificacionesConciertos(self):
        return self.__notificaciones_conciertos
    
    def getAnuncios(self):
        self.__anuncios

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
            notificaciones_leidas = cuenta.getNotificacionesLeidas()
            numero_anuncio = random.randint(0, 9)  # Genera un número aleatorio para elegir un anuncio
            paga = cliente.getPaga()  # Recibe si la cuenta debe ver anuncios
            
            if not notificaciones_leidas:
                print("Nuevas notificaciones en la seccion de notificaciones ")
                print()
            
            if not paga:  # Evalúa si la cuenta debe ver anuncios
                print("Anuncio")
                anuncio_imprimir = self.__anuncios[numero_anuncio]
                print(anuncio_imprimir)  # Imprime un anuncio

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
    def MenuCuenta(self, cuenta_abierta, cliente):
        Salir_menu_cuenta = False  # Variable para salir del menú

        while not Salir_menu_cuenta:
            notificaciones_leidas = cuenta_abierta.getNotificacionesLeidas()
            if not notificaciones_leidas:
                print("¡Nuevas notificaciones! ")
                print("ve a la seccion de notificaciones ")
                print()
            
            # Menú de la cuenta
            print("Menú cuenta" + "     Cuenta: " + cuenta_abierta.getNombre())  # Menú de la cuenta
            print("1. Buscar por Título")
            print("2. Buscar por Artista")
            print("3. Buscar por Álbum")
            print("4. Buscar en lista de reproducción")
            print("5. Crear lista de reproducción")
            print("6. Notificaciones")
            print("7. Cerrar sesión")
            print()

            try:  # Manejo de error si la variable no es un número entero
                opcion = int(input("Ingresa una opción: "))  # Recibe la opción del usuario
                print()

                if opcion == 1:  # Opción 1: buscar por título
                    lista = self.__catalogo
                    self.BuscarPorTitulo(cuenta_abierta, cliente, lista)
                        
                elif opcion == 2:  # Búsqueda por artista en el catalogo
                    self.BuscarPorArtista(cuenta_abierta, cliente)

                elif opcion == 3:  # Búsqueda por álbum en el catalogo
                    self.BuscarPorAlbum(cuenta_abierta, cliente)

                elif opcion == 4:  # Búsqueda en lista de reproducción
                    busqueda = cuenta_abierta.BuscarEnLista()
                    if busqueda != None:
                        cancion_encontrada = busqueda
                        self.Reproductor(cancion_encontrada, cuenta_abierta, cliente)  # Si se encontró la canción, se reproduce
                    
                elif opcion == 5:  # Opción 5: crear lista de reproducción
                    cuenta_abierta.CrearListaDeReproduccion()
                
                elif opcion == 6:  # Opción 5: crear lista de reproducción
                    cuenta_abierta.MostrarNotificaciones(self.__notificaciones_conciertos)

                elif opcion == 7:  # Opción 6: cerrar sesión
                    Salir_menu_cuenta = True

                else:
                    print("Opción inválida, intenta de nuevo")
                    print()
            except ValueError:  # Manejo de error si el usuario ingresa algo que no es un número
                print("Error: No has ingresado un número entero válido.")  # Mensaje de error
                print()


    def BuscarPorTitulo(self, cuenta, cliente, lista):
        # Solicita el título de la canción a buscar
        titulo_a_buscar = input("Ingresa el título de la canción: ")
        print()
        busqueda_existosa = False  # Variable para la búsqueda
        # Itera entre las canciones del catálogo
        for cancion in lista:
            titulo = cancion.getTitulo()  # Obtiene el título de la canción
            if titulo_a_buscar.lower() == titulo.lower():  # Compara los títulos (sin importar mayúsculas/minúsculas)
                cancion_encontrada = cancion  # Almacena la canción encontrada
                busqueda_existosa = True  # Búsqueda exitosa

        if busqueda_existosa:  # Si la canción se encontró, se reproduce
            self.Reproductor(cancion_encontrada, cuenta, cliente)
        else:
            print("El título no se encuentra")  # Mensaje de fallo
            print()

    def BuscarPorArtista(self, cuenta, cliente):
        
        artista_a_buscar = input("Ingresa el nombre del artista: ") # Solicita el nombre del artista
        print()
        
        canciones_coincidentes = [] # crea una lista para gusrdar las lists que comparten artista
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
            # Muestra los títulos de las canciones del artista
            print(f"Canciones del artista {artista_a_buscar}:")
            for cancion_artista in canciones_coincidentes:
                print(cancion_artista.getTitulo())  
            print()
            self.BuscarPorTitulo(cuenta, cliente, canciones_coincidentes)

    def BuscarPorAlbum(self, cuenta, cliente):
        
        album_a_buscar = input("Ingresa el nombre del album: ") # Solicita el nombre del album
        print()
        canciones_coincidentes = [] # crea una lista para gusrdar las lists que comparten album
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
            self.BuscarPorTitulo(cuenta, cliente, canciones_coincidentes)
            
        
    
    # Método para mostrar el menú del plan del cliente y permitir la creación de cuentas y el acceso a cuentas existentes
    def MenuPlan(self, Cliente):
        Salir = False  # Variable para salir del menú
        tipo_de_plan = Cliente.getTipoPlan()  # Obtiene el tipo de plan del cliente

        while not Salir:
            cuentas = Cliente.getCuentas()
            print("Plan " + tipo_de_plan + "    Nombre Usuario: " + Cliente.getNombre())  # Muestra el tipo de plan y el nombre del usuario
            print()
            
            if len(cuentas) > 0: # Verifica si hay contenido en la lista
                print("Perfiles creados: ")
                for cuenta in cuentas:
                    nombre_cuenta = cuenta.getNombre()
                    print(nombre_cuenta)
                print()
            
            # Muestra el menú del cliente
            print("Menú Plan")
            print("1. Crear cuenta/perfil")
            print("2. Eliminar cuenta")
            print("3. Acceder a una cuenta existente")
            print("4. Salir")

            try:
                opcion = int(input("Ingresa una opción: "))  # Solicita al usuario que ingrese una opción
                print()

                if opcion == 1:  # Opción 1: crear una nueva cuenta
                    Cliente.AgregarCuenta()

                elif opcion == 2:
                    Cliente.EliminarCuenta()
                
                elif opcion == 3:  # Opción 2: acceder a una cuenta existente
                    cuentas = Cliente.getCuentas()  # Obtiene la lista de cuentas del cliente
                    hay_cuentas = False
                    if len(cuentas) > 0:  # Verifica si el cliente tiene cuentas existentes
                        hay_cuentas = True
                        
                    if hay_cuentas:
                        #imprime los nombres de las cuentas creadas si existen 
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
        plan = Plan() # Crea instancia de clase Plan para asignar los distintos tipos de planes 
        
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
