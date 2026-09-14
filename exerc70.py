total = totmil = 0
while True:
    produto = str(input('nome do produto: '))
    preço = float(input('Preço = R$'))
    total += preço
    if preço > 1000:
        totmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
           break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'o total da compra foi R${total:.2f}')
print(f'A quantidade de produtos acima de R$1000,0 é {totmil}')