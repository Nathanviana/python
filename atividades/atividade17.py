# Um trem se locomove há 150 km/h, e funciona por 20 horas por dia. A cada 2.000 km ele deve parar 6 horas para manutenção. Cada manutenção custa R$ 2.000,00 e a cada 3 dias é cobrada uma taxa de R$ 5.000,00 de uso da ferrovia. Escreva em um algoritmo que receba o número de dias e escreva na tela um relatório, com o número de kilômetros percorridos e manutenções realizadas, assim como o custo total. 

vDoTrem = 150
funcionaPorDia = 20
distanciaManutencao = 2000
tempoManutencao = 6
custoManutencao = 2000
txUsoFerroviaria = 5000

dias = int(input('Digite um número de dias:'))
    
horaTotal = dias * funcionaPorDia

kmPecorridos = horaTotal * vDoTrem

numManutencao = kmPecorridos / distanciaManutencao

custoTotalManutencao = numManutencao * custoManutencao

numTaxaFerrovia = dias // 3

custoTotalTaxaFerrovia = numTaxaFerrovia * txUsoFerroviaria

custoTotal = custoTotalManutencao + custoTotalTaxaFerrovia

print("Relatório:")
print(f"km pecorridos: {kmPecorridos} km" )
print(f"Manutenções realizadas: {numManutencao}")
print(f"Custo total: R$ {custoTotal}")
