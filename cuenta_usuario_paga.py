from cuenta_usuario_gratuito import CuentaUsuarioGratuito

class Cuenta_usuario_paga(CuentaUsuarioGratuito):

    def __init__(self):
        super().__init__()
        self.anuncio = False

