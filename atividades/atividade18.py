# Escreva um algoritmo que receba o valor de um produto, e para cada R$ 100,00 dê um desconto de 0,05%. 

valorProduto = float(input("Digite o valor do produto: "))


quantidaDeDesconto = valorProduto // 100
desconto = quantidaDeDesconto * 0.05


valorFinal = valorProduto - desconto


print("Valor final com desconto: R$", valorFinal)
