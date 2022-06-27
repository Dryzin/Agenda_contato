from contatos import*

class Agenda:
    def __init__(self):
        self.listaContatos = []
    
    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('\nCódigo -',self.listaContatos[i].cod,'\nNome -', self.listaContatos[i].nome,'\n Telefone -',self.listaContatos[i].telefone,'\n')

    def mudar_contato(self):
        b = input("Informe o código do número de mudança: ")
        c = input("Mudar Nome -[1]\nMudar Núemro -[2]\n")

        for i in range(len(self.listaContatos)):
            
            if b == self.listaContatos[i].cod and c == 1:
                    self.listaContatos[i].nome = input('Digite o novo nome: ')

            elif b == self.listaContatos[i].cod and c == 2:
                    self.listaContatos[i].telefone = input('Digite o novo número: ')

            else:
                pass
