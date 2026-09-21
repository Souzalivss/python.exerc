listagem = ('Lápis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 25,
            'mochila', 120)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}, ', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')