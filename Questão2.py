#Declaração de Variáveis
precoIngressos : float
despesas : float
lucro : float
qntIgressos : int 

precoIngressos = 5.00
qntIgressos = 120
despesas = 200.00

#Processamento e Saída 
while precoIngressos >= 1.00:
    lucro =  qntIgressos * precoIngressos - despesas
    print(f'|Preço: \t\t |R$ {precoIngressos:.2f}')
    print(f'|Lucro: \t\t |R$ {lucro:.2f}')
    print(f'|Ingressos Vendidos: \t |{qntIgressos}')
    print('------------------------------------')
    precoIngressos = precoIngressos - 0.50
    qntIgressos = qntIgressos + 26