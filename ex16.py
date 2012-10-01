from sys import argv

script, arquivo = argv

print 'Nos vamos apagar %r'% arquivo
print 'Se voce nao quer fazer isso use CTRL-C(^C)'
print 'Se quiser continuar use ENTER'

raw_input('?')

print 'Abrindo arquivo...'
alvo = open(arquivo,'w')

print 'Trancando o arquivo'
alvo.truncate()

print 'Agora vamos perguntar para voce 3 linhas'

linha1 = raw_input('linha 1: ')
linha2 = raw_input('linha 2: ')
linha3 = raw_input('linha 3: ')

print 'Vou escrever isso em um arquivo'

alvo.write(linha1)
alvo.write('\n')
alvo.write(linha2)
alvo.write('\n')
alvo.write(linha3)
alvo.write('\n')

print 'E agora nos fechamos'
alvo.close()
