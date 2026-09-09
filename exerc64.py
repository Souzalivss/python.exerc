num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma = soma +num
    num  = int(input('Digite um numero [999 para parar]: '))
    cont = cont + 1
print('voce digitou {} numeros e asoma entre eles foi {}'.format(cont, soma))
