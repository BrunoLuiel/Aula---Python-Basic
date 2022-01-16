lista = [1, 7, 5, 4] #List'a sempre estará em colchetes
lista_animal = ['cachorro', 'gato', 'elefante'] #Lembrando que python começa com 0 então 0 = cachorro, 1 = gado...

for x in lista_animal:
    print(x)

print(sum(lista))
print(max(lista)) #Saber o maior valor
print(min(lista_animal)) #Calcula o maior em textos sendo pelo primeiro caractere. A ordem de grandeça é "A" o menor e "Z" o maior

if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não há lobo na lista, por isso será adicionado uma nova')
    lista_animal.append('lobo')    #"append" insere um novo registro na lista - o "append" já é um metodo da lista, por isso não há necessidade de fazer lista_animal = lista_animal.apend('lobo') 
    print('agora existe um lobo na lista')
    lista_animal.append('arara')

lista_animal.pop(2)# O "pop" retira o último item da lista, mas pode ser alterado a sequencia preenchendo o entre parenteses o numero do item
print(lista_animal)

lista_animal.remove('gato')# Para retirar o elemento pelo nome usa-se o "remove"

lista.sort()
lista_animal.sort() #organiza do menor para maior, incluindo letras

print(lista)
print(lista_animal)

lista.reverse #Faz o contrario do sort
lista_animal.reverse

print(lista)
print(lista_animal)

lista(0) = 'macaco'