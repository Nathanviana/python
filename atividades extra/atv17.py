# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual (ambos com 4 dígitos). Calcule e imprima: • essa idade convertida em semanas.

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento

idadeEmSemanas = idade * 52

print("A idade convertida em semanas é:", idadeEmSemanas)


