import mysql.connector
from Informacoes import inf


class DBAestoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user='root',
            password="Dryq1w2e3$",
            database='BDA_Estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def salvar_produtos(self, cod, nome, quant):
        objcontato = inf(cod, nome, quant)
        comando_sql = f'insert into Estoque (nome, quant) value ("{objcontato.nome}", "{objcontato.quant}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar_produtos(self):
        comando_sql = f'select * from Estoque'
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