# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor


numCarrosVendidos = int(input("Digite o número de carros vendidos: "))
valorTotalVendas = float(input("Digite o valor total das vendas: R$ "))
salarioFixo = float(input("Digite o salário fixo do vendedor: R$ "))
valorPorCarro = float(input("Digite o valor que o vendedor recebe por carro vendido: R$ "))


comissaoFixa = numCarrosVendidos * valorPorCarro

comissaoTotalVendas = 0.05 * valorTotalVendas

salarioFinal = salarioFixo + comissaoFixa + comissaoTotalVendas

print("O salário final do vendedor é de R$ {:.2f}".format(salarioFinal))
