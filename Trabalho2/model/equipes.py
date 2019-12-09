from dao.conexao import Conexao

class Equipe(Conexao):

# //////////////////

    def set_cadastrar(self, ps1, ps2, ps3, ps4):

        self.ps1 = ps1
        self.ps2 = ps2
        self.ps3 = ps3
        self.ps4 = ps4

    def get_cadastrar(self):

        return {'Id_1':self.ps1, 'Id_2':self.ps2, 'Id_3':self.ps3, 'Id_4':self.ps4}

# //////////////////

    def set_editar(self, id_equipe, ps1, ps2, ps3, ps4):

        self.id_equipe = id
        self.ps1 = ps1
        self.ps2 = ps2
        self.ps3 = ps3
        self.ps4 = ps4

    def get_editar(self):

        return {'Id_equipe':self.id_equipe, 'Id_1':self.ps1, 'Id_2':self.ps2, 'Id_3':self.ps3, 'Id_4':self.ps4}

