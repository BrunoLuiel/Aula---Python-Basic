#Função é tudo que retorna valor
#Metodo é o que não retorna valor

class Calculadora: #Por definição nome da "class" inicia sempre com letra maiuscula, enquanto métodos e funções, letras minusculas
    def __init__(self):  ######## o def não pode ficar vazio por isso nesse caso se usa o "pass". Essa é sua única finalidade. Se quiser pode excluir o "init" e funcionará normalmente
        pass

    def soma(self, valor_a, valor_b):   # "def" de definição, lembrando de identar a class
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

calculadora = Calculadora() # No instanciamento não vai nenhum valor
if __name__ == '__main__':
    print(calculadora.divisao(10,2)) # agora é aqui que vai valor
    print(calculadora.multiplicacao(10,2))
    print(calculadora.subtracao(10,2))