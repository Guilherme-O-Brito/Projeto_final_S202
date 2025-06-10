class Vendedor:
    def __init__(self, nome:str, email:str, descricao:str, produtos, pais_de_origem:str):
        self.nome = nome
        self.email = email
        self.descricao = descricao
        self.produtos = produtos
        self.pais_de_origem = pais_de_origem
    
    def __str__(self):
        return f'Vendedor: {self.nome} do {self.pais_de_origem}'