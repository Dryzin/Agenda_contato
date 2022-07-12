from class_DB_agenda import *

class Menu:
    def __init__(self):
        function = DBAestoque()


        while True:
            entrada = input('1 - Cadastrar\n2 - Listar \n3 - Atualizar informações\n4 - Excluir \n0 - Sair\n')

            if entrada == '1':
                cod = None
                nome = input('Nome do produto: ')
                quant = input('Quantidade: ')

                function.salvar_contatos(cod, nome, quant)


            elif entrada == '2':
                function.listar_contatos()

            elif entrada == '3':
                cod = input('Informe cod: ')
                nome = input('Nome do produto: ')
                atributo = 'Contatos' # Atributo lá da tabela o nome do q vai ser mudado
                function.alterar_contatos(atributo, nome, cod)

            elif entrada == '4':
                cod = input('Informe cod: ')
                atributo = 'Contatos' # Atributo lá da tabela o nome do q vai ser mudado
                function.excluir_contato(cod)

            elif entrada == '0':
                break

            else:
                print('Entrada incorreta!')
