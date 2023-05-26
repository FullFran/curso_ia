'''----- Antes de nada tenemos que tener aquí la base de datos de clientes y pedidos que creamos
    -----en el ejercicio anterior.'''

# vamos a crear una 'base de datos' de nuestros clientes y nuestros
# pedidos primero para hacer el ejercicio.

import uuid

clientes = [
    {
        'nombre': 'Pedro',
        'apellidos': 'Cuenca',
        'ID': str(uuid.uuid4().int)[:7],
        'dinero_gastado': 0.0,
        'num_pedidos': 0,
        'pedidos': []
    },
    {
        'nombre': 'Ana',
        'apellidos': 'Martínez',
        'ID': str(uuid.uuid4().int)[:7],
        'dinero_gastado': 0.0,
        'num_pedidos': 0,
        'pedidos': []
    },
    {
        'nombre': 'Alicia',
        'apellidos': 'Romero',
        'ID': str(uuid.uuid4().int)[:7],
        'dinero_gastado': 0.0,
        'num_pedidos': 0,
        'pedidos': []
    },
    # Agrega más clientes si es necesario
]

# Creamos otra lista de  diccionarios con los pedidos

pedidos = [
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-18',
        'codigo_cliente': clientes[0]['ID'],
        'importe_total': 100.0
    },
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-17',
        'codigo_cliente': clientes[0]['ID'],
        'importe_total': 150.0
    },
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-16',
        'codigo_cliente': clientes[1]['ID'],
        'importe_total': 200.0
    },
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-16',
        'codigo_cliente': clientes[1]['ID'],
        'importe_total': 50.0
    },
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-16',
        'codigo_cliente': clientes[1]['ID'],
        'importe_total': 100.0
    },
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-16',
        'codigo_cliente': clientes[2]['ID'],
        'importe_total': 200.0
    },
    {
        'codigo_pedido': str(uuid.uuid4().int)[:7],
        'fecha': '2023-05-16',
        'codigo_cliente': clientes[2]['ID'],
        'importe_total': 300.0
    },
]


# a) Creamos una función para rellenar el campo pedidos de los clientes.
def rellenar_pedidos(clientes=clientes, pedidos=pedidos):
    '''Aquí rellenamos los pedidos de los clientes\n
        modificando también el dinero gastado\n
        y el número de pedidos.'''
    clientes_aux = clientes
    for cliente in clientes_aux:
        ids = []
        for ped in cliente['pedidos']:
            ids.append(ped['codigo_pedido'])
        for pedido in pedidos:
            if pedido['codigo_cliente'] == cliente['ID'] and pedido['codigo_pedido'] not in ids:
                cliente['pedidos'].append(pedido)
                cliente['dinero_gastado'] += pedido['importe_total']
                cliente['num_pedidos'] += 1


# b) Una función de ordenación de los clientes por los campos dados en el ejercicio anterior


def ordenar(clientes, clave='nombre'):
    '''Claves válidas: 'Numero de pedidos' 'Número de pedidos' 'pedidos' \n
                        'nombre' (clave por defecto) \n
                        'apellidos' \n
                         'dinero_gastado' '''
    if clave == 'Numero de pedidos' or clave == 'Número de pedidos' or clave == 'pedidos' or clave == 'num_pedidos':
        return sorted(clientes, key=lambda i: i['num_pedidos'], reverse=True)
    try:
        return sorted(clientes, key=lambda i: i[clave])
    except:
        print('ERROR: Posiblemente elegiste una clave que no existe')

# c) Una función que calcule el total de pedidos y el dinero gastado por un cliente si estos campos no estuviesen rellenados


def r_num_pedios_dinero(cliente):
    '''Esta función rellena el numero de pedidos\n
        y el dinero gastado si estos campos están vacíos.'''
    if cliente['num_pedidos'] == 0:
        for pedido in cliente['pedidos']:
            cliente['dinero_gastado'] += pedido['importe_total']
            cliente['num_pedidos'] += 1


'''
d) Con la función anterior, crear una función que añada un nuevo pedido a la
lista de pedidos y al cliente correspondiente y actualice los campos
necesarios de dicho cliente.
'''


def nuevo_pedido(pedido, pedidos=pedidos, clientes=clientes):
    '''Esta función añade un nuevo pedido a la lista de pedidos\n
        después rellena los pedidos de los clientes para añadir\n
        el nuevo pedido.'''
    pedidos.append(pedido)
    rellenar_pedidos(clientes, pedidos)


'''
e) Una función que añada un nuevo cliente pasándole solamente el nombre y
los apellidos.
'''


def nuevo_cliente(nombre, apellidos):
    cliente = {
        'nombre': str(nombre).capitalize(),
        'apellidos': str(apellidos).title(),
        'ID': str(uuid.uuid4().int)[:7],
        'dinero_gastado': 0.0,
        'num_pedidos': 0,
        'pedidos': []
    }
    clientes.append(cliente)


'''
f) Una función que visualice un cliente con el siguiente formato

Nombre: Pepe

Apellidos: García González

ID: 000345

Número de pedidos: 4

Dinero gastado: 94.57€

Fecha del último pedido: 4.8.2022
'''


def ver_cliente(cliente):
    texto = str(cliente).replace('{', '').replace('}', '').replace('\'', '').replace(
        'num_pedidos', f'Número de pedidos').replace('_', f' ').split(',')[:5]
    texto[3] += '€'
    for t in texto:
        print(f'{t.strip().title()}')
    try:
        ped = ordenar(cliente['pedidos'], clave='fecha')

        print('Fecha del último pedido: ',
              ped[-1]['fecha'].replace('-', f'.'), '\n')
    except:
        print('No hay pedidos.\n')


''' Aquí meto una prueba de alguna cosa'''

nuevo_cliente('Pedro', 'García')

rellenar_pedidos()

for cliente in clientes:
    ver_cliente(cliente)
