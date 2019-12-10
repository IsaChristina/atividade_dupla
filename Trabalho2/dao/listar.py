from dao.conexao import Conexao

class Listar(Conexao):

# //////////////////

    def listar_pessoas(self):

        lista = []

        self.cursor.execute('Select * from Pessoas')

        for i in self.cursor.fetchall():
            lista.append({'Id':i[0], 'Nome':i[1], 'Cpf':i[2], 'Telefone':i[3]})
        
        return lista
        
# //////////////////

    def listar_funcionarios(self):

        lista = []

        self.cursor.execute('Select * from Funcionarios')

        for i in self.cursor.fetchall():
            lista.append({'Id':i[0], 'Cargo':i[1], 'Salario':i[2], 'Id_pessoal':i[3]})
        
        return lista
        
# //////////////////

    def listar_equipes(self):

        lista = []

        self.cursor.execute('Select * from Equipes')

        for i in self.cursor.fetchall():
            lista.append({'Id':i[0], 'Pessoa_1':i[1], 'Pessoa_2':i[2], 'Pessoa_3':i[3], 'Pessoa_4':i[4]})
        
        return lista
        
# //////////////////

    def listar_linguagens(self):

        lista = []

        self.cursor.execute('Select * from Linguagens')

        for i in self.cursor.fetchall():
            lista.append({'Id':i[0], 'Nome':i[1]})
        
        return lista

# //////////////////

    def listagem_pessoal(self, id):

        lista = []

        self.cursor.execute('Select * from Linguagens where Id = ', id)

        for i in self.cursor.fetchall():
            lista.append({'Id':i[0], 'Nome':i[1]})
        
        return lista