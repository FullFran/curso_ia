
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

# Vamos a definir también la suma de vectores.


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

    def __mul__(self, v):
        new_vector = vector(0, 0, 0)

        if isinstance(v, float) or isinstance(v, int):
            new_vector.__x = float(self.__x * v)
            new_vector.__y = float(self.__y * v)
            new_vector.__z = float(self.__z * v)
            return (new_vector)
        elif isinstance(v, vector):
            return self.__x * v.__x + self.__y * v.__y + self.__z * v.__z

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

# ---------Lo Probamos----------------------------------------------


print('Creamos vectores e imprimimos el primero.')
v1 = vector(1, 1, 0)
v2 = vector(0, 0, 1)
v3 = vector(-1, 1, 0)
print(v1.imprimir_vector())

print('\nAñadimos vectores a un .txt')
v1.meter_txt('clase4/vecs.txt')
v2.meter_txt('clase4/vecs.txt')
v3.meter_txt('clase4/vecs.txt')

print('\nCargamos los vectores desde un archivo')
vectores = hacer_vector('clase4/baseortonormal.txt')

for v in vectores:
    print(v.imprimir_vector())


print('\nVamos a sumar vectores')
print((v1.__add__(v2)).imprimir_vector())
print((v1+v2).imprimir_vector())

print('\nVamos a restar vectores')
print((v1.__sub__(v2)).imprimir_vector())
print((v1-v2).imprimir_vector())

print('\nVamos a multiplicar vectores escalarmente')
# Hemos puesto esto porque los hice linealmente independientes XD
print(((v1+v3).__mul__(v3)))
print((v1+v3)*v3)

print('\nVamos a multiplicar vectores por un escalar')
print((v1.__mul__(2)).imprimir_vector())
print((v1*2).imprimir_vector())
