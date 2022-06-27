from agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()


        while True:
            entrada = input('1 - Novo Contato\n2 - Listar Contatos\n3 - Mudar Contato\n0 - Sair\n')
            if entrada == '1':
                agenda.salvar_contatos()

            elif entrada == '2':
                agenda.listar_contatos()

            elif entrada == '3':
                agenda.mudar_contato()

            elif entrada == '0':
                break

            else:
                print('Opção inválida')
