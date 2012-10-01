primeiro=raw_input("idade: ")
segundo=raw_input("Nome: ")
terceiro=raw_input("altura: ")

from sys import argv

script, primeiro, segundo, terceiro = argv

print "O script chamado: ",script
print "Sua primeira variavel eh: ",primeiro
print "Sua segunda variavel eh: ",segundo
print "sua terceira variavel eh: ", terceiro
