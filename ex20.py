from sys import argv

script, arquivo = argv

def print_tudo(a):
    print a.read()
    
def rebobinar(a):
    a.seek(0)
    
def print_uma_linha(cont_linha,a):
    print cont_linha, a.readline()
    
arquivo_atual = open(arquivo)

print "Primeiro vamos printar algumas coisas do arquivo:\n"

print_tudo(arquivo_atual)

print "Agora vamos rebobinar uma fita"

rebobinar(arquivo_atual)

print "Vamos printar 3 linhas"

linha = 1
print_uma_linha(linha, arquivo_atual)

linha = linha + 1
print_uma_linha(linha, arquivo_atual)

linha = linha + 1
print_uma_linha(linha, arquivo_atual)
