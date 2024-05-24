from collections import Counter

texto = "Um texto é uma manifestação da linguagem. Pode ser definido como tudo aquilo que é dito por um emissor e interpretado por um receptor. Dessa forma, tudo que é interpretável é um texto. Outra forma de conceituação é pensar que tudo aquilo que produz um sentido completo, que seja uma mensagem compreensível, é um texto."

contar = texto.replace(".","").replace(',','').replace('?','').replace(':','').split()
# palavras = contar.split()

print("\nO total de palavras no texto é:")
# print(palavras)
print(len(contar))

#frequencia de cada palavra
frequencia = Counter(contar)

print("\nFrequencia de cada palavra")
print(frequencia)

palavra_mais_frequente = frequencia.most_common(1)[0]
print("\nA palavra mais frequente é:")
print(f"{palavra_mais_frequente[0]}: {palavra_mais_frequente[1]} vezes")

# media
quantidade_de_letras = [len(contar) for contar in contar]
soma_de_letras = sum(quantidade_de_letras)
numero_de_palavras = len(texto.split())
media_letras_por_palavra = soma_de_letras / numero_de_palavras
bunito = f"{media_letras_por_palavra:.2f}"

print(f"\nComprimento medio das palavras\n{bunito}")
# print(bunito)