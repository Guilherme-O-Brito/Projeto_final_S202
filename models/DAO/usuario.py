class Usuario:
    # o parametro compras deve ser especificamente um array de produtos
    def __init__(self, nome:str, email:str, compras=[]):
        self.nome = nome
        self.email = email
        self.compras = compras
    
    def __str__(self):
        return f'Usuario: {self.nome} email: {self.email}'
    
    # retorna um dicionario representando o usuario
    def to_dict(self) -> dict:

        produtos = []
        for produto in self.compras:
            produtos.append(produto.to_dict())

        return {
            'nome': self.nome,
            'email': self.email,
            'compras': produtos
        }
        