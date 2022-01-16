#Função é tudo que retorna valor
#Metodo é o que não retorna valor

from typing import Mapping


class Calculadora: #Por definição nome da "class" inicia sempre com letra maiuscula, enquanto métodos e funções, letras minusculas
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):   # "def" de definição, lembrando de identar a class
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

if __name__ == '__main__':
    print(__name__)
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.divisao())
    print(calculadora.multiplicacao())
    print(calculadora.subtracao())
