"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção
O Motor terá a responsabilidade de controlar a Velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado Velocidade
2) Método acelear, que deverá incrementar a velocidade em uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

    N
O       L
    S

        Exemplo:
        # Testando Motor
        >>> motor = Motor()
        >>> motor.velocidade
        0
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        >>> motor.acelerar()
        >>> motor.velocidade
        2
        >>> motor.acelerar()
        >>> motor.velocidade
        3
        >>> motor.frear()
        >>> motor.velocidade
        1
        >>> motor.frear()
        >>> motor.velocidade
        0
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Norte'
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_velocidade()
        0
        >>> carro.acelerar()
        >>> carro.calcular_velocidade()
        1
        >>> carro.frear()
        >>> carro.calcular_velocidade()
        0
        >>> carro.calcular_direcao()
        'Norte'
        >>> carro.girar_a_direita()
        >>> carro.calcular_direcao()
        'Leste'
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Norte'
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotacao = {0: 'Norte', 1: 'Leste', 2: 'Sul', 3: 'Oeste'}

    def __init__(self):
        self._valor = 0

    @property
    def valor(self):
        return self.rotacao[self._valor]

    def girar_a_direita(self):
        self._valor = (self._valor + 1) % 4

    def girar_a_esquerda(self):
        self._valor = (self._valor - 1) % 4


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.valor

    def calcular_velocidade(self):
        return self.motor.velocidade
