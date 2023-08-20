from tkinter import *
import tkinter as tk

def pegar_imc():

  peso = float(peso_pessoa.get())
  altura = float(altura_pessoa.get())

  imc = peso / altura**2

  resultado = imc

  if imc < 18.5:
    msg['text'] ='Abaixo do peso'
  elif imc >= 18.5 and imc < 25:
    msg['text'] ='Peso normal'
  elif imc >= 25 and imc < 30:
    msg['text'] ='Acima do peso'
  else:
    msg['text'] = 'Obesidade'

  label_salvo['text'] = "{:.{}f}".format(resultado, 2)
 
janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg="gray")
janela.geometry('500x425')

nome_calculadra = Label(janela, text= "Calculadora")
nome_calculadra.grid(column = 0, row = 0)
nome_calculadra.place(relx=.5, rely=.05, anchor="center")


peso = Label(janela, text= "Digite seu peso")
peso.grid(row=0, column=0)
peso.place(relx=.3, rely=.2, anchor="center")

peso_pessoa = tk.Entry(janela)
peso_pessoa.grid(row=0 ,column=0)
peso_pessoa.place(relx=.6, rely=.2, anchor="center")

altura = Label(janela, text= "Digite sua altura")
altura.grid(row=2, column=0)
altura.place(relx=.3, rely=.3, anchor="center")

altura_pessoa = tk.Entry(janela)
altura_pessoa.grid(row=2, column=0)
altura_pessoa.place(relx=.6, rely=.3, anchor="center")

botao = Button(janela, text="Calcular", command=pegar_imc)
botao.grid(row=4, column=0)
botao.place(relx=.4, rely=.4)

label_salvo = Label(janela, text="", background="gray")
label_salvo.grid(row=6, column=2)
label_salvo.place(relx=.5, rely=.6, anchor="center")

imc = Label(janela, text= "Seu IMC é:")
imc.grid(row=6, column=0)
imc.place(relx=.3, rely=.6, anchor="center")

msg = Label(janela, text="", background="gray")
msg.grid(row=9, column=1)
msg.place(relx=.5, rely=.8, anchor="center")

janela.mainloop()