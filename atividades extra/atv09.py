# Crie um algoritmo/programa que receba três nomes quaisquer e os mostre na tela na ordem inversa da que foi fornecida. Exemplo de entrada: Ana, Bruno e Caio Exemplo de saída: Caio, Bruno e Ana

nome1 = 'Ana'
nome2 = 'Bruno'
nome3 = 'Caio'

print(nome1, nome2, nome3)

nome4 = nome1
nome1 = nome3
nome3 = nome4

print(nome1, nome2, nome3)