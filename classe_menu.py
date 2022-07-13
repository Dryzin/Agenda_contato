from class_DB_agenda import *

class Menu:
    def __init__(self):
        function = DBAestoque()


        while True:
            entrada = input('1 - Cadastrar\n2 - Listar \n3 - Atualizar Descrição\n4 - Procurar Produto \n5 - Excluir \n0 - Sair\n')

            if entrada == '1':

                num1 = str(input('Deseja:\n'
                                    '1 - Cadastrar Novo Produto\n'
                                    '2 - Cadastrar Novo Fabricante\n'
                                    '0 - Voltar\n'))
                if num1 == '1':
                    cod = None
                    nome = input('Nome do produto: ')
                    quant = input('Quantidade: ')
                    atributo = 'Fabricante'
                    function.listar_produtos(atributo)
                    fabr = int(input('Entre com o ID do fabricante: '))
                    function.salvar_produtos(cod, nome, fabr, quant)

                elif num1 == '2':
                    cod = None
                    nome = input('Entre com o Nome do Fabricante: ')
                    cnpj = input('Entre com o CNPJ do fabricante: ')
                    local = input('Entre com o Endereço do fabricante: ')
                    function.salva_fabricante(cod, nome, cnpj, local)
                    
                elif num1 == '0':
                    pass
                    
                else: pass


            elif entrada == '2':

                num1 = str(input('Deseja:\n'
                                    '1 - Listar Produtos\n'
                                    '2 - Listar Fabricante\n'
                                    '0 - Voltar\n'))
                if num1 == '1':
                    atributo = 'Estoque'
                    function.listar_produtos(atributo)

                elif num1 == '2':
                    atributo = 'Fabricante'
                    function.listar_produtos(atributo)

                elif num1 == '0':
                    pass
                    
                else: pass

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
