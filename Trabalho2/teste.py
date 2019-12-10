import sys
sys.path.append("C:/Users/900218/Documents/Exercicios/atividade_dupla/Trabalho2/")

from dao.dao_linguagens import Linguagem_db

teste = Linguagem_db()
teste.set_cadastrar('PHP')
teste.cadastrar_db(teste.get_cadastrar())