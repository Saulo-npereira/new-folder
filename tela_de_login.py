from tkinter import *
contas = [('saulo', '123'), ('maria', '444')]
def salvar():
    nome1 = entrada_nome.get()
    senha1 = entrada_senha.get()
    if (nome1, senha1) in contas:
        tela_login.pack_forget()
        tela_principal.pack()
    else:
        aprov.configure(text='senha ou usuario não aprovado')
        
    

janela = Tk()
tela_login = Frame(janela)
tela_login.pack()
frame = Frame(tela_login, height=100)
frame.pack()
label_login = Label(tela_login, text='LOGIN')
label_login.pack(pady=50)
nome = Label(tela_login, text='NOME')
nome.pack(padx=5, pady=5)

entrada_nome = Entry(tela_login)
entrada_nome.pack(padx=5, pady=5)

frame2 = Frame(tela_login, height=50)
frame2.pack()

senha = Label(tela_login, text='SENHA')
senha.pack(padx=10, pady=5)

entrada_senha = Entry(tela_login)
entrada_senha.pack(padx=5, pady=5)
but = Button(tela_login, text='SALVAR', command=salvar, bg ='green', fg='white')
but.pack()
aprov = Label(tela_login, text='')
aprov.pack()

tela_principal = Frame()
frame3 = Frame(tela_principal, height=300)
frame3.pack()
label_principal = Label(tela_principal, text='bem vindo a tela principal')
label_principal.pack()

janela.mainloop()