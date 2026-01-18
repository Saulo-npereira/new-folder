estudos = []
import time
import os
saida = ['saindo.', 'saindo..', 'saindo...']
p=0
def tempo(a):
    time.sleep(a)
def limpa():
    os.system('cls')
def mostrar_menu():
    print('\n1 - Adicionar estudo')
    print('\n2 - Listar estudos')
    print('\n3 - Remover estudo')
    print('\n0 - Sair')
def adicionar_estudo():

    materia = str(input('Materia: '))
    tempo = input('Tempo: ')
    estudo = {'materia': materia,
              'tempo': tempo}
    estudos.append(estudo)
def listar_estudos():
    if len(estudos) == 0:
        print('Nenhum estudo registrado')
        return
    for estudo in estudos:
        print(estudo['materia'], '-', estudo['tempo'])
def remover_estudo():
    for i, estudo in enumerate(estudos):
        print(i, '-', estudo['materia'])
    indice = int(input('Digite o número para remover: '))
    if estudos == []:
        print('Você já removeu todos')
    elif indice>i or indice<i:
        print('indice não registrado')
    else:
        estudos.pop(indice)



while True:
    mostrar_menu()
    opcao = input('escolha uma opção: ')

    if opcao == '1':
        adicionar_estudo()
        tempo(0.5)
        limpa()
    elif opcao == '2':
        listar_estudos()
        tempo(2)
        limpa()
    elif opcao == '3':
        remover_estudo()
        tempo(1)
        limpa()
    elif opcao == '0':
        limpa()
        while p<1:
            for i in saida:
                print(i, end = '\r')
                time.sleep(0.6)
            p += 1
        break
    else:
        print('Opção invalida')
        tempo(1)
        limpa()

