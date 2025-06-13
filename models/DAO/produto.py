class Produto:
    # a nota de avaliação deve ser um valor de 0 ate 5
    def __init__(self, id:int, nome:str, descricao:str, preco:float, nota_de_avaliacao:int, quantidade:int):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.nota_de_avaliacao = nota_de_avaliacao
        self.quantidade = quantidade
        assert 0 <= nota_de_avaliacao <= 5

    def __str__(self):
        return f'''
            Produto: 
            id: {self.id}
            nome: {self.nome}
            descrição: {self.descricao}
            preço: {self.preco}
            nota de avaliação: {self.nota_de_avaliacao}
            quantidade: {self.quantidade}
        '''
        
    # retorna um dicionario representando o produto
    def to_dict(self) -> dict:

        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'nota_de_avaliacao': self.nota_de_avaliacao,
            'quantidade': self.quantidade
        }
    def to_dict_compra(self,qnt) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'nota_de_avaliacao': self.nota_de_avaliacao,
            'quantidade': qnt
        }