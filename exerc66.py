n = s = cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
    cont = cont + 1
print(f'a soma dos {cont} valores é {s}')