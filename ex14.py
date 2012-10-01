from sys import argv

script, usuario = argv
prompt = '> '

print "ola %s, Esse eh o script %s"%(usuario, script)
print "Vou fazer algumas perguntas"
print "Voce gosta de mim %s ?"% usuario
opniao = raw_input(prompt)
 
print "Onde voce mora?"
local = raw_input(prompt)
 
print "Qual o seu sistema operacional?"
computador = raw_input(prompt)
 
print """
vc disse que %s gosta de mim, que mora
em %s e seu sistema operacional eh %s
"""%(opniao, local, computador)
