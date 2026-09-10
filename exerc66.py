n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
print(f'a soma é {s}')