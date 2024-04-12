# Uma determinada pessoa que trabalha com a construção de piscinas precisa de um programa que calcule o valor das construções solicitadas pelos clientes, sabendo-se que os clientes sempre fornecem o comprimento, a largura e a profundidade da piscina a ser construída. Leve em consideração que o valor da construção é cobrado por m3 de água e o preço é de R$ 75,00 por m3.

comprimento = float(input("Digite o comprimento da piscina (em metros): "))
largura = float(input("Digite a largura da piscina (em metros): "))
profundidade = float(input("Digite a profundidade da piscina (em metros): "))

preçoMetroCubico = 75.00

volume = comprimento * largura * profundidade

custoTotal = volume * preçoMetroCubico

print(custoTotal)

