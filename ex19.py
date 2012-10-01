def queijo_e_biscoito(cont_queijo,caixa_de_biscoito):
    print 'Voce tem %d queijos!' % cont_queijo
    print 'Voce tem %d caixas de biscoitos!' % caixa_de_biscoito
    print 'Estamos prontos para festa'

print 'Nos podemos numeros diretos para a funcao'
queijo_e_biscoito(20,30)

print 'Ou podemos usar variaveis fora do script'
qtd_de_queijo = 10
qtd_de_biscoito = 50

queijo_e_biscoito(qtd_de_queijo,qtd_de_biscoito)

print 'nos podemos usar matematica tambem'
queijo_e_biscoito(10+20,5+6)

print 'E podemos combinar os 2, variaveis e matematica'
queijo_e_biscoito(qtd_de_queijo+100,qtd_de_biscoito+1000)
