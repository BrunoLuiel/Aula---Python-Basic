
class Arquivotxt:

    def escrever_arquivo(texto):
        #diretorio = 'C:/Users/ADM/Documents/teste.txt'     ##Essa seria uma outra opção para salvar em uma pasta diferente 'C:/Users/ADM/Documents/teste.txt'
        #arquivo.open(diretorio, 'w') 
        arquivo = open('teste.txt', 'w') # 'teste.txt', 'w' escreve. 'teste.txt', 'a' atualiza arquivo 
        arquivo.write(texto)
        arquivo.close()

    def atualizar_arquivo(nome_arquivo):
        arquivo = open('notas.txt', 'a') # 'teste.txt', 'w' escreve. 'teste.txt', 'a' atualiza arquivo
        arquivo.write(nome_arquivo)
        arquivo.close()

    def ler_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        texto = arquivo.read()
        print(texto)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    Arquivotxt.atualizar_arquivo('\n maisum')
    #ler_arquivo('teste.txt')
