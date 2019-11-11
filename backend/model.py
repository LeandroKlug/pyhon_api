from peewee import *

arq = './database.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()

class Produto(BaseModel):
    produto_nome = CharField()
    produto_valor = DecimalField()
    produto_descricao = CharField()

if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa, Produto])
    joao = Pessoa.create(nome="Joao da Silva", 
        endereco="Casa 9", telefone="3541-1230")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone)