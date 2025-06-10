class Produto:
    # a nota de avaliação deve ser um valor de 0 ate 5
    def __init__(self, id:int, nome:str, descricao:str, preco:float, nota_de_avaliacao:int):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.nota_de_avaliacao = nota_de_avaliacao
        assert 0 <= nota_de_avaliacao <= 5

    def __str__(self):
        return f'''
            Produto: \n
            id: {self.id}\n
            nome: {self.nome}\n 
            descrição: {self.descricao}\n 
            preço: {self.preco}\n 
            nota de avaliação: {self.nota_de_avaliacao}\n
        '''
        
    # retorna um dicionario representando o produto
    def to_dict(self) -> dict:

        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'nota_de_avaliacao': self.nota_de_avaliacao
        }