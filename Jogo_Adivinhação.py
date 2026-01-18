import random
import time
import os
def limpa():
    os.system('cls')


def lin():
    print('—' * 40)

numeros = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
os.system('cls')
lin()
print('JOGO ADIVINHAÇÃO DE NUMERO ENTRE 1 E 100')
lin()
print('CARREGANDO')
for i in numeros:
    print(i,'%', end = '\r')
    time.sleep(0.3)
time.sleep(0.3)
limpa()
n=random.randint(1, 100)
n1=int(input('digite um número entre 1 e 100: '))
tent = 7
if n1 == n and tent == 0:
    print('PARABENS VOCÊ ACERTOU DE PRIMEIRA')
else:
    while n1!=n and tent >0:
        if n1!=n:
            if n1>n:
                print(f'o numero certo é menor, voce tem {tent} tentativas')
                n1=int(input('digite um número entre 1 e 100: '))
            elif n1<n:
                print(f'o numero certo é maior, voce tem {tent} tentativas')
                n1=int(input('digite um número entre 1 e 100: '))
        tent -= 1
if n1==n and tent !=7:
    print('VOCE ACERTOU O NUMERO')


    