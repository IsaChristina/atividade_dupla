from model.equipes import Equipe


class Equipe_db(Equipe):

# //////////////////

    def cadastrar_db(self, equipe):

        self.cursor.execute(f"Insert into Equipes values (DEFAULT, {equipe['Id_1']}, "
                            f"{equipe['Id_2']}, {equipe['Id_3']}, {equipe['Id_4']})")

        self.conexao.commit()

# //////////////////

    def editar_db(self, equipe):

        self.cursor.execute(f"Update Equipes Set Pessoa_1 = {equipe['Id_1']}, Pessoa_2 = {equipe['Id_2']},"
                            f" Pessoa_3 = {equipe['Id_3']}, Pessoa_4 = {equipe['Id_4']}")

        self.conexao.commit()

# //////////////////

    def deletar_db(self, id):

        self.cursor.execute(f"Delete from Equipes where Id = {id}")

        self.conexao.commit()