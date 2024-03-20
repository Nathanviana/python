# Escreva um programa que receba o valor do salário de um funcionário e o valor do salário-mínimo. Calcule e mostre quantos salários-mínimos ganha esse funcionário.

salarioDoFuncionario = float(input("Digite o salário do funcionário:"))
salarioMin = 1412

salarioMinGanho = salarioDoFuncionario / salarioMin

print('O funcionário ganha {:.2f} salários mínimos.' .format(salarioMinGanho))