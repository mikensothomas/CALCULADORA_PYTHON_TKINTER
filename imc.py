from tkinter import *

tela = Tk()

# Definição que vai "pegar" o texto da lbl e salvar em uma variável global
def salvar_dados():
   # Vamos criar uma variável global
   global armazenar_nome

   # Vamos dizer que ela recebe o texto do widget Entry
   armazenar_nome = nome_do_cliente.get()

# Texto Nome:
texto = Label(tela, text="Nome: ")
# Widget de Entrada
nome_do_cliente = Entry(tela)
# Botão de confirmação 
btn_enviar = Button(tela, text="Enviar",command=salvar_dados)

# Definindo a geometria de tela, eu não sei trabalhar bem com .pack()
texto.grid(row=1,column=1)
nome_do_cliente.grid(row=1,column=2)
btn_enviar.grid(row=2,column=1,columnspan=2)


'''A partir daqui só tem código referente a recuperação da variável com o nome do cliente'''


def recuperar():
    # Vamos tornar a variável disponível nessa definição
    global armazenar_nome

    # Vamos fazer o lbl_salvo receber o nome do cliente, armazenado na variável global
    lbl_salvo["text"] = armazenar_nome

# Label que vai receber o conteúdo da variável global
lbl_salvo = Label(tela, text="Aqui vai aparecer o nome do cliente")

# Botão que vai acionar o evento recuperar
btn_recuperar = Button(tela, text="Qual é o nome do cliente?",command=recuperar)

# Definindo a geometria de tela, eu não sei trabalhar bem com .pack()
lbl_salvo.grid(row=3,column=1,columnspan=2)
btn_recuperar.grid(row=4, column=1, columnspan=2)

tela.mainloop()