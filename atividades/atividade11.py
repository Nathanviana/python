# Elabore um programa que calcule e mostre a taxa de consumo em km/l que um carro tem em um deslocamento. Devem ser criadas variáveis para a distância percorrida (em kilômetros), a quantidade de litros consumidos e o valor da taxa de consumo (em km/l). O cálculo é feito pela fórmula:  taxaDeConsumo = distancia / litros

distancia = float(input('Digite a ditância pecorrida em quilômetros:'))
litros = float(input('Digite a quantidade de litros consumidos:'))

taxaDeConsumo = distancia / litros

print("A taxa de consumo do carro é de {:.2f} km/l." .format(taxaDeConsumo))