SERIE CONTINUA

ALTERNA EN SERIE

EJERCICO DEL TIPO:

    LOS QUE MANDÓ
    POSIBLEMENTE EL DE PRIMER ORDEN
    DOS DE PRIMER ORDEN.

DE SEGUNDO ORDEN:

    TRASITORIO DE LOS DEL TIPO

DIAGRAMA DE BODE:

    MIRAR DIAGRAMAS DE BODE

AMPLIFICADORES:

    MIRAR AMPLIFICADORES
    SE HA DADO EL MULTIPLICADOR, EL INTEGRADOR, EL DERIVADOR
    PERO NO SE HA DADO EL DE LAS EXPONENCIALES.

SOLO HA MANDADO 2 EJERCICIOS:

    DEL TEMA 1 BASTANTE LARGO QUE ERA DE MALLAS

    EL DEL TEMA 2 QUE ES DE LOS QUE HEMOS HECHO, EL QUE ERAN DOS DE PRIMER ORDEN JUNTOS
    (PASA DE BOBINA A CONDENSADOR O ASÍ.)


Ahora este código no da error, pero teniendo solo una neurona de salida, me da dos outputs:

# creamos nuestra primera red neuronal.

class my_neural_network():
    def __init__(self, topologia, act_fun):
        self.topologia = topologia
        self.act_fun = act_fun
        self.pesos = []
        self.bias = []

        for i in range(len(topologia)-1):
            wi = np.random.rand(topologia[i], topologia[i+1])
            bi = np.random.rand(topologia[i+1])
            self.pesos.append(wi)
            self.bias.append(bi)

    def feedforward(self, x):
        a = x
        for w, b in zip(self.pesos, self.bias):
            z = np.dot(a, w) + b
            a = self.act_fun[0](z)
        return a

    def train(self, data, y_true, lr=0.01, epochs=100):
        for epoch in range(epochs):
            for x, y in zip(data, y_true):
                activation = [x]
                a = x
                for w, b in zip(self.pesos, self.bias):
                    z = np.dot(a, w) + b
                    a = self.act_fun[0](z)
                    activation.append(a)

                # Backpropagation
                deltas = []
                for l in reversed(range(len(self.topologia)-1)):
                    a = activation[l+1]
                    z = a @ self.pesos[l].T + self.bias[l]

                    if l == len(self.topologia) - 2:
                        deltas.insert(0, self.act_fun[1](a) * mse_loss[1](a, y))
                    else:
                        deltas.insert(0, np.dot(deltas[0], _w.T) * self.act_fun[1](a))

                    _w = self.pesos[l]

                    self.bias[l] = self.bias[l] - lr * np.mean(deltas[0], axis=0, keepdims=True)
                    self.pesos[l] = self.pesos[l] - lr * np.dot(np.expand_dims(activation[l], axis=1), np.expand_dims(deltas[0], axis=0))

        return activation[-1]

topologia = [2, 2, 1]
act_fun = (sigm[0], sigm[1])

red = my_neural_network(topologia, act_fun)
x = np.array([[1, 1], [2, 2]])
y = red.feedforward(x)
print(red.pesos)
print(red.bias)
print(y)

red.train(x, np.array([[1], [1]]))