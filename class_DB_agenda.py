import mysql.connector
from Informacoes import Fabricante, inf


class DBAestoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user='root',
            password="Dryq1w2e3$",
            database='BDA_Estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def salvar_produtos(self, cod, nome, fabr, quant):
        objcontato = inf(cod, nome, fabr,quant)
        comando_sql = f'insert into Estoque (nome, fabricante, quant) value ("{objcontato.nome}", "{objcontato.fabr}", "{objcontato.quant}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def salva_fabricante(self, cod, nome, cnpj, local):
        obj_fabricante = Fabricante(cod, nome, cnpj, local)
        sql = f'insert into Fabricante (nome, cnpj, endereço) value ("{obj_fabricante.nome}", "{obj_fabricante.cnpj}", "{obj_fabricante.local}")'
        self.meu_cursor.execute(sql)
        self.conexao.commit()

    def listar_produtos(self, atributo):
        comando_sql = f'select * from {atributo}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_produtos(self, atributo, valor, cod):
        comando_sql = f'update Estoque set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

        # neste caso apenas troca o nome

    def procurar(self, cod):
        comando_sql = f'select * from Estoque where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def excluir_produtos(self, cod):
        comando_sql = f'delete from Estoque where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

        # neste caso exclui todo elemento