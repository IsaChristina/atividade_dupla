from model.linguagens import Linguagem


class Linguagem_db(Linguagem):

# //////////////////

    def cadastrar_db(self, linguagem):

        self.cursor.execute(f"Insert into Linguagens values (DEFAULT, '{linguagem}')")

        self.conexao.commit()

# //////////////////

    def editar_db(self, linguagem):

        self.cursor.execute(f"Update Linguagens Set Nome = '{linguagem[1]}' where Id = {linguagem[0]}")

        self.conexao.commit()

# //////////////////

    def deletar_db(self, id):

        self.cursor.execute(f"Delete from Funcionarios where Id = {id}")

        self.conexao.commit()