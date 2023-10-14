class Cancion:
    # Método constructor de la clase Canción, inicializa los atributos compartidos de las canciones
    def __init__(self, titulo, duracion, artista, album):
        self.__titulo = titulo  # Título de la canción
        self.__duracion = duracion # duracion de la cancion
        self.__artista = artista  # Artista de la canción
        self.__album = album  # Álbum de la canción

    # Método que regresa una cadena con la información de la canción
    def __str__(self):
        return f"Título: {self.__titulo}, Artista: {self.__artista}, Álbum: {self.__album}"

    # Método que proporciona el título de la canción
    def getTitulo(self):
        return self.__titulo

    # Método que proporciona la duración de la canción
    def getDuracion(self):
        return self.__duracion

    # Método que proporciona el artista de la canción
    def getArtista(self):
        return self.__artista

    # Método que proporciona el álbum de la canción
    def getAlbum(self):
        return self.__album

    def Reproducir(self):
        # Método que simula la reproducción de la canción e imprime información sobre la canción
        print()
        print("Reproduciendo: " + self.__titulo)
        print("Artista: " + self.__artista)
        print("Álbum: " + self.__album)
        print()
