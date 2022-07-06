import mysql.connector
from contatos import Contato


class DBAgenda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user='root',
            password="q1w2e3",
            database='agenda'
        )
        self.meu_cursor = self.conexao.cursor()

    def salvar_contatos(self, cod, nome, telefone):
        objcontato = Contato(cod, nome, telefone)
        comando_sql = f'insert into Contatos (nome, telefone) value ("{objcontato.nome}", "{objcontato.telefone}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar_contatos(self):
        comando_sql = f'select * from Contatos'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_contatos(self, atributo, valor, cod):
        comando_sql = f'update Contatos set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir_contato(self, cod):
        comando_sql = f'delete from Contatos where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()