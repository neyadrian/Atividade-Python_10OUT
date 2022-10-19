import os

#Declação de Variáveis
c : str 
compra : float ; cv : float ; cp : float ; ct : float
compra = 0
cv = 0
cp = 0 

#Processamento de Dados
for n in range(1, 16):
    print(f"Dados de {n}ª venda")
    c = input("Digite o código da compra (V - à vista ou P - à prazo): ").upper()
    while (c != "V" or c != "P"):
        c = input("Digite o código da compra (V - à vista ou P - à prazo): ").upper()
    if c == "V":
        compra = float(input("Digite o valor da compra: R$ "))
        cv = cv + compra
    elif c == "P":
        compra = float(input("Digite o valor da compra: R$ "))
        cp = cp + compra
    os.system("cls")

#Saída de Dados  
print(f"O valor total da compra à vista: R$ {cv:.2f}")
print(f"O valor total da compra à prazo: R$ {cp:.2f}")
print(f"O valor total das compras: R$ {cp + cv:.2f}")
print(f"O valor da primeira prestação das compras a prazo juntas: R$ {cp/3:.2f}")

