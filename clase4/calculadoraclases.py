'''     Vamos a hacer una calculador practicando clases!!!      '''


class calculadora:
    def __init__(self):
        self.operadores = ['+', '-', '**', '/', '*']

    def calcular(self, num1, num2, i):
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

    def iniciar_calculadora(self):
        while True:
            inp = input('Operación: ')
            invalido = True
            for i, operador in enumerate(self.operadores):
                if operador in inp:
                    invalido = False
                    numeros = inp.split(operador)
                    num1 = int(numeros[0].strip())
                    num2 = int(numeros[1].strip())
                    result = self.calcular(num1, num2, i)
                    print(f'{num1} {operador} {num2} = {result}')
                    break

            if invalido:
                print('Operación inválida')
            q = input('Quiere hacer otra cuenta?(q para salir)')
            if q.lower() == 'q':
                break
    
    def multi_calcular(self):
        pass

cal = calculadora()
cal.iniciar_calculadora()
