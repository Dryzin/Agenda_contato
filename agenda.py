from contatos import*

class Agenda:
    def __init__(self):
        self.listaContatos = []
    
    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('\nCódigo -',self.listaContatos[i].cod,'\nNome -', self.listaContatos[i].nome,'\nTelefone -',self.listaContatos[i].telefone,'\n')

    def mudar_contato(self):
        b = input("Informe o código do número de mudança: ")

        for x in range(len(self.listaContatos)):
           if  b == self.listaContatos[x].cod:
                self.listaContatos[x].telefone = input('Digite o novo número: ')