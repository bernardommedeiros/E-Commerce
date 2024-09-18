from flask_login import UserMixin

class Usuario(UserMixin):
    id = 0
    nome = ""
    email = ""
    senha = ""
    
    def instanciar(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha