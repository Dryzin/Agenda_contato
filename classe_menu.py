from class_DB_agenda import *

class Menu:
    def __init__(self):
        function = DBAestoque()


        while True:
            entrada = input('1 - Cadastrar\n2 - Listar Produtos \n3 - Atualizar Descrição\n4 - Procurar Produto \n5 - Excluir \n0 - Sair\n')

            if entrada == '1':
                cod = None
                nome = input('Nome do produto: ')
                quant = input('Quantidade: ')

                function.salvar_produtos(cod, nome, quant)


            elif entrada == '2':
                function.listar_produtos()

            elif entrada == '3':
                cod = input('Informe cod: ')
                nome = input('Novo nome do produto: ')
                atributo = 'nome' # Atributo lá da tabela o nome do q vai ser mudado
                function.alterar_produtos(atributo, nome, cod)

            elif entrada == '4':
                cod = input('Informe cod: ')
                function.procurar(cod)

            elif entrada == '5':
                cod = input('Informe cod: ')
                atributo = 'Estoque' # Atributo lá da tabela o nome do q vai ser mudado
                function.excluir_produtos(cod)

            elif entrada == '0':
                break

            else:
                print('Entrada incorreta!')
