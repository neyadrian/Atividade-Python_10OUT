import math

#Declaração de Variáveis
num : int
somaNumPares : int 
somaNumPrimos : int 
contNumPrimo : int 

contNumPrimo = 0
somaNumPares = 0 
somaNumPares = 0

#Entrada de Dados
for n in range(1, 4):
    num = int(input("Informe um número: "))

#Processamento de Dados
    if num % 2 == 0:
        somaNumPares += num

    for m in range(1, int(math.sqrt(num)+1)):
        if num % m == 0:
            contNumPrimo += 1

    if contNumPrimo == 0:
        somaNumPrimos += num

#Saída de Dados
print(f"A resultado da soma dos números pares é de: {somaNumPares}")
print(f"A resultado da soma dos números primos é de: {somaNumPrimos}")