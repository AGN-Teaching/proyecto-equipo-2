
class Cuenta():
    
    def __init__(self, nombre, anuncio):
        self.__anuncio = anuncio
        self.__nombre = nombre
        self.__listas_de_reproduciion = []
        
    
        
    def AgregarCancion(self, cancion):
        Salir = False
        
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
                    if len(self.__listas_de_reproduciion) > 0:
                        print("Listas disponibles")
                        for elemento in self.__listas_de_reproduciion:
                            nombre_lista = elemento.get("nombre")
                            print(nombre_lista)
                        print()
                        nombre_lista_de_reproduccion_a_buscar = input("ingresa el nombre de la lista: ")
                        print()
                        lista_encontrada = False
                        for elemento in self.__listas_de_reproduciion:
                            nombre_lista = elemento["nombre"]
                            if nombre_lista_de_reproduccion_a_buscar.lower() == nombre_lista.lower():
                                lista_encontrada = True
                                lista = elemento["lista"]
                                lista.append(cancion)
                        if lista_encontrada:
                            print("¡Cancion agregada exitosamente!")
                            print()
                            Salir = True
                        else:
                            print("La lista no se encuentra")
                    else:
                        print("No hay listas de reproduccion, crea una nueva")
                        print()
                        
                elif opcion == 2:
                    nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
                    print()
                    nombre_lista_disponible = True
                    for lista in self.__listas_de_reproduciion:
                        nombre_lista_a_comparar = lista["nombre"]
                        if nombre_lista_nueva.lower() ==  nombre_lista_a_comparar.lower():
                            nombre_lista_disponible = False
                    if nombre_lista_disponible: 
                        lista_nueva = []
                        lista_nueva.append(cancion)
                        self.__listas_de_reproduciion.append({"nombre": nombre_lista_nueva, "lista" : lista_nueva})
                        print("Cancion agregada a la lista nueva")
                        print()
                    else:
                        print()
                        print("El nombre de la lista esta ocupado")
                        print()
                elif opcion == 3:
                    Salir =True
                else:
                    print("La opcion es invalida ")
                    print()
            except ValueError:
                print("Error: No has ingresado una opcion.")
                print()
                    
            
        
    
    def CrearListaDeReproduccion(self):
        nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
        print()
        nombre_lista_disponible = True
        for lista in self.__listas_de_reproduciion:
            nombre_lista_a_comparar = lista["nombre"]
            if nombre_lista_nueva.lower() ==  nombre_lista_a_comparar.lower():
                nombre_lista_disponible = False
        if nombre_lista_disponible: 
            lista_nueva = []
            self.__listas_de_reproduciion.append({"nombre": nombre_lista_nueva, "lista" : lista_nueva})
            print("Lista Creada exitosamente!")
            print()
        else:
            print()
            print("El nombre de la lista esta ocupado")
            print()
        
    def getAnuncio(self):
        return self.__anuncio   
        
    def getNombre(self):
        return self.__nombre
    
    def getListasDeReproduccion(self):
        return self.__listas_de_reproduciion
    
    def getListaReproduccion(self, nombre_lista_a_buscar):
        lista_a_retornar = []
        for elemento  in self.__listas_de_reproduciion:
            nombre_lista = elemento.get("nombre")
            if nombre_lista_a_buscar.lower() == nombre_lista.lower():
                lista_a_retornar = elemento.get("lista")
        return lista_a_retornar
                
                        