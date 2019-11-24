from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests
from playhouse.shortcuts import dict_to_model
import json


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')



########  ########   #######  ########  ##     ## ########  #######  
##     ## ##     ## ##     ## ##     ## ##     ##    ##    ##     ## 
##     ## ##     ## ##     ## ##     ## ##     ##    ##    ##     ## 
########  ########  ##     ## ##     ## ##     ##    ##    ##     ## 
##        ##   ##   ##     ## ##     ## ##     ##    ##    ##     ## 
##        ##    ##  ##     ## ##     ## ##     ##    ##    ##     ## 
##        ##     ##  #######  ########   #######     ##     #######  

lista_produtos = []

@app.route("/produto/", methods=['GET'])
def produto():
    response = requests.get('http://localhost:5000/produto/')      
    lista_produtos = json.loads(response.text)
    return render_template("produto/produto_listar.html", response = lista_produtos)

@app.route("/produto/criar/", methods=['GET', 'POST'])
def produto_criar():
    # cria um novo produto
    # produto = request.args.post('produto')
    if request.method == 'GET':
        return render_template("produto/produto_criar.html")
    else:
        requests.post(
            'http://localhost:5000/produto/criar/', 
            json = 
                {
                    'produto_nome':request.form.get('produto_nome'),
                    'produto_valor':request.form.get('produto_valor'),
                    'produto_descricao':request.form.get('produto_descricao'),
                }            
        )
        return redirect(url_for("produto"))

@app.route("/produto/editar/<produto_id>/", methods=['GET', 'POST'])
def produto_editar(produto_id):
    if request.method == 'GET':
        response = requests.get('http://localhost:5000/produto/editar/' + produto_id + '/')
        produto = json.loads(response.text)
        return render_template("produto/produto_editar.html", produto = produto[0])
    else:
        requests.post(
            'http://localhost:5000/produto/editar/' + produto_id +'/', 
            json = 
                {
                    'produto_nome':request.form.get('produto_nome'),
                    'produto_valor':request.form.get('produto_valor'),
                    'produto_descricao':request.form.get('produto_descricao'),
                }            
        )
        return redirect(url_for("produto"))

@app.route("/produto/excluir/<produto_id>/", methods=['GET'])
def produto_excluir(produto_id):

    requests.delete('http://localhost:5000/produto/excluir/' + produto_id + '/')
   
    # produto = request.args.get('produto')
    # exclui um produto
    return redirect('produto')


                                                    
 ######  ##       #### ######## ##    ## ######## ######## 
##   ## ##        ##  ##       ###   ##    ##    ##       
##      ##        ##  ##       ####  ##    ##    ##       
##      ##        ##  ######   ## ## ##    ##    ######   
##      ##        ##  ##       ##  ####    ##    ##       
##   ## ##        ##  ##       ##   ###    ##    ##       
######  ######## #### ######## ##    ##    ##    ########  


lista_clientes = []

@app.route("/cliente/", methods=['GET'])
def cliente():
    response = requests.get('http://localhost:5000/cliente/')      
    lista_clientes = json.loads(response.text)
    return render_template("cliente/cliente_listar.html", response = lista_clientes)

@app.route("/cliente/criar/", methods=['GET', 'POST'])
def cliente_criar():
    # cria um novo cliente
    # cliente = request.args.post('cliente')
    if request.method == 'GET':
        return render_template("cliente/cliente_criar.html")
    else:
        requests.post(
            'http://localhost:5000/cliente/criar/', 
            json = 
                {
                    'cliente_nome':request.form.get('cliente_nome'),
                    'cliente_endereco':request.form.get('cliente_endereco'),
                    'cliente_telefone':request.form.get('cliente_telefone'),
                }            
        )
        return redirect(url_for("cliente"))

@app.route("/cliente/editar/<cliente_id>/", methods=['GET', 'POST'])
def cliente_editar(cliente_id):
    if request.method == 'GET':
        response = requests.get('http://localhost:5000/cliente/editar/' + cliente_id + '/')
        cliente = json.loads(response.text)
        return render_template("cliente/cliente_editar.html", cliente = cliente[0])
    else:
        requests.post(
            'http://localhost:5000/cliente/editar/' + cliente_id +'/', 
            json = 
                {
                    'cliente_nome':request.form.get('cliente_nome'),
                    'cliente_endereco':request.form.get('cliente_endereco'),
                    'cliente_telefone':request.form.get('cliente_telefone'),
                }            
        )
        return redirect(url_for("cliente"))

@app.route("/cliente/excluir/<cliente_id>/", methods=['GET'])
def cliente_excluir(cliente_id):

    requests.delete('http://localhost:5000/cliente/excluir/' + cliente_id + '/')
   
    # cliente = request.args.get('cliente')
    # exclui um cliente
    return redirect('cliente')



########  ######## ########  #### ########   #######   ######  
##     ## ##       ##     ##  ##  ##     ## ##     ## ##    ## 
##     ## ##       ##     ##  ##  ##     ## ##     ## ##       
########  ######   ##     ##  ##  ##     ## ##     ##  ######  
##        ##       ##     ##  ##  ##     ## ##     ##       ## 
##        ##       ##     ##  ##  ##     ## ##     ## ##    ## 
##        ######## ########  #### ########   #######   ######  


lista_pedidos = []

@app.route("/pedido/", methods=['GET'])
def pedido():
    response = requests.get('http://localhost:5000/pedido/')      
    lista_pedidos = json.loads(response.text)
    
    return render_template("pedido/pedido_listar.html", lista_pedidos = lista_pedidos)

@app.route("/pedido/criar/", methods=['GET', 'POST'])
def pedido_criar():
    # cria um novo pedido
    # pedido = request.args.post('pedido')
    if request.method == 'GET':

        response = requests.get('http://localhost:5000/cliente/')      
        lista_clientes = json.loads(response.text)

        response = requests.get('http://localhost:5000/produto/')      
        lista_produtos = json.loads(response.text)
        
        return render_template(
            "pedido/pedido_criar.html", 
            lista_clientes = lista_clientes,
            lista_produtos = lista_produtos)
    else:
        requests.post(
            'http://localhost:5000/pedido/criar/', 
            json = 
                {
                    'pedido_cliente':request.form.get('pedido_cliente'),
                    'pedido_produto':request.form.get('pedido_produto'),
                }            
        )
        return redirect(url_for("pedido"))


@app.route("/pedido/editar/<pedido_id>/", methods=['GET', 'POST'])
def pedido_editar(pedido_id):
    if request.method == 'GET':
        response = requests.get('http://localhost:5000/pedido/editar/' + pedido_id + '/')
        pedido = json.loads(response.text)
        return render_template("pedido/pedido_editar.html", pedido = pedido[0])
    else:
        requests.post(
            'http://localhost:5000/pedido/editar/' + pedido_id +'/', 
            json = 
                {
                    'pedido_cliente':request.form.get('pedido_cliente'),
                    'pedido_produto':request.form.get('pedido_produto'),
                }           
        )
        return redirect(url_for("pedido"))

@app.route("/pedido/excluir/<pedido_id>/", methods=['GET'])
def pedido_excluir(pedido_id):

    requests.delete('http://localhost:5000/pedido/excluir/' + pedido_id + '/')
   
    # pedido = request.args.get('pedido')
    # exclui um pedido
    return redirect('pedido')

app.run(debug=True, port=4999)