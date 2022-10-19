#Declaração de Variáveis
faixa1 : int
faixa2 : int
faixa3 : int
faixa4 : int 
faixa5 : int

#Processamento e Saída de Dados
for n in range(1,9):
    idade = int(input('Digite a idade da pessoa: '))

if idade <= 15:
    faixa1 = faixa + 1
elif idade > 15 and idade <= 30:
    faixa2 += 1
elif idade > 30 and idade <= 45:
    faixa3 += 1
elif idade > 45 and idade <= 60:
    faixa4 += 1
else:
    faixa5 += 1

print(f"Pessoas na faixa etária até 15 anos: {faixa1}")
print(f"Pessoas na faixa etária de 16 a 30 anos: {faixa2}")
print(f"Pessoas na faixa etária de 31 a 45 anos: {faixa3}")
print(f"Pessoas na faixa etária de 46 a 60 anos: {faixa4}")
print(f"Pessoas na faixa acima de 60 anos: {faixa5}")

porcentagem1 = (faixa1/8)*100
porcentagem2 = (faixa5/8)*100

print(f"A porcentagem de pessoas na faixa etária até 15 anos é de {faixa1/8*100}%")
print(f"A porcentagem de pessoas da última faixa em relação ao total {faixa5/8*100}%")




