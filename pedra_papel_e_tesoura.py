import os
import time
import random 
def lin():
    print('-' * 30)

def limpa():
    os.system('cls')

lin()
print('PEDRA, PAPEL E TESOURA')
lin()
nome1=input('digite o nome do p1: ')
nome2='maquina'
limpa()
print(f'VEZ DE ')
j1=int(input('[PEDRA] = 1\n[PAPEL] = 2\n[TESOURA] = 3\nESCOLHA:'))
time.sleep(1)
limpa()
j2=random.randint(1,3)
time.sleep(1)
limpa()
print('E O VENCEDOR É:')
time.sleep(1)
if j1 == 1 and j2 ==1:
    print('EMPATE')
if j1 == 2 and j2 ==2:
    print('EMPATE')
if j1 == 3 and j2 ==3:
    print('EMPATE')
if j1 == 1 and j2 == 2:
    print(f'{nome2} ganhou')
if j1 == 1 and j2 == 3:
    print(f'{nome1} ganhou')
if j1 == 2 and j2 == 1:
    print(f'{nome1} ganhou')
if j1 == 2 and j2 == 3:
    print(f'{nome2} ganhou')
if j1 == 3 and j2 == 1:
    print(f'{nome2} ganhou')
if j1 == 3 and j2 == 2:
    print(f'{nome1} ganhou')
