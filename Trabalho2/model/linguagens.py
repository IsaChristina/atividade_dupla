from dao.conexao import Conexao

class Linguagem(Conexao):

# //////////////////

    def set_cadastrar(self, nome):

        self.nome = nome

    def get_cadastrar(self):

        return self.nome

# //////////////////

    def set_editar(self, id, nome):

        self.id = id
        self.nome = nome

    def get_editar(self):

        return {'Id':self.id, 'Nome':self.nome}

