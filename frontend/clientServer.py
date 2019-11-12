from flask import Flask, render_template, jsonify, request, redirect, url_for
from model import Pessoa
import requests
from playhouse.shortcuts import dict_to_model
import json
# https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html
# pip3 install requests
# necessário para fazer chamadas get no python: acessar o backend

app = Flask(__name__)

lista_produtos = []

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter do backend a lista de pessoas
    dados_pessoas = requests.get('http://localhost:4999/listar_pessoas')
    # converter os dados recebidos para o formato json
    json_pessoas = dados_pessoas.json()
    # inicializar a lista de pessoas
    pessoas = []
    # percorrer as pessoas em json
    for pessoa_em_json in json_pessoas['lista']:
        
        # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#dict_to_model
        # converter a pessoa em json para pessoa do peewee
        p = dict_to_model(Pessoa, pessoa_em_json)
        # adicionar a pessoa convertida na lista de pessoas
        pessoas.append(p)
    
    # fornecer a lista de pessoas para a página exibir as pessoas
    return render_template("produto_listar.html", lista = pessoas)


@app.route("/produto/", methods=['GET'])
def produto():
    response = requests.get('http://localhost:5000/produto/')      
    lista_produtos = json.loads(response.text)
    return render_template("produto_listar.html", response = lista_produtos)

@app.route("/produto/criar/", methods=['GET', 'POST'])
def produto_criar():
    # cria um novo produto
    # produto = request.args.post('produto')
    if request.method == 'GET':
        return render_template("produto_criar.html")
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
        return render_template("produto_editar.html", produto = produto[0])
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

app.run(debug=True, port=4999)