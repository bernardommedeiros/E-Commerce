from flask_login import login_manager
from ecommerce import db

class Usuario():
    id = int
    nome = str
    email = str
    senha = str

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    @login_manager.user_loader
    def load_user(id):
        cursor = db.cursor()
        usuarioDB = cursor.fetchall("SELECT * FROM users WHERE id = %s", (id))
        return Usuario(usuarioDB[0], usuarioDB[1], usuarioDB[2], usuarioDB[3])
    
    def get_id(self):
        return str(self.id)
    
    def instanciar(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha