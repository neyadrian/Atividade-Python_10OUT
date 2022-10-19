import os
#Declaração de Variáveis
a : int
b : int
c : int 
d : int
n : int
m1 : int 
m2 : int 
m3 : int 
m4 : int 

#Entrada de Dados
m1 = 0
m2 = 0 
m3 = 0
m4 = 0

#Processamento de Dados
for n in range(1,6):
    os.system("cls")
    print(f'Digite os valores para o grupo {n}: ')
    a = int(input('Digite o valor para A: '))
    b = int(input('Digite o valor para B: '))
    c = int(input('Digite o valor para C: '))
    d = int(input('Digite o valor para D: '))

if a>=b and a>=c and a>=d:
        m1 = a
        if b>=c and b>=d:
            m2 = b
            if c>=d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        elif c>=b and c>=d:
            m2 = c
            if b>=d:
                m3 = b
                m4 = d
            else:
                m3 = d
                m4 = b
        else:
            m2 = d
            if c>=b:
                m3 = c
                m4 = b
            else:
                m3 = b
                m4 = c
elif b>=a and b>=c and b>=d:
        m1 = b
        if a>=c and a>=d:
            m2 = a
            if c>=d:
                m3 = c
                m4 = d
            else:
                m3 = d
                m4 = c
        elif c>=a and c>=d:
            m2 = c
            if a>=d:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
        else:
            m2 = d
            if a>=c:
                m3 = a
                m4 = c
            else:
                m3 = c
                m4 = a
elif c>=a and c>=b and c>=d:
        m1 = c
        if a>b and a>d:
            m2 = a
            if b>d:
                m3 = b
                m4 = d
            else:
                m3 = d
                m4 = b
        elif b>a and b>d:
            m2 = b
            if a>d:
                m3 = a
                m4 = d
            else:
                m3 = d
                m4 = a
        else:
            m2 = d
            if a>b:
                m3 = a
                m4 = b
            else:
                m3 = b
                m4 = a
else:
        m1 = d
        if a>b and a>c:
            m2 = a
            if b>c:
                m3 = b
                m4 = c
            else:
                m3 = c
                m4 = b
        elif b>a and b>c:
            m2 = b
            if a>c:
                m3 = a
                m4 = c
            else:
                m3 = c
                m4 = a
        else:
            m2 = c
            if a>b:
                m3 = a
                m4 = b
            else:
                m3 = b
                m4 = a

#Saída de Dados
print(f"A ordem recebida foi: {a, b, c, d}")
print(f"A ordem crescente é: {m4, m3, m2, m1}")
print(f"A ordem decrescente é: {m1, m2, m3, m4}")
            
