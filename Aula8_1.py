from Aula7_3 import Televisao
from Aula7_1 import Calculadora
from Aula8_2 import contador_letras

if __name__=='__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por lista: {}'. format(total_letras))