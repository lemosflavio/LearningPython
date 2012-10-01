from sys import argv

scritp, arquivo = argv

print 'Vamos ler um arquvio'
print 'Abrindo arquivo'
alvo = open(arquivo, 'r')

print 'Truncando o arquivo'

print 'Agora vamos ler o arquivo'

print alvo.read()

print 'Fechando o arquivo'
alvo.close()

