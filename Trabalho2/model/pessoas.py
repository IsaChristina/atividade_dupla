from dao.conexao import Conexao

class Pessoa(Conexao):

# //////////////////

    def set_cadastrar(self, nome, cpf, telefone):

        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def get_cadastrar(self):

        return {'Nome':self.nome, 'Cpf':self.cpf, 'Telefone':self.telefone}

# //////////////////

    def set_editar(self, id, nome, cpf, telefone):

        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def get_editar(self):

        return {'Id':self.id, 'Nome':self.nome, 'Cpf':self.cpf, 'Telefone':self.telefone}

