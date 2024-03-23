# # Sabe-se que o quilowatt de energia custa 2% do salário mínimo. Escreva um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência. Calcule e imprima: 
# • o valor, em reais, de cada quilowatt; 
# • o valor, em reais, a ser pago por essa residência; 
# • o novo valor à ser pago por essa residência, se for dado um desconto de 15%. 

salarioMinimo = float(input("Digite o valor do salário mínimo: R$ "))
quilowattsConsumidos = float(input("Digite a quantidade de quilowatts    consumidos: "))

valorPorQuilowatt = salarioMinimo * 0.02

valorTotal = valorPorQuilowatt * quilowattsConsumidos

desconto = valorTotal * 0.15

valorComDesconto = valorTotal - desconto

print("Valor por quilowatt: R$", valorPorQuilowatt)
print("Valor a ser pago pela residência: R$", valorTotal)
print("Novo valor a ser pago com desconto de 15%: R$", valorComDesconto)