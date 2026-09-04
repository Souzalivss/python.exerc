from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa]''')
    opção = int(input('Digite uma opção:: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'o resultado de {n1} x {n2} é {multiplicar}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior vale {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Digite seu novo número: ')
        n1 = input('Primeiro valor: ')
        n2 = input('Segundo valor: ')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.')
    sleep(2)
print('Fim do programa!')


