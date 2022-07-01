class main:
    def __init__(self):
        function1 = Func()
        function2 = Compra()
        function2.ent = function1

        while True:
                entrada = input('\n1 - Cadastrar\n2 - Listar Todos\n3 - Procurar Produto\n4 - Alterar Produto\n5 - Mov.Entrada\n6 - Mov.Saída\n0 - Sair\n')

                if entrada == '1':
                    function1.salvar_prod()

                elif entrada == '2':
                    function1.listar_prod()

                elif entrada == '3':
                    function1.procurar()

                elif entrada == '4':
                    function1.alterar()

                elif entrada == '5':
                    function2.mov()

                elif entrada == '6':
                    function2.said()

                elif entrada == '':
                    function1.listar_prod()

                elif entrada == '0':
                    break

                else:
                    print('Opção inválida')

class Func:
    def __init__(self):
        self.listaProdutos = []
    
    def salvar_prod(self):
        self.listaProdutos.append(Inf())

    def listar_prod(self):
        for i in range(len(self.listaProdutos)):
            print('\nCódigo -',self.listaProdutos[i].cod,'\nNome -', self.listaProdutos[i].desc,'\nFabricante -',self.listaProdutos[i].fabricante,'\nQuantidade -',self.listaProdutos[i].quant)

    def procurar(self):
        b = input("\nInforme o código do Produto: ")
        for x in range(len(self.listaProdutos)):
            if b == self.listaProdutos[x].cod:
                print(self.listaProdutos[x].cod," - ",self.listaProdutos[x].desc, "-", self.listaProdutos[x].quant)
            else:
                pass

    def alterar(self):
        b = input("Informe o código do número de mudança: ")

        for x in range(len(self.listaProdutos)):
           if  b == self.listaProdutos[x].cod:
                self.listaProdutos[x].desc = input('Digite a nova descrição: ')



class Inf:
    def __init__(self):
        self.cod = int(input("Informe codigo: "))
        self.desc = input("Informe nome: ")
        self.fabricante = input("Informe fabricante: ")
        self.quant = int(input("Informe a quantidade: "))

        '''self.fabricante = objeto.nome'''

class Compra:

    def __init__(self):
        self.ent = Func()

    def mov(self):

        num = int(input('Cod do produto: '))

        for i in range(len(self.ent.listaProdutos)):
            print(self.ent.listaProdutos[i].cod)
            if num == self.ent.listaProdutos[i].cod:
                self.ent.listaProdutos[i].quant += int(input("Informe a quantidade comprada: "))
            
            else:
                print("ERRO")
        

    def said(self):

        num = int(input('Cod do produto: '))

        for i in range(len(self.ent.listaProdutos)):
            print(self.ent.listaProdutos[i].cod)
            if num == self.ent.listaProdutos[i].cod:
                self.ent.listaProdutos[i].quant -= int(input("Informe a quantidade comprada: "))
            
            else:
                print("ERRO")

class Fabricante:
    def __init__(self):
        self.cod_f = input("Informe codigo do Fabricante: ")
        self.desc_f = input("Informe nome do Fabricante: ")


menu = main()
