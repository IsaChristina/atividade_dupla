from model.pessoas import Pessoa


class Pessoa_db(Pessoa):

# //////////////////

    def cadastrar_db(self, pessoa):

        self.cursor.execute(f"Insert into Pessoas (Nome, Cpf, Telefone) values ('{pessoa['Nome']}', "
                            f"{pessoa['Cpf']}, {pessoa['Telefone']})")

        self.conexao.commit()

# //////////////////

    def editar_db(self, pessoa):

        self.cursor.execute(f"Update Pessoas Set Nome = '{pessoa['Nome']}', Cpf = {pessoa['Cpf']}, "
                            f"Telefone = {pessoa['Telefone']} where Id = {pessoa['Id']}")

        self.conexao.commit()

# //////////////////

    def deletar_db(self, id):

        self.cursor.execute(f"Delete from Pessoas where Id = {id}")

        self.conexao.commit()

        return True