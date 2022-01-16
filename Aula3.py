a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('o maior número é {}'.format(a))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}'.format(c))
print('Final do programa')

# Para saber se é par:

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0: # Quando quiser contemplar um resultado que tenha como resultado o igual, devo usar "==" pois somente um "=" é receber uma informação
    print('foi digitado um número par') # a função "not" é o sistema inverso, ou seja, nesse caso, se resto_b for maior que zero então ele vai executar
else:
    print('nenhum número par foi digitado')

# Validação de notas de um aluno

a = int(input('Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media do aluno é: {}'.format(media))
else:
    print('você digitou a nota errada')