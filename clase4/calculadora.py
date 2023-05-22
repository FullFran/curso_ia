'''     Vamos a crear una calculadora!      '''


operadores = ['+', '-', '*', '/', '**']

while True:
    inp = input('Operación: ')
    for i, operador in enumerate(operadores): # Enumerate te devuelve (indice, valor) de una lista
        if operador in inp:
            numeros = inp.split(operador)
            num1 = int(numeros[0].strip())
            num2 = int(numeros[1].strip())

            result = None

            if i == 0:
                result = num1+num2
            elif i == 1:
                result = num1 - num2
            elif i == 2:
                result = num1 * num2
            elif i == 3:
                result = num1 / num2
            elif i == 4:
                result = num1 ** num2

            print(f'{num1}\n{operador}\n{num2}\nresultado = {result}')

    q = input('Quiere hacer otra cuenta?(q para salir)')
    if q == 'q':
        break
