from Aula9_1 import Arquivotxt

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') # Esse split faz com que o caractere que eu informar seja o separador de lista, ou seja agora cada linha do TXT será uma lista
    print(aluno_nota)
    for x in aluno_nota:
        lista_alunos = x.split(',') #Agora fiz uma nova listagem através da ','
        aluno = lista_alunos[0] # Agora o aluno da Lista "0" está definido.
        lista_alunos.pop(0)
        media = lambda notas: sum([int(i) for i in notas] / 4)
        print(media(lista_alunos))




 



