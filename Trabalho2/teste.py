from dao.dao_linguagens import Linguagem_db

teste = Linguagem_db()
teste.set_editar(1, 'Python 3')
teste.editar_db(teste.get_editar())

# teste2 = Pessoa_db()
# teste2.set_cadastrar('Junior', 5468435, 5761418)
# teste2.cadastrar_db(teste2.get_cadastrar())