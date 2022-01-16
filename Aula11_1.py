lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[3]
    x = a

except ZeroDivisionError:
    print('Não é possível realizar um divisão por zero')
except IndexError:
    print('Erro ao acessar um dindice inválido da lista')
except Exception as ex: # Essa é a mae dos erros ou seja se colocar em primeiro da lista dos except vai dar erro sem olhar os demais, recomendado ver a lista de erros no site do Python
    print('erro desconhecido; Erro: {}'.format(ex))
else:
    print('Executa quando não encontrar uma exceção')
finally:
    print('quando da erro as linhas para baixo não são executadas, exceto usando o "finally"')