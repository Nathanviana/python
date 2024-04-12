#  O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o cust

custoFabrica = float(input("Digite o custo de fábrica do carro: "))


porcentagemDistribuidor = 28 / 100
porcentagemImpostos = 45 / 100

custoConsumidor = custoFabrica + (custoFabrica * porcentagemDistribuidor) + (custoFabrica * porcentagemImpostos)


print("O custo total do carro ao consumidor é de R$ {}".format(custoConsumidor))
