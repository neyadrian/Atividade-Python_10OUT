import os

#Declaração de Variáveis
idade : int ; idade50 : int ; alturaEntre10e20 : int ; peso40 : int ; qtdCadastros : int 
altura : float ; peso : float ; somaAltura : float 

idade50 = 0
altura = 0
somaAltura = 0
alturaEntre10e20 = 0
peso40 = 0 
qtdCadastros = 0

#Entrada de Dados
qtdCadastros = int(input("Informe a quantidade de cadastros a serem realizados: "))
os.system("cls")

#Processamento e Saída de Dados
for n in range(1, qtdCadastros + 1):
    print(f"Informe os dados para {qtdCadastros} pessoas!")
    print(f"Infome os dados para {n}ª pessoas!")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    os.system("cls")

    if idade > 50:
        idade50 += 1
    if idade >= 10 and idade <= 20:
        somaAltura += altura 
        alturaEntre10e20 += 1
    if peso < 40:
        peso40 += 1

print(f"Existem {idade50} pessoas com idade superior a 50 anos.")
if alturaEntre10e20 <=0:
    print("Não foram informados pessoas com média de altura entre 10 e 20.")
else:
    print(f"A média das alturas entre 10 e 20 é de {somaAltura/alturaEntre10e20:.2f}.")
print(f"% de pessoas com peso inferior a 40 kg: {peso40/qtdCadastros*100}%")