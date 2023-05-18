hola = 2
c = 3
print(hola)
# se pueden encadenar metodos
animal = ' chanchito feliz'
print(animal.strip().capitalize())
print(animal.strip().find('h'))
print(animal.replace('ch', 'j'))
print('ch' in animal)
print('\'\ \n \\ ')

# condicional ternario
edad = 18
mensaje = 'Es mayor' if edad > 17 else 'es menor'
print(mensaje)

# and, or, not
# condicional doble: hay que poner parentesis a la condición...
# if gas and (encendido or edad > 17):

# Diccionarios
diccionario = {'azul': 'blue', 'rojo': 'red', 'verde': 'green'}

diccionario['amarillo'] = 'yellow'

del (diccionario['amarillo'])


print(diccionario)

diccionario = {'alejandro': [22, 2.73], 'juan': [29, 1.87]}

diccionario = {'alejandro': {'edad': 22, 'altura': 2.73}, 'juan': [29, 1.87]}

print(diccionario['alejandro']['edad'])

# Crear clases:


class coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arracado = False

    def arrancar(self):
        self.arrancado = True
        print('El ', self.marca, self.modelo, ' se ha arrancado.')

    def apagar(self):
        self.arrancado = False
        print('El ', self.marca, self.modelo, ' se ha apagado.')


laguna = coche('tesla', 't4')
print(type(laguna))
print(laguna.marca)
laguna.arrancar()
laguna.apagar()

# Herencia de clases


class supercoche(coche):
    super = 'premium'
    publicidad = False


bugati = supercoche('bugati', 'veyron')
bugati.arrancar()


class ultracoche(supercoche):
    mas_millon = True

lambo=ultracoche('lamborghini', 'Gallardo')
lambo.arrancar()
print(lambo.mas_millon)