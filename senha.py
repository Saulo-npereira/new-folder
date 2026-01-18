import time
def lin():
    print('—' * 30)

lin()
print('LOJAS SAULO')
lin()

time.sleep(1)
print('USUARIOS:\n[ADMIN] = 1\n[FUNCIONARIO] = 2')
time.sleep(0.5)
print('\n')
usuario=int(input('USUARIO: '))
senha=int(input('SENHA: '))
n = 2
if usuario == 1 and senha == 762:
    print('acesso liberado')
elif usuario == 1 and senha != 762:
    while n > 0 and senha != 762:
        print(f'acesso negado, {n} tentivas')
        senha=int(input('senha: '))
        n -= 1
        if n == 0:
            print('TENTATIVAS ESGOTADAS')
        if senha == 762:
            print('acesso liberado')
elif usuario == 2 and senha == 1234:
    print('acesso liberado')
elif usuario == 2 and senha != 1234:
    while n > 0 and senha != 1234:
        print(f'acesso negado, {n} tentativas')
        senha=int(input('senha: '))
        n -= 1
        if n == 0 and senha != 1234 :
            print('TENTATIVAS ESGOTADAS')
        if senha == 1234:
            print('acesso liberado')

