from Informacoes import*

class Funcion:
    def __init__(self):
        self.listaContatos = []
    
    def salvar_contatos(self):
        self.listaContatos.append(inf())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('\nCódigo -',self.listaContatos[i].cod,'\nNome -', self.listaContatos[i].nome,'\nQuantidade: -',self.listaContatos[i].quant,'\n')

    def mudar_contato(self):
        b = input("Informe o código do número de mudança: ")

        for x in range(len(self.listaContatos)):
           if  b == self.listaContatos[x].cod:
                self.listaContatos[x].quant = input('Digite o novo número: ')