import sys
sys.path.append("C:/Users/900226/Desktop/exercicios/atividade_dupla/Trabalho2/")
from model.funcionarios import Funcionario


class Funcionario_db(Funcionario):

# //////////////////

    def cadastrar_db(self, funcionario):

        self.cursor.execute(f"Insert into Funcionarios values (DEFAULT, '{funcionario['Cargo']}', "
                            f"{funcionario['Salario']}, {funcionario['Id_pessoal']})")

        self.conexao.commit()

# //////////////////

    def editar_db(self, funcionario):

        self.cursor.execute(f"Update Funcionarios Set Cargo = '{funcionario['Cargo']}', "
                            f"Salario = {funcionario['Salario']}")

        self.conexao.commit()

# //////////////////

    def deletar_db(self, id):

        self.cursor.execute(f"Delete from Funcionarios where Id = {id}")

        self.conexao.commit()

        return True