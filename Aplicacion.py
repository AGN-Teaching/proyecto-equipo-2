from cuenta_usuario_gratuito import CuentaUsuarioGratuito
from cuenta_usuario_paga import Cuenta_usuario_paga
from cancion import Cancion
from cliente import Cliente
from streaming import Streaming


def Main():
    Servicio = Streaming()
    Servicio.CargarCatalogo("Catalogo.json")
    Salir = False
    while not Salir:
        lista_clientes = Servicio.getClientes()
        print("Menú Principal")
        print("1. Acceder con usuario")
        print("2. Contratar plan")
        print("3. Salir")
        try:
            print()
            opcion = int(input("Ingresa una opcion: "))
            print()
        except ValueError:
            print("Error: No has ingresado un número entero válido.")
            print()
            opcion = 4
        if opcion == 1:
            if (lista_clientes) > 0:
                nombre_Cliente_a_buscar = input("Ingresa el nombre del usuario: ")
                print()
                usuario_existe = False
                for Cliente in lista_clientes:
                    nombre_cliente = Cliente.getNombre()
                    if nombre_Cliente_a_buscar.lower() == nombre_cliente.lower():
                        Servicio.MenuPlan(Cliente)
                        usuario_existe = True
                        
                if usuario_existe:
                    print("El usuario no existe")
                    print()
            else:
                print("No hay usuarios registrados")
                print()
        elif opcion == 2:
            Servicio.MenúContratarPlan()
        elif opcion == 3:
            Salir = True
        else:
            print("La opcion es invalida, intenta de nuevo")
            print()
            
Main()