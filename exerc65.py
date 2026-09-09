resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant = quant + 1

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {}!'.format(quant, media))
