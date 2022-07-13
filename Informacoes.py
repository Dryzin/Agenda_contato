class inf:
    # metodo(argumentos)
    def __init__(self, cod, nome, fabr,quant):
        self.cod = cod
        self.nome = nome
        self.fabr = fabr
        self.quant = quant
        
        print("Objeto Criado com sucesso")

#atributo é o cod, nome, telefone

class Fabricante:
    # metodo(argumentos)
    def __init__(self, cod, nome, cnpj, local):
        self.cod = cod
        self.nome = nome
        self.cnpj = cnpj
        self.local = local
        
        print("Fabricante Cadastrado com sucesso")