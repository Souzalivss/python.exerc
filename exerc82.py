num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'a lista completa é {num}')
print(f'a lista de ímpares é {ímpares}')
print(f'a lista completa de pares é {pares}')