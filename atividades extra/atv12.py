# Escreva um programa para solucionar e exibir o resultado da seguinte questão: um pendrive pode armazenar 8GB de dados, sabendo que ele já está armazenando 3584MB, quanto esse pendrive ainda pode armazenar em GB?

penDrive = 8
usado = 3584

conversor = 3580 / 1000

armazenandoRestante = penDrive - conversor

print(armazenandoRestante)