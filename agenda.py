from contatos import*

class Agenda:
    def __init__(self):
        self.listaContatos = []
    
    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('\nCódigo -',self.listaContatos[i].cod,'\nNome -', self.listaContatos[i].nome,'/n')

    def mudar_contato(self):
        b = input("buscar o contato por nome para mudar")
        for i in range(len(self.listaContatos)):
            if b == self.listaContatos[i].cod:
                self.listaContatos[i].telefone = input('Digite o novo número')

