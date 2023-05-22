
'''
Crear una clase vector que tenga tres atributos privados (x, y,  z) y además los siguientes métodos:
Un constructor al que se le pasan 3 números tipo float para cada atributo correspondiente
a) Un método público para imprimir el vector con el formato siguiente, por ejemplo:
(12.34, 3, -17.9)
b) Un método que apende un vector a un archivo de texto (.txt)
c) Una función fuera de la clase, que lea un archivo con uno o más vectores y cree tantos objetos tipo vector como puntos haya. Llamar a la función e imprimir todos los vectores.
Ejemplo de archivo:
12 3.5 -1
23.4 -4 89
1 1 1

Nota: acordarse de que en el método de escribir en un archivo y en esta función hay que poner formatos de string compatibles.
'''


class vector():
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def imprimir_vector(self):
        print(f'({self.__x},{self.__x},{self.__x})')

    def meter_txt(self):
        pass
        # acordarse de que hay que poner formatos compatibles.


def hacer_vector(*args):
    # acordarse de que hay que poner formatos compatibles.
    pass
