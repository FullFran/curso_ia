class animal:
    def __init__(self, Reino, regiones, Poblacion):
        self.Reino = Reino
        self.Regiones_habita = regiones
        self.Poblacion = Poblacion

        def hablar(self):
            pass  # cada bisho habla de una forma, ya lo llenaremos.


class mamifero(animal):
    def __init__(self, reino, regiones, poblacion, filo):
        super().__init__(reino, regiones, poblacion)
        self.filo = filo


class perro(mamifero):
    def __init__(self, nombre, edad, genero):
        super().__init__('Animalia', ['europa', 'africa', 'asia', 'america'],
                         50000000, 'chordata')
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def hablar(self):
        print('guau guau')


class gato(mamifero):
    def __init__(self, nombre, edad, genero):
        super().__init__('Animalia', ['europa', 'africa', 'asia', 'america'],
                         50000000, 'chordata')
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def hablar(self):
        print('miau miau')


class jauria:
    def __init__(self):
        self.perros = []

    def agregar_perro(self, perro):
        self.perros.append(perro)

    def mostrar_jauria(self):
        for perro in self.perros:
            print(
                f'Nombre: {perro.nombre} Edad: {perro.edad} Genero: {perro.genero}')

    def guardar_txt(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            for perro in self.perros:
                lin = f'{perro.nombre}, {perro.edad}, {perro.genero}\n'
                f.write(lin)

    def crear_txt(self, nombre_archivo):
        Jauria = jauria()
        with open(nombre_archivo, 'r') as f:
            for lin in f:
                datos = lin.strip().split(',')
                nombre = datos[0]
                edad = int(datos[1])
                genero = datos[2]
                Perro = perro(nombre, edad, genero)
                Jauria.agregar_perro(Perro)
            return Jauria


'''------------------------------HACEMOS PRUEBAS----------------------------------------'''
print('Estos son los sonidos:')
miau = gato('miau', 3, 'F')
miau.hablar()
guts = perro('Guts', 1, 'M')
guts.hablar()
print('\n Ahora creamos y guardamos en .txt:')


los_chavales = jauria()
juan = perro('Juan', 23, 'M')
ivan = perro('Ivan', 22, 'M')
guts = perro('Guts', 1, 'M')
los_chavales.agregar_perro(juan)
los_chavales.agregar_perro(ivan)
los_chavales.agregar_perro(guts)
los_chavales.mostrar_jauria()

los_chavales.guardar_txt('loschavales.txt')

print('\n Ahora creamos a partir del .txt:')
chavales = jauria().crear_txt('loschavales.txt')
chavales.mostrar_jauria()
