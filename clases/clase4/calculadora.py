'''     Vamos a crear una calculadora!      '''

operadores = ['+', '-', '**', '/', '*']


def calcular(num1, num2, operador):
    result = None
    if i == 0:
        result = num1+num2
    elif i == 1:
        result = num1 - num2
    elif i == 2:
        result = num1 ** num2
    elif i == 3:
        if num2 != 0:
            result = num1 / num2
        else:
            return 'No se divide por 0'
    elif i == 4:
        result = num1 * num2
    return result


while True:
    inp = input('Operación: ')
    # Enumerate te devuelve (indice, valor) de una lista
    for i, operador in enumerate(operadores):
        if operador in inp:
            numeros = inp.split(operador)
            num1 = int(numeros[0].strip())
            num2 = int(numeros[1].strip())
            result = calcular(num1, num2, operador)
            print(f'{num1} {operador} {num2} = {result}')
            break

    q = input('Quiere hacer otra cuenta?(q para salir)')
    if q == 'q':
        break
