#progressão aritmetica
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo = termo + razao
    cont = cont + 1