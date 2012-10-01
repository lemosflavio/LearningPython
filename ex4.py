carros = 5000
pessoasDentro = 4.0
motoristas = 30
passageiros = 90
carrosSemMotoristas = carros-motoristas
carrosComMotoristas = motoristas
capacidade = carrosComMotoristas*pessoasDentro
maximoDeCarrosPorPassageiro = passageiros/carrosComMotoristas

print "Carros disponiveis: ",carros
print "Motoristas disponiveis: ",motoristas
print "Carros sem motoristas: ",carrosSemMotoristas
print "Capacidade de pessoas que podem ser transportadas hoje: ",capacidade
print "Quantidade de passageiros",passageiros
print "Maximo de passageiros por carro", maximoDeCarrosPorPassageiro
