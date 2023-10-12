from cancion import Cancion
import json 

class CuentaUsuarioGratuito():
    
    def __init__(self, nombre):
        self.__anuncio = True
        self.__nombre = nombre
        self.__catalogo = []
        self.__listas_de_reproduciion = []
        
    
        
    def AgregarCancion(self, cancion):
        Salir = False
        
        while not Salir:
            print("Opciones: ")
            print("1. Agregar a lista de reproduccion existente")
            print("1. Agregar a una lista de reproduccion nueva ")
            print("3. Regresar")
            print()
            opcion = input("Elige una opción")
            if opcion == 1:
                if not self.__listas_de_reproduciion:
                    print("No hay listas de reproduccion, crea una nueva")
                else:
                    print("Listas disponibles")
                    for elemento in self.__listas_de_reproduciion:
                        nombre_lista = elemento.get("nombre")
                        print(nombre_lista)
                    nombre_lista_de_reproduccion_a_buscar = input("ingresa el nombre de la lista ")
                    for elemento in self.__listas_de_reproduciion:
                        nombre_lista = elemento.get("nombre")
                        if nombre_lista_de_reproduccion_a_buscar.lower() == nombre_lista.lower():
                            elemento["lista"].append(cancion)
                            print("¡Cancion agregada exitosamente!")
                            Salir = True
            elif opcion == 2:
                nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
                lista_nueva = []
                self.__listas_de_reproduciion.append({"nombre": nombre_lista_nueva, "lista" : lista_nueva})
            elif opcion == 3:
                Salir =True
            else:
                print("La opcion es invalida ")
        
    
    def CrearListaDeReproduccion(self):
        nombre_lista_nueva = input("Ingresa el nombre de la lista nueva: ")
        lista_nueva = []
        self.__listas_de_reproduciion.append({"nombre": nombre_lista_nueva, "lista" : lista_nueva})
        print("Lista Creada exitosamente!")
        
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
                
                        