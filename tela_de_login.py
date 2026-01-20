from tkinter import *
import time
contas = [('saulo', '123'), ('maria', '444')]
p = 2
s = 2
i = 5
def nao_mostrarc():
    global s
    entrada_senhac.configure(show='*')
    s += 1
def mostrarc():
    global s
    if s % 2==0:
        entrada_senhac.configure(show='')
        s += 1
    else:
        nao_mostrarc()
def entrar():
    tela_cadastrar.pack_forget()
    tela_login.pack()
def cadastrar():
    tela_login.pack_forget()
    tela_cadastrar.pack()
def nao_mostrar():
    global p
    entrada_senha.configure(show='*')
    p  +=1
def mostrar():
    global p
    if p % 2==0:
        entrada_senha.configure(show='')
        p +=1
    else:
        nao_mostrar()
def bloquear():
    but.configure(state='disabled')
def desbloquear():
    but.configure(state='normal')

def salvar():
    global i
    nome1 = entrada_nome.get()
    senha1 = entrada_senha.get()
    if (nome1, senha1) in contas:
        tela_login.pack_forget()
        tela_principal.pack()
    else:
        aprov.configure(text=f'senha ou usuario não aprovado, você tem mais {i} tentativas', fg='red')
        if i ==0:
            bloquear()
            i=5
        i -= 1
        
    

janela = Tk()
#tela login
tela_login = Frame(janela)
tela_login.pack()
frame = Frame(tela_login, height=100)
frame.pack()
label_login = Label(tela_login, text='LOGIN', font=('Verdana', 18, 'bold'))
label_login.pack(pady=50)
nome = Label(tela_login, text='NOME', font=('Verdana', 10, 'bold'))
nome.pack(padx=5, pady=5)

entrada_nome = Entry(tela_login)
entrada_nome.pack(padx=5, pady=5)

frame2 = Frame(tela_login, height=50)
frame2.pack()

senha = Label(tela_login, text='SENHA', font=('Verdana', 10, 'bold'))
senha.pack(padx=10, pady=5)
frame_senha = Frame(tela_login)
frame_senha.pack()
entrada_senha = Entry(frame_senha, show="*", cursor='xterm')
entrada_senha.pack(side=LEFT, padx=5, pady=5)
but_mostrar = Button(frame_senha, text='👁', command=mostrar, cursor='hand2')
but_mostrar.pack()
but = Button(tela_login, text='ENTRAR', command=salvar, bg ='green', fg='white', cursor='hand2', font=('Verdana', 10, 'bold'))
but.pack()
aprov = Label(tela_login, text='')
aprov.pack()
Frame(tela_login, height=200).pack()
frame5 = Frame(tela_login, width=1200)
frame5.pack(side=LEFT)
botao_logar = Button(tela_login, text='CADASTRAR-SE', fg='white', bg='red', command=cadastrar, font=('verdana', 10, 'bold'), cursor='hand2')
botao_logar.pack()
#fim tela login
#tela cadastrar
tela_cadastrar = Frame()
Frame(tela_cadastrar, height=100).pack()
label_cadastrar = Label(tela_cadastrar, text='CADASTRAR-SE', font=('verdana', 18, 'bold'))
label_cadastrar.pack(pady=50)
Label(tela_cadastrar, text='NOME', font=('verdana', 10, 'bold')).pack()
entrada_nomec = Entry(tela_cadastrar)
entrada_nomec.pack(pady=5)
Frame(tela_cadastrar, height=50).pack()
Label(tela_cadastrar, text='SENHA', font=('verdana', 10, 'bold')).pack()
frame_senhac = Frame(tela_cadastrar)
frame_senhac.pack()
entrada_senhac = Entry(frame_senhac, show='*')
entrada_senhac.pack(side=LEFT, pady=5)
but_mostrarc = Button(frame_senhac, text='👁', command=mostrarc, cursor='hand2')
but_mostrarc.pack()
but_salvar = Button(tela_cadastrar, text='SALVAR', font=('verdana', 10, 'bold'), fg='white', bg='green', cursor='hand2')
but_salvar.pack()
Frame(tela_cadastrar, height=250).pack()
Frame(tela_cadastrar, width=1200).pack(side=LEFT)
but_login = Button(tela_cadastrar, text='ENTRAR', command=entrar, fg='white', bg='red', font=('verdana', 10, 'bold'), cursor='hand2')
but_login.pack()
#fim tela cadastrar
#tela principal
tela_principal = Frame()
frame3 = Frame(tela_principal, height=300)
frame3.pack()
label_principal = Label(tela_principal, text='bem vindo a tela principal')
label_principal.pack()

janela.mainloop()