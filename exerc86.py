matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): #linha e c coluna
    for c in range(0, 3):
        matriz[l][c] =  int(input(f'digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')  #5 espaços centralizados
    print() #quebra de linha apos terminar coluna
print('-=' * 30)
