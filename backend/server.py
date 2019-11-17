from flask import Flask, request, jsonify
from model import Cliente, Produto, Pedido
from playhouse.shortcuts import model_to_dict


app = Flask(__name__)



########  ########   #######  ########  ##     ## ########  #######  
##     ## ##     ## ##     ## ##     ## ##     ##    ##    ##     ## 
##     ## ##     ## ##     ## ##     ## ##     ##    ##    ##     ## 
########  ########  ##     ## ##     ## ##     ##    ##    ##     ## 
##        ##   ##   ##     ## ##     ## ##     ##    ##    ##     ## 
##        ##    ##  ##     ## ##     ## ##     ##    ##    ##     ## 
##        ##     ##  #######  ########   #######     ##     #######   


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

@app.route("/produto/excluir/<produto_id>/", methods=['DELETE'])
def produto_excluir(produto_id):
    Produto.delete_by_id(produto_id)
    
    return None



######  ##       #### ######## ##    ## ######## ######## 
##   ## ##        ##  ##       ###   ##    ##    ##       
##      ##        ##  ##       ####  ##    ##    ##       
##      ##        ##  ######   ## ## ##    ##    ######   
##      ##        ##  ##       ##  ####    ##    ##       
##   ## ##        ##  ##       ##   ###    ##    ##       
######  ######## #### ######## ##    ##    ##    ######## 


@app.route("/cliente/", methods=['GET', 'POST'])
def cliente():
    query = Cliente.select().dicts()
    itens = []
    for item in query:
        itens.append(item)

    return jsonify(itens)

@app.route("/cliente/criar/", methods=['GET', 'POST'])
def cliente_criar():
    Cliente.create(**request.get_json()).save()

    return None

@app.route("/cliente/editar/<cliente_id>/", methods=['GET', 'POST'])
def cliente_editar(cliente_id):
    if request.method == 'GET':
        query = Cliente.select().where(Cliente.id == cliente_id).dicts()
        itens = []
        for item in query:
            itens.append(item)

        print(itens)

        return jsonify(itens)

    else:
        info_frontend = request.get_json()
        q = (Cliente
            .update(
                {
                    Cliente.cliente_id: info_frontend['cliente_nome'],
                    Cliente.cliente_descricao: info_frontend['cliente_endereco'],
                    Cliente.cliente_valor: info_frontend['cliente_telefone'],
                }
            )
            .where(Cliente.id == cliente_id))
        q.execute() 
    return None

@app.route("/cliente/excluir/<cliente_id>/", methods=['DELETE'])
def cliente_excluir(cliente_id):
    Cliente.delete_by_id(cliente_id)
    
    return None  


                                                                                                     
########  ######## ########  #### ########   #######   ######  
##     ## ##       ##     ##  ##  ##     ## ##     ## ##    ## 
##     ## ##       ##     ##  ##  ##     ## ##     ## ##       
########  ######   ##     ##  ##  ##     ## ##     ##  ######  
##        ##       ##     ##  ##  ##     ## ##     ##       ## 
##        ##       ##     ##  ##  ##     ## ##     ## ##    ## 
##        ######## ########  #### ########   #######   ######  


@app.route("/pedidos/", methods=['GET', 'POST'])
def pedido():
    query = Pedido.select().dicts()
    itens = []
    for item in query:
        itens.append(item)

    return jsonify(itens)

@app.route("/pedido/criar/", methods=['GET', 'POST'])
def pedido_criar():
    Pedido.create(**request.get_json()).save()

    return None

@app.route("/pedido/editar/<pedido_id>/", methods=['GET', 'POST'])
def pedido_editar(pedido_id):
    if request.method == 'GET':
        query = Pedido.select().where(Pedido.id == pedido_id).dicts()
        itens = []
        for item in query:
            itens.append(item)

        print(itens)

        return jsonify(itens)

    else:
        info_frontend = request.get_json()
        q = (Pedido
            .update(
                {
                    Pedido.cliente_nome: info_frontend['cliente_nome'],
                    Pedido.produto_nome: info_frontend['produto_nome'],
                }
            )
            .where(Pedido.id == pedido_id))
        q.execute() 
    return None

@app.route("/pedido/excluir/<pedido_id>/", methods=['DELETE'])
def pedido_excluir(pedido_id):
    Pedido.delete_by_id(pedido_id)
    
    return None


if __name__ == '__main__':
    app.run(debug=True, port=5000)