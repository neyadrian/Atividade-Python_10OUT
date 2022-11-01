import os

idade : int
somaIdade : int 
pesoSuperior90alturaInferior150 : int 
idade10e30altura190 : int 
peso : float
altura : float 
mediaIdade : float

pesoSuperior90alturaInferior150 = 0
somaIdade = 0
idade10e30altura190 = 0

for n in range(1,11):
    print(f"dados para {n}ª pessoa: ")
    idade = int(input("informe a iadde: "))
    peso = float(input("informe o peso: "))
    altura = float(input("informe a altura: "))

os.system ("cls")
somaIdade = somaIdade + idade
if(peso > 90) and (altura < 1.50):
    pesoSuperior90alturalturaInferior150 += 1
if(idade >= 10 and idade <= 30) and altura > 1.90:
    idade10e30Altura += 1

madiaIdade = somaIdade / 10

print(f"Média das idade das dez pessoas: {mediaIdade:.2f}")
print(f"Quantidade de pessoaos com o peso superior a 90 kg e altura inferior a 1,50 metros: {pesoSuperior90alturalturaInferior150}m.")
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m: {idade10e30Altura190/10*100:1f}%.")