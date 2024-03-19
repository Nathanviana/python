#Faça um programa que:  
# a) Obtenha o valor para a variável HT (horas trabalhadas no mês)  
# b) Obtenha o valor para a variável VH (valor hora trabalhada)  
# c) Obtenha o valor para a variável PD (percentual de desconto)  
# d) Calcule o salário bruto SB HT VH  
# e) Calcule o total de desconto TD ==( 100 )*SB  
# f) Calcule o salário líquido SL SB TD  
# g) Apresente os valores de Horas trabalhadas, Salário Bruto, Desconto, Salário Líquido. 

ht = 60
vh = 20
pd = 10

sb = ht*vh
td = sb*pd/ 100
sl = sb - td 

print("horas trabalhadas:", ht)
print("salário bruto:", sb)
print("desconto:", td)
print("salário liquido:", sl)