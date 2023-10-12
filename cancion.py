class Cancion:
# Método constructor de la clase Canción, inicializa los atributos compartidos de las canciones
    def __init__(self, titulo, duracion, artista, album):
        self.__duracion = duracion
        self.__titulo = titulo # Título del video
        self.__artista = artista # director de la canción
        self.__album = album # Clasificación de la canción
        
    # metodo que regresa una cadena con la informacion de la canción
    def __str__(self):
        return f"Titulo: {self.__titulo}, Artista: {self.__artista}, Album: {self.__album}"

    # metodo que proporciona el Titulo
    def getTitulo(self):
        return self.__titulo
    
    # Metodo que proporciona la duracion de la cancion
    def getDuracion(self):
        return self.__duracion

    # metodo que proporciona el Artista
    def getArtista(self):
        return self.__artista

    # metodo que proporciona el Album
    def getAlbum(self):
        return self.__album
    
    def Reproducir(self):
        print()
        print("Reproduciendo: " + self.__titulo)
        print("Artista: " + self.__artista)
        print("Almbum: " + self.__album)
        print()
            

        