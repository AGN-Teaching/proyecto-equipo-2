# Importa la clase 'Streaming' desde el módulo 'streaming'
from streaming import Streaming


# Define una función llamada 'Main'
def Main():
    # Crea una instancia de la clase 'Streaming' y almacénala en la variable 'Servicio'
    Servicio = Streaming()

    # Carga un catálogo de datos desde un archivo llamado 'Catalogo.json'
    Servicio.CargarCatalogo("Catalogo.json")

    # Inicializa una variable 'Salir' como 'False' para controlar la ejecución del programa
    Salir = False

    # Comienza un bucle while que se ejecutará hasta que 'Salir' sea True
    while not Salir:
        # Obtiene una lista de clientes desde el servicio de streaming
        lista_clientes = Servicio.getClientes()

        # Muestra un menú principal en la consola
        print("Menú Principal")
        print("1. Acceder con usuario")
        print("2. Contratar plan")
        print("3. Salir")

        try:
            print()
            # Espera a que el usuario ingrese una opción y la almacena como un número entero en 'opcion'
            opcion = int(input("Ingresa una opción: "))
            print()
        except ValueError:
            # En caso de que el usuario no ingrese un número válido, muestra un mensaje de error
            print("Error: No has ingresado un número entero válido.")
            print()
            # Establece 'opcion' en 4 como un valor predeterminado
            opcion = 4

        # Verifica la opción seleccionada por el usuario
        if opcion == 1:
            # Comprueba si hay clientes registrados
            if len(lista_clientes) > 0:
                # Solicita al usuario que ingrese el nombre del cliente a buscar
                nombre_Cliente_a_buscar = input("Ingresa el nombre del usuario: ")
                print()
                usuario_existe = False

                # Recorre la lista de clientes para buscar un cliente con el nombre ingresado
                for Cliente in lista_clientes:
                    nombre_cliente = Cliente.getNombre()

                    # Compara el nombre ingresado (sin importar mayúsculas/minúsculas) con el nombre del cliente actual
                    if nombre_Cliente_a_buscar.lower() == nombre_cliente.lower():
                        # Si se encuentra un cliente con el nombre dado, muestra un menú relacionado con el plan del cliente
                        Servicio.MenuPlan(Cliente)
                        usuario_existe = True

                # Si no se encontró al cliente, muestra un mensaje de que el usuario no existe
                if not usuario_existe:
                    print("El usuario no existe")
                    print()
            else:
                # Si no hay usuarios registrados, muestra un mensaje correspondiente
                print("No hay usuarios registrados")
                print()
        elif opcion == 2:
            # Si la opción es 2, llama a una función llamada 'MenúContratarPlan' en el servicio de streaming
            Servicio.MenúContratarPlan()
        elif opcion == 3:
            # Si la opción es 3, establece 'Salir' en True para salir del bucle while y terminar el programa
            Salir = True
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print("La opción es inválida, inténtalo de nuevo")
            print()


# Llama a la función 'Main' para comenzar la ejecución del programa
Main()
