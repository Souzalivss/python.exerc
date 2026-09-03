from random import randint
computador = randint(0, 10)
print('Sou seu computadoor, acabei de pensar em um número...')
print('Advinhe? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais alto... tente mais uma vez')
        elif jogador > computador:
            print('Mais baixo, tente mais uma vez')
print('Acertou com {} palpites'.format(palpites))

