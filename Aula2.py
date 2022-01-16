a = 5
b = 10
soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
resto = a % b
print(soma)
print(subtracao)
print(divisao)
print(multiplicacao)
print(resto)
print(type(soma))
print('Soma é igual a ' + str(soma)) #Veja que para concatenar uma string com um integer foi necessario declarar o inteiro como uma string, mas a melhor forma de faze-lo é a abaixo:
print('Soma é igual a {}. Subtração é igual a {}'.format(soma,subtracao)) # ou pode ser também:
print('Soma é igual a {sum}. Subtração é igual a {sub}'.format(sum = soma, sub = subtracao)) # Posso colocar a descrição que quiser entre os colchetes, desde que referencie no format
print('Soma é igual a {sum}\nSubtração é igual a {sub}' #Veja que /n é como se fosse o enter e nesse exemplo a obrigação de uma ordem não é tão necessária
'\n divisao é igual a {div}'
'\n resto é igual a {res}'.format(sum = soma, sub = subtracao, res = resto, div = divisao))

c = int(input('Entre com o primeiro valor'))# para funcionar os calculos no input deve inserir o "int" antes do inputbox, se não considerará os numeros como string
d = int(input('Entre com o segundo valor'))

summ = c + d
subb = c - d

print(type(sum))
print('A soma no inputbox é de ' + str(summ))
print('A subtrção no inputbox2 é de {}'.format(subb))