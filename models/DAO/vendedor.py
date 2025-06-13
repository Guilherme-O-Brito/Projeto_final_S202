class Vendedor:
    def __init__(self, nome:str, email:str, descricao:str, pais_de_origem:str, produtos=[]):
        self.nome = nome
        self.email = email
        self.descricao = descricao
        self.pais_de_origem = pais_de_origem
        self.produtos = produtos
    
    def __str__(self):
        return f'Vendedor: \n{self.nome} do {self.pais_de_origem} email: {self.email} \n {self.descricao}'
    
    # retorna um dicionario representando o usuario
    def to_dict(self) -> dict:

        produtos = []
        for produto in self.produtos:
            produtos.append(produto.to_dict())

        return {
            'nome': self.nome,
            'email': self.email,
            'descricao': self.descricao,
            'produtos': produtos,
            'pais_de_origem': self.pais_de_origem
        }