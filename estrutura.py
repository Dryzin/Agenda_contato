from tkinter import *
from unicodedata import numeric
from class_DB_agenda import *
#criar janela

root = Tk()
fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
fr4 = Frame(root)

#geometria
root.geometry('230x180')

function = DBAestoque()


def salvar() :
    cod = None
    nome = ent1.get()
    quant = ent2.get()
    fabr = ent3.get()
    print(nome, quant, fabr)
    function.salvar_produtos(cod, nome, fabr, quant)



root.grid_rowconfigure(0,  weight=1)
root.grid_rowconfigure(1,  weight=1)
root.grid_rowconfigure(2,  weight=1)
root.grid_rowconfigure(3,  weight=1)
root.grid_rowconfigure(5,  weight=1)



root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)




fr1.grid(row=1, column=0, sticky=NSEW)

#criar os widgets

lb1 = Label(fr1, text='Estrutura')
bt1 = Button(fr1, text='Cadastro', command = lambda: [fr1.grid_remove(), fr2.grid(row=0, column=1)])
bt2 = Button(fr1, text='Listar')
bt3 = Button(fr1, text='Atualizar descrição')
bt4 = Button(fr1, text='Procurar Produto')
bt5 = Button(fr1, text='Excluir')
bt6 = Button(fr1, text='Sair')


#organizar os widgets

lb1.grid(row=0, column=2, sticky=NSEW)

bt1.grid(row=1, column=1, sticky=NSEW)
bt2.grid(row=2, column=1, sticky=NSEW)
bt3.grid(row=1, column=3, sticky=NSEW)
bt4.grid(row=2, column=3, sticky=NSEW)
bt5.grid(row=3, column=1, sticky=NSEW)

bt6.grid(row=5, column=2, sticky=NSEW)

#frame 2

bt1 = Button(fr2, text='Cadastrar Produto', command = lambda: [fr2.grid_remove(), fr3.grid(row=0, column=1)])
bt2 = Button(fr2, text='Cadastrar Fabricante', command = lambda: [fr2.grid_remove(), fr3.grid(row=0, column=1)])

#organizar os widgets 2
bt1.grid(row=1, column=1, sticky=NSEW)
bt2.grid(row=1, column=2, sticky=NSEW)


#frame 3

lb1 = Label(fr3, text='Produto')
lb2 = Label(fr3, text='Nome: ')
lb3 = Label(fr3, text='Quantidade: ')
lb4 = Label(fr3, text='ID do Fabricante: ')
ent1 = Entry(fr3, text='') #nome
ent2 = Entry(fr3, text='')# quant
ent3 = Entry(fr3, text='')# id fabri
bt1 = Button(fr3, text='Salvar', command= salvar)



#organizar os widgets 3

lb1.grid(row=2, column=2, sticky=NSEW)

lb2.grid(row=3, column=1, sticky=NSEW)
ent1.grid(row=3, column=2, sticky=NSEW)

lb3.grid(row=4, column=1, sticky=NSEW)
ent2.grid(row=4, column=2, sticky=NSEW)

lb4.grid(row=5, column=1, sticky=NSEW)
ent3.grid(row=5, column=2, sticky=NSEW)

bt1.grid(row=6, column=1, sticky=NSEW)


#executar a janela
root.mainloop()