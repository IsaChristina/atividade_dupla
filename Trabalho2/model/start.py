import sys
sys.path.append("C:/Users/900226/Desktop/exercicios/atividade_dupla/Trabalho2")

from flask import Flask, render_template, redirect, request

from dao.listar import Listar
from dao.dao_pessoas import Pessoa_db
from dao.dao_linguagens import Linguagem_db
from dao.dao_funcionarios import Funcionario_db
from dao.dao_equipes import Equipe_db

from model.pessoas import Pessoa
from model.equipes import Equipe
from model.linguagens import Linguagem
from model.funcionarios import Funcionario



app = Flask(__name__, template_folder = '../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listagem')
def listagem():
    listar = Listar()
    lista_pessoa = listar.listar_pessoas()
    lista_funcionario = listar.listar_funcionarios()
    lista_equipe = listar.listar_equipes()
    lista_linguagem = listar.listar_linguagens()
    return render_template('listagem.html', pessoa = lista_pessoa, funcionario = lista_funcionario, equipe = lista_equipe, linguagem = lista_linguagem)

@app.route('/salvar_pessoa')
def salvar_pessoa():
    pessoa = Pessoa_db()
    nome = request.args["nome"]
    cpf = request.args["cpf"]
    telefone = request.args["telefone"]
    pessoa.set_cadastrar(nome, cpf, telefone)
    pessoa.cadastrar_db(pessoa.get_cadastrar())
    return redirect('/')

@app.route('/salvar_funcionario')
def salvar_funcionario():
    funcionario = Funcionario_db()
    idpessoal = request.args["id-pessoal"]
    cargo = request.args["cargo"]
    salario = request.args["salario"]
    funcionario.set_cadastrar(cargo, salario, idpessoal)
    funcionario.cadastrar_db(funcionario.get_cadastrar())
    return redirect('/')

@app.route('/salvar_linguagem')
def salvar_linguagem():
    linguagem = Linguagem_db()
    nome = request.args["linguagem"]
    linguagem.set_cadastrar(nome)
    linguagem.cadastrar_db(linguagem.get_cadastrar())
    return redirect('/')

@app.route('/salvar_equipe')
def salvar_equipe():
    equipe = Equipe_db()
    funcionario1 = request.args["funcionario1"]
    funcionario2 = request.args["funcionario2"]
    funcionario3 = request.args["funcionario3"]
    funcionario4 = request.args["funcionario4"]
    equipe.set_cadastrar(funcionario1, funcionario2, funcionario3, funcionario4)
    equipe.cadastrar_db(equipe.get_cadastrar())
    return redirect('/')


app.run(debug=True)