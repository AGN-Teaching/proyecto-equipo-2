class Cuenta():

    def __init__(self, nombre, anuncio):
        # Constructor: inicializa la cuenta con nombre y anuncio
        self.__anuncio = anuncio
        self.__nombre = nombre
        self.__listas_de_reproduccion = []

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
                if opcion == 1:
                    # Agregar a lista de reproducción existente
                    if len(self.__listas_de_reproduciion) > 0:
                        print("Listas disponibles")
                        # Mostrar las listas de reproducción existentes
                        for elemento in self.__listas_de_reproduciion:
                            nombre_lista = elemento.get("nombre")
                            print(nombre_lista)
                        print()
                        nombre_lista_de_reproduccion_a_buscar = input("Ingresa el nombre de la lista: ")
                        print()
                        lista_encontrada = False
                        for elemento in self.__listas_de_reproduciion:
                            nombre_lista = elemento["nombre"]
                            if nombre_lista_de_reproduccion_a_buscar.lower() == nombre_lista.lower():
                                lista_encontrada = True
                                lista = elemento["lista"]
                                lista.append(cancion)
                        if lista_encontrada:
                            print("¡Canción agregada exitosamente!")
                            print()
                            Salir = True
                        else:
                            print("La lista no se encuentra")
                    else:
                        print("No hay listas de reproducción, crea una nueva")
                        print()
                elif opcion == 2:
                    # Agregar a una lista de reproducción nueva
                    nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
                    print()
                    nombre_lista_disponible = True
                    for lista in self.__listas_de_reproduciion:
                        nombre_lista_a_comparar = lista["nombre"]
                        if nombre_lista_nueva.lower() == nombre_lista_a_comparar.lower():
                            nombre_lista_disponible = False
                    if nombre_lista_disponible:
                        lista_nueva = []
                        lista_nueva.append(cancion)
                        self.__listas_de_reproduciion.append({"nombre": nombre_lista_nueva, "lista": lista_nueva})
                        print("Canción agregada a la lista nueva")
                        print()
                    else:
                        print()
                        print("El nombre de la lista está ocupado")
                        print()
                elif opcion == 3:
                    Salir = True
                else:
                    print("La opción es inválida ")
                    print()
            except ValueError:
                print("Error: No has ingresado una opción.")
                print()

    def CrearListaDeReproduccion(self):
        # Método para crear una nueva lista de reproducción
        nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
        print()
        nombre_lista_disponible = True
        for lista in self.__listas_de_reproduciion:
            nombre_lista_a_comparar = lista["nombre"]
            if nombre_lista_nueva.lower() == nombre_lista_a_comparar.lower():
                nombre_lista_disponible = False
        if nombre_lista_disponible:
            lista_nueva = []
            self.__listas_de_reproduciion.append({"nombre": nombre_lista_nueva, "lista": lista_nueva})
            print("Lista creada exitosamente!")
            print()
        else:
            print()
            print("El nombre de la lista está ocupado")
            print()

    def getAnuncio(self):
        # Método para obtener el anuncio de la cuenta
        return self.__anuncio

    def getNombre(self):
        # Método para obtener el nombre de la cuenta
        return self.__nombre

    def getListasDeReproduccion(self):
        # Método para obtener una lista de todas las listas de reproducción
        return self.__listas_de_reproduciion

    def getListaReproduccion(self, nombre_lista_a_buscar):
        # Método para obtener una lista de reproducción específica en función de su nombre
        lista_a_retornar = []
        for elemento in self.__listas_de_reproduciion:
            nombre_lista = elemento.get("nombre")
            if nombre_lista_a_buscar.lower() == nombre_lista.lower():
                lista_a_retornar = elemento.get("lista")
        return lista_a_retornar
