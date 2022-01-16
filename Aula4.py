# durante o laço de repetição de 0 até o numero escolhido, vai printar os número primos, ou seja se é divisivel apenas por 1 e por ele mesmo 
a = int(input('Entre com o número: '))

for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1 # esse formato é a simplificação de div = div + 1
    if div == 2:
        print(num)

print('fim do programa do primo\n inicia programa com while')

# Estrutura While...

a = 0

while a <= 7:
    print(a)
    a += 1
