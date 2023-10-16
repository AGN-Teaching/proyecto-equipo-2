
class Cuenta():
    # Constructor: inicializa los atributos
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__listas_de_reproduccion = []
        self.__notificaciones_leidas = False

    def AgregarCancion(self, cancion):
        # Método para agregar una canción a una lista de reproducción existente o crear una nueva
        Salir = False  # Variable para controlar el bucle

        while not Salir:
            print("Opciones: ")
            print("1. Agregar a lista de reproduccion existente")
            print("2. Agregar a una lista de reproduccion nueva ")
            print("3. Regresar")
            print()
            try:
                opcion = int(input("Ingresa una opcion: "))
                print()
                if opcion == 1: # Agregar a lista de reproducción existente
                    self.AgregarAListaExistente(cancion)
                    
                elif opcion == 2: # Agregar a una lista de reproducción nueva
                    self.AgregarAListaNueva(cancion)
                    
                elif opcion == 3: # Salir
                    Salir = True
                    
                else:
                    print("La opción es inválida ")
                    print()
            except ValueError:
                print("Error: No has ingresado una opción.")
                print()
                
    def AgregarAListaExistente(self, cancion):
        hay_listas = False
        if len(self.__listas_de_reproduccion) > 0:
            hay_listas = True
            
        if hay_listas:
            print("Listas disponibles")
            # Mostrar las listas de reproducción existentes
            for elemento in self.__listas_de_reproduccion:
                nombre_lista = elemento.get("nombre")
                print(nombre_lista)
            print()
            nombre_lista_de_reproduccion_a_buscar = input("Ingresa el nombre de la lista: ") # solicita el nombre de la lista a buscar
            print()
            
            lista_agregada = False
            for elemento in self.__listas_de_reproduccion: # busca si la lista solicitada existe 
                nombre_lista = elemento["nombre"]
                if nombre_lista_de_reproduccion_a_buscar == nombre_lista: # si los nombres coinciden se declara lista_encontrada como verdadero
                    lista = elemento["lista"]
                    lista.append(cancion)
                    lista_agregada = True
            
            # Se evalua el mensaje destinado al usuario
            if lista_agregada: 
                print("¡Canción agregada exitosamente!")
                print()
                Salir = True
            else:
                print("La lista no se encuentra")
                
        else:
            print("No hay listas de reproducción, crea una nueva")
            print()
    
    def AgregarAListaNueva(self, cancion):
        nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ") # Solicita el nombre de la lista nueva
        print()
        
        # Busca si la lista existe
        nombre_lista_disponible = True
        for lista in self.__listas_de_reproduccion: 
            nombre_lista_a_comparar = lista["nombre"]
            if nombre_lista_nueva.lower() == nombre_lista_a_comparar.lower():
                nombre_lista_disponible = False
                
        # crea la lista y gusrda la cancion
        if nombre_lista_disponible:
            lista_nueva = []
            lista_nueva.append(cancion)
            self.__listas_de_reproduccion.append({"nombre": nombre_lista_nueva, "lista": lista_nueva})
            print("Canción agregada a la lista nueva")
            print()
        # Indica si la lista existe 
        else:
            print()
            print("El nombre de la lista está ocupado")
            print()
    
    def CrearListaDeReproduccion(self):
        # Método para crear una nueva lista de reproducción
        nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
        print()
        nombre_lista_disponible = True
        for lista in self.__listas_de_reproduccion:
            nombre_lista_a_comparar = lista["nombre"]
            if nombre_lista_nueva.lower() == nombre_lista_a_comparar.lower():
                nombre_lista_disponible = False
        if nombre_lista_disponible:
            lista_nueva = []
            self.__listas_de_reproduccion.append({"nombre": nombre_lista_nueva, "lista": lista_nueva})
            print("Lista creada exitosamente!")
            print()
        else:
            print()
            print("El nombre de la lista está ocupado")
            print()
            
    def BuscarEnLista(self):
        contenido_en_lista = False
        retorno = None # retorno por defecto
        if len(self.__listas_de_reproduccion) > 0: # revisa si hay contenido en la lista 
            contenido_en_lista = True
        else:
            print("No hay listas de reproducción disponibles")
            print()
        
        if contenido_en_lista: # revisa si hay contenido en la lista 
            print("Listas disponibles:")
            for lista in self.__listas_de_reproduccion:
                nombre_lista = lista.get("nombre")
                print(nombre_lista)  # Muestra los nombres de las listas de reproducción

            titulo_lista_a_buscar = input("Ingresa el título de la lista: ")  # Solicita el nombre de la lista de reproducción a buscar
            print()
            lista_reproduccion = self.getListaReproduccion(titulo_lista_a_buscar)

            contenido_en_lista_repoduccion = False
            if len(lista_reproduccion) > 0:# revisa si hay contenido en la lista 
                contenido_en_lista_repoduccion = True
            else:
                print("La lista de reproducción está vacía")
                print()
            
            if contenido_en_lista_repoduccion: # revisa si hay contenido en la lista de reproduccion
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

                if busqueda_existosa: # si la cancion se encontro se retorna 
                    retorno = cancion_encontrada
                else: 
                    print("El título no se encuentra")
                    print()               
        return retorno

    # Funcion para mostrar las notificaciones del sistema
    def MostrarNotificaciones(self, lista):
        salir = False
        while not salir:
            self.__notificaciones_leidas = True
            print()
            print("Notificaciones: ")
            print()
            for notificaion in lista:
                print(notificaion)
                print()
            try:
                print()
                opcion = int(input("Escribe 1 para salrir: "))  # Solicita al usuario que ingrese una opción
                print()
                if opcion == 1:
                    salir = True
                else:
                    print("La opcion no es valida")
            except ValueError:
                print()
                print("Error: No has ingresado un número entero válido.")

    def getNombre(self):
        # Método para obtener el nombre de la cuenta
        return self.__nombre

    def getListasDeReproduccion(self):
        # Método para obtener una lista de todas las listas de reproducción
        return self.__listas_de_reproduccion

    def getListaReproduccion(self, nombre_lista_a_buscar):
        # Método para obtener una lista de reproducción específica en función de su nombre
        lista_a_retornar = []
        for elemento in self.__listas_de_reproduccion:
            nombre_lista = elemento.get("nombre")
            if nombre_lista_a_buscar.lower() == nombre_lista.lower():
                lista_a_retornar = elemento.get("lista")
        return lista_a_retornar
    
    def getNotificacionesLeidas(self):
        return self.__notificaciones_leidas
