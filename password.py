import random

while (True):
    caracterPassword = input('Insira a quantidade de caracteres: ')
    if(caracterPassword == 'sair'):
        print('Programa cancelado')
        break
    else:
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*()_abcdefghijklmnopqrstuvwxyz'
        create = ''.join(random.sample(caracteres,int(caracterPassword)))
        print('Sua senha é: ', create)