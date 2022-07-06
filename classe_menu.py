from class_DB_agenda import *

class Menu:
    def __init__(self):
        agenda = DBAgenda()


        while True:
            entrada = input('1 - Novo Contato\n2 - Listar Contatos\n3 - Mudar Contato\n0 - Sair\n')

            if entrada == '1':
                cod = None
                nome = input('Entre com o Nome: ')
                telefone = input('Entre com o Telefone: ')

                agenda.salvar_contatos(cod, nome, telefone)


            elif entrada == '2':
                agenda.listar_contatos()

            elif entrada == '3':
                cod = None
                nome = input('Entre com o Nome: ')
                telefone = input('Entre com o Telefone: ')
                atributo = 'nome' # Atributo lá da tabela o nome do q vai ser mudado
                agenda.alterar_contatos(atributo, cod)

            elif entrada == '0':
                break

            else:
                print('Entrada incorreta!')
