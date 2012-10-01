def print_dois(*args):
    arg1, arg2 = args
    print 'arg1: %r, arg2: %r' % (arg1,arg2)

def print_dois_novo(arg1,arg2):
    print 'arg1: %r, arg2: %r' % (arg1,arg2)
    
def print_um(arg1):
    print 'arg1: %r'%(arg1)
    
def print_nenhum():
    print 'Nada'
    
print_dois('flavio','augusto')
print_dois_novo('flavio','augusto')
print_um('Primeiro')
print_nenhum()
