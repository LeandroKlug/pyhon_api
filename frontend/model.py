from peewee import *

# http://docs.peewee-orm.com/en/latest/peewee/database.html#using-sqlite
# a leitura de dados será apenas em memória, 
# temporário, para renderizar os dados
arq = ':memory:'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    cliente_nome = CharField()
    cliente_endereco = CharField()
    cliente_telefone = CharField()

class Produto(BaseModel):
    produto_nome = CharField()
    produto_valor = DecimalField()
    produto_descricao = CharField()

class Pedido(BaseModel):
    cliente_nome = ForeignKeyField(Cliente)
    prduto_nome = ForeignKeyField(Produto) 
        
if __name__ == "__main__":
    db.connect()
    db.create_tables([Cliente, Produto, Pedido])
    joao = Cliente.create(nome="Joao da Silva", endereco="Casa 9", telefone="3541-1230")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone)