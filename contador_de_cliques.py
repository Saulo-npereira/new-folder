import os
contador = 0
while True:
    os.system('cls')
    clique = input('aperte ENTER pra contar ou q pra sair: ')
    if 'q' in clique:
        print(contador, 'cliques')
        break
    contador += 1