# |————————————————————————————————————————————————————————————————————|
# |          Proyecto final Programación Orientada a objetos           |
# |                     Juan Daniel Valencia Henao                     |
# |                         Inyer Marín Medina                         |
# |                 Universidad Tecnológica de Pereira                 |
# |                                2021                                |
# |————————————————————————————————————————————————————————————————————|


#clase vehiculo
class Vehiculo:
    
    #constructor
    def __init__(self, placa, marca, color, tipo):
        self.__placa = placa
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo

    
    #metodos
    def getPlaca(self):
        return self.__placa 
    
    def getMarca(self):
        return self.__marca
    
    def getColor(self):
        return self.__color
    
    def getTipo(self):
        return self.__tipo
    
     
#clases hijas de Vehiculo
class Camioneta(Vehiculo):
    
    pass

class Deportivo(Vehiculo):
    
    pass

class Clasico(Vehiculo):
    
    pass

#clase moto, hija de vehiculo
class Moto(Vehiculo):
    
    def __init__(self, placa, marca, color, tipo):
        Vehiculo.__init__(self, placa, marca, color, tipo)
        

#clases hijas de Moto
class Moto_AltoCC(Moto):
    
    pass

class Moto_BajoCC(Moto):
    
    pass


#Clase para crear los usuarios 
class Usuarios():
    
    #constructor con variables encapsuladas
    def __init__(self, usuario, password):
        self.__nombre_usuario = usuario
        self.__contrasena = password
    
    #metodos
    def getUser(self):
        return self.__nombre_usuario
    
    def getPass(self):
        return self.__contrasena

    




