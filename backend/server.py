from flask import Flask, request, jsonify
from model import Pessoa, Produto
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route("/")
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    # forma alternativa rápida: usando map (lambda)
    pessoas = list(map(model_to_dict, Pessoa.select()))
    return jsonify({'lista':pessoas}) # referência: https://www.geeksforgeeks.org/python-map-function/


@app.route("/produto/", methods=['GET', 'POST'])
def produto():
    query = Produto.select().dicts()
    itens = []
    for item in query:
        itens.append(item)

    return jsonify(itens)

@app.route("/produto/criar/", methods=['GET', 'POST'])
def produto_criar():
    Produto.create(**request.get_json()).save()

    return None

@app.route("/produto/editar/<produto_id>/", methods=['GET', 'POST'])
def produto_editar(produto_id):
    if request.method == 'GET':
        query = Produto.select().where(Produto.id == produto_id).dicts()
        itens = []
        for item in query:
            itens.append(item)

        print(itens)

        return jsonify(itens)

    else:
        info_frontend = request.get_json()
        q = (Produto
            .update(
                {
                    Produto.produto_nome: info_frontend['produto_nome'],
                    Produto.produto_descricao: info_frontend['produto_descricao'],
                    Produto.produto_valor: info_frontend['produto_valor'],
                }
            )
            .where(Produto.id == produto_id))
        q.execute() 
    return None

@app.route("/produto/excluir/", methods=['DELETE'])
def produto_excluir(produto_id):
    Produto.delete().where(Produto.id == produto_id).dicts()
    
    info_frontend = request.get_json()
    q = (Produto
        .delete(
            {
                Produto.produto_nome: info_frontend['produto_nome'],
                Produto.produto_descricao: info_frontend['produto_descricao'],
                Produto.produto_valor: info_frontend['produto_valor'],
            }
        )
        .where(Produto.id == produto_id))
    q.execute()

    return None


if __name__ == '__main__':
    app.run(debug=True, port=5000)