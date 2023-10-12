from cuenta_usuario_gratuito import CuentaUsuarioGratuito

class Cuenta_usuario_paga(CuentaUsuarioGratuito):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.anuncio = False