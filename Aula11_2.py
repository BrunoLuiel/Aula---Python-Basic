class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
        
x = input(int('Entre com uma nota de 0 a 10: '))

while True:
    try:
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')# Raise força que ocorra a exceção
        elif x < 0:
            raise InputError('Nota não pode ser menor que zero')
        break # necessário para que não haja loop infinito e só será acionado quando a linha anterior for não der erro, uma vez que as linhas de baixo da linha do erro não são executadas
    except ValueError:
        InputError('Valor invalido. Deve-se informar apenas números')

