class main:
    def __init__(self):
        function1 = Func()

        while True:
                entrada = input('\n1 - Cadastrar\n2 - Listar Todos\n3 - Procurar Produto\n4 - Alterar Produto\n5 - Mov.Entrada\n0 - Sair\n')

                if entrada == '1':
                    function1.salvar_prod()

                elif entrada == '2':
                    function1.listar_prod()

                elif entrada == '3':
                    function1.procurar()

                elif entrada == '4':
                    function1.alterar()

                elif entrada == '5':
                    function1.mov()

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


    def mov(self):
        for i in range(len(self.listaProdutos)):
            x= i+1
        print("Total de movimentaçõe de entrada: ",x)



class Inf:
    def __init__(self):
        self.cod = input("Informe codigo: ")
        self.desc = input("Informe nome: ")
        self.fabricante = input("Informe fabricante: ")
        self.quant = input("Informe a quantidade: ")

'''class entrada:

    def mov(self):
        for i in range(len(self.listaProdutos)):
            x= i+1
        print("Total de movimentaçõe de entrada: ",x)
    

menu = main()'''