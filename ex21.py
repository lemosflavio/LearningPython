def soma(a,b):
    print 'Somando %d + %d'%(a,b)
    return a+b

def sub(a,b):
    print 'Subtraindo %d + %d'%(a,b)
    return a-b

def mult(a,b):
    print 'Multiplicando %d * %d'%(a,b)
    return a*b
    
def div(a,b):
    print 'Didindo %d/%d'%(a,b)
    return a/b

print 'Vamos fazer algumas contas com funcoes'

idade = soma(30,5)
altura = sub(78,4)
peso = mult(90,2)
qi = div(100,2)

print 'Idade: %d, Altura: %d, Peso: %d, QI: %d' % (idade,altura,peso,qi)

what = soma(idade,sub(altura,mult(peso,div(qi,2))))

print 'E isso: ',what,' Voce poderia fazer isso na mao?'
