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
    
    def get_id(self):
        return str(self.id)
    
    def instanciar(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha