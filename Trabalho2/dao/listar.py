from dao.conexao import Conexao

class Listar(Conexao):

# //////////////////

    def listar_pessoas(self):

        self.cursor.execute('Select * from Pessoas')
        
        return self.cursor.fetchall()
        
# //////////////////

    def listar_funcionarios(self):

        self.cursor.execute('Select * from Funcionarios')
        
        return self.cursor.fetchall()
        
# //////////////////

    def listar_equipes(self):

        self.cursor.execute('Select * from Equipes')
        
        return self.cursor.fetchall()
        
# //////////////////

    def listar_linguagens(self):

        self.cursor.execute('Select * from Linguagens')
        
        return self.cursor.fetchall()