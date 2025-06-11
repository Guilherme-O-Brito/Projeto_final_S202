from models.DAO.vendedor import Vendedor
from models.DAO.produto import Produto
from db.database import Database

class VendedorDAO:
    def __init__(self, database:Database):
        self.db = database

    def create_vendedor(self, vendedor:Vendedor):
        try:
            res = self.db.collection.insert_one(vendedor.to_dict())
            return res
        except Exception as e:
            print(e)
            return None
    
    def listar_vendedores(self):
        try:
            vendedores = []
            responses = self.db.collection.find()

            for res in responses:
                produtos = []
                for produto in res['produtos']:
                    produtos.append(Produto(
                        id=produto['id'],
                        nome=produto['nome'],
                        descricao=produto['descricao'],
                        preco=produto['preco'],
                        nota_de_avaliacao=produto['nota_de_avaliacao']
                    ))
                vendedores.append(Vendedor(res['nome'], res['email'], res['descricao'], res['pais_de_origem'], produtos))

            return vendedores
        except Exception as e:
            print(e)
            return None
    
    def alterar_vendedor(self, email:str, novo_nome:str, novo_email:str, nova_descricao:str, novo_pais_de_origem:str):
        vendedor = self.db.collection.find_one({'email':email})
        self.db.collection.update_one(
                {'email':email}, 
                {'$set':
                    {
                        'nome':novo_nome if novo_nome != '' else vendedor['nome'], 
                        'email':novo_email if novo_email != '' else vendedor['email'],
                        'descricao':nova_descricao if nova_descricao != '' else vendedor['descricao'],
                        'pais_de_origem':novo_pais_de_origem if novo_pais_de_origem != '' else vendedor['pais_de_origem'],
                    }
                }
            )
        print('Vendedor alterado com sucesso!')

    def delete_vendedor(self, email:str):
        try:
            self.db.collection.delete_one({'email':email})
        except Exception as e:
            print(e)
            return None
        
    def check_email(self, email:str) -> bool:
        try:
            res = self.db.collection.find_one({'email':email})
            if res == None:
                return False
            return True
        except Exception as e:
            print(e)
            return False
        
    