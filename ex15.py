from sys import argv

script, arquivo = argv

txt =  open(arquivo)

print "Esse eh o seu arquivo %r"%arquivo
print txt.read()

print "Tipo de arquivo"
arquivo_novo = raw_input("> ")

txt_novo=open(arquivo_novo)

print txt_novo.read()
