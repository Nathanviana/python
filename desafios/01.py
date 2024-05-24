# X = []
# for i in range(10):
#     numero = int(input())
#     if numero <= 0:
#         numero = 1
#         X.insert(i,numero)
#     else:
#         X.insert(i,numero)

# for i in range(10):
#     print('X[{}] = {}'.format(i,X[i]))

X = []

for i in range(10):
    if i == 0:
        valor = int(input())
        dobro = valor
        X.insert(i,valor)
    else:
        dobro = dobro * 2
        X.insert(i,dobro)
    
for i in range(10):
    print("N[{}] = {}".format(i,X[i]))