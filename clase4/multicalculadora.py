class calculadora:
    def __init__(self):
        self.operadores = ['+', '-', '**', '/', '*']

    def calcular(self, num1, num2, operador):
        result = None
        if operador == '+':
            result = num1 + num2
        elif operador == '-':
            result = num1 - num2
        elif operador == '**':
            result = num1 ** num2
        elif operador == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return 'No se divide por 0'
        elif operador == '*':
            result = num1 * num2
        return result

    def iniciar_calculadora(self):
        while True:
            inp = input('Operación: ')
            invalido = True
            for operador in self.operadores:
                if operador in inp:
                    invalido = False
                    numeros = inp.split(operador)
                    num1 = int(numeros[0].strip())
                    num2 = int(numeros[1].strip())
                    result = self.calcular(num1, num2, operador)
                    print(f'{num1} {operador} {num2} = {result}')
                    break

            if invalido:
                print('Operación inválida')
            q = input('Quiere hacer otra cuenta?(q para salir)')
            if q.lower() == 'q':
                break

    def iniciar_multi_calculadora(self):
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

    def multi_calcular(self, syms):
        result = 0
        op_aux = None
        num_aux = 0
        for num in syms:
            if num.isnumeric():
                num_aux = int(num)
                if op_aux is None:
                    result = num_aux
                else:
                    result = self.calcular(result, num_aux, op_aux)
                continue

            if num in self.operadores:
                op_aux = num
                continue
        return result


cal = calculadora()

a = cal.multi_calcular(['3', '+', '4', '-', '5'])
print(a)

cal.iniciar_calculadora()
