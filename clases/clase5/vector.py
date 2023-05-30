'''Esto es una librería que vamos a importar que contiene la clase vector con sus 
métodos y operaciones y una función para leer vectores'''
import numpy as np


class vector():
    def __init__(self, x, y, z):
        self.__x = float(x)
        self.__y = float(y)   # asi nos aseguramos de meterle un float
        self.__z = float(z)

    # Overwrite de operadores
    def __add__(self, v):
        new_vector = vector(0, 0, 0)
        new_vector.__x = float(self.__x + v.__x)
        new_vector.__y = float(self.__y + v.__y)
        new_vector.__z = float(self.__z + v.__z)
        return (new_vector)

    def __sub__(self, v):
        new_vector = vector(0, 0, 0)
        new_vector.__x = float(self.__x - v.__x)
        new_vector.__y = float(self.__y - v.__y)
        new_vector.__z = float(self.__z - v.__z)
        return new_vector

    def metric(self):
        return np.sqrt(self.__x**2+self.__y**2+self.__z**2)

    def angle(self, v):
        return np.arccos(self.__mul__(v)/(v.metric()*self.metric()))

    def __mul__(self, v):
        new_vector = vector(0, 0, 0)

        if isinstance(v, float) or isinstance(v, int):
            new_vector.__x = float(self.__x * v)
            new_vector.__y = float(self.__y * v)
            new_vector.__z = float(self.__z * v)
            return (new_vector)
        elif isinstance(v, vector):
            return self.__x * v.__x + self.__y * v.__y + self.__z * v.__z

    def crossmul(self, v):
        new_vector = vector(self.__y * v.__z - self.__z * v.__y,
                            self.__z * v.__x - self.__x * v.__z,
                            self.__x * v.__y - self.__y * v.__x)
        return new_vector

    def imprimir_vector(self):
        return f'({self.__x},{self.__y},{self.__z})'

    def meter_txt(self, archivo):
        with open(archivo, 'a') as f:
            f.write(f'{self.imprimir_vector()}\n')
        # acordarse de que hay que poner formatos compatibles.


def hacer_vector(archivo):
    # acordarse de que hay que poner formatos compatibles.
    vs = []
    with open(archivo, 'r') as f:
        for line in f:
            cor = line.strip().replace('(', '').replace(')', '').split(',')

            if len(cor) == 3:
                v = vector(cor[0], cor[1], cor[2])
                vs.append(v)
    return vs


v1 = vector(1, 0, 0)
v2 = vector(0, 1, 0)

v3 = v1.angle(v2)
print(v3/np.pi, 'pi')
