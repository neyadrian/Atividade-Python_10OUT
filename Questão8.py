import os

#Declaração de Variáveis
idade : int
somaIdd : int
mediaIdd : float
idade50 : int
peso60 : float
altura : float
somaAlt : float
altAbaixo150 : int
peso : float
corOlhos : str
spmaOlhoAzul : int
somaCRuivoOAzul : int
somaCabRuivo : int
corCabelos : str
cadastros : int

idade = 0
somaIdd = 0
mediaIdd = 0
idade50 = 0
peso60 = 0
altura = 0
somaAlt = 0
altAbaixo150 = 0
peso = 0
spmaOlhoAzul = 0
somaCRuivoOAzul = 0
somaCabRuivo = 0

#Entrada de Dados
os.system("cls")
cadastros = int(input("Digite a quantidades de cadarstros que seram feitos: "))

#Processamento e Saída de Dados
for n in range(1, cadastros + 1):
    print(f"Informe os dados da {n}ª pessoa!")
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe a altura: "))
    corOlhos = input("Informe a cor dos olhos (A — azul; P — preto; V — verde; e C — castanho): ").upper()
    corCabelos = input("Informe a cor dos cabelos (P — preto; C — castanho; L — louro; e R — ruivo): ").upper()
    os.system("cls")

    if idade > 50:
        idade50 += 1
    if peso < 60:
        peso60 += 1
    if altura < 1.50:
        somaIdd += idade
        mediaIdd += 1
    if corOlhos == 'A':
        somaOlhoAzul += 1
    if corDeOlho != 'A' and corCabelos == "R":
        somaCRuivoOAzul += 1

    

print(f'A quantidade de pessoas acima de 50 são {idade50}. Pessoas com peso infeior a 60kg são de {peso60}.')

if idade50 <= 0:
    print(f'Não foram cadastradas pessoas acima de 50 anos. Pessoas com peso infeior a 60kg são de {peso60}.')
elif peso60 <= 0:
    print(f'Quantidade de pessoas com idade acima de 50 são de {idade50}. Não foram cadastradas pessoas com peso abaixo de 60kg.')
else:
     print(f'Não foram cadastradas pessoas acima de 50 anos. Não foram cadastradas pessoas com o peso abaixo de 60kg.')

if somaIdade == 0:
    print(f'Não foram cadastradas pessoas com menos de 1.50 de altura.')
else:
    print(f'A média das idades de pessoas com altura inferior a 1.50 é de {somaIdd/mediaIdd * 100:.2f}%.')


if somaOlhoAzul <=0:
    print(f'Não foram cadastradas pessoas com os olhos azuis.')
else:
    print(f'A % de pessoas cadastradas com os olhos azuis é de {somaOlhoAzul/n * 100:.2f}%.')

if somaCRuivoOAzul <= 0:
    print("Não foram cadastradas pessoas com os cabelo ruivo sem os olhos azuis.")
else:
    print(f'Foram cadastradas {somaCRuivoOAzul} pessoas com os cabeloos ruivos que não possuem os olhos azuis.')
    