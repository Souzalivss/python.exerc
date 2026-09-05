#pa com termos indefinidos
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais vc quer mostrar? '))
print('FIM')