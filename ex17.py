from sys import argv
from os.path import exists

script, do_arquivo, para_arquivo = argv

print 'copiando do arquivo %r para %r '% (do_arquivo, para_arquivo)
no_arquivo = open(do_arquivo)
nos_dados = no_arquivo.read()

print 'O arquivo possui %d bytes' % len(nos_dados)

print 'A saida do arquivo existe? %r' % exists(para_arquivo)
print 'Pronto aperte ENTER para continuar, ou CTRL-C para cancelar'
raw_input()

fora_arquivo = open(para_arquivo,'w')
fora_arquivo.write(nos_dados)

fora_arquivo.close()
no_arquivo.close()
