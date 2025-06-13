from models.DAO.vendedor import Vendedor
from models.DAO.produto import Produto
from db.database import Database
from bson.objectid import ObjectId

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
                        nota_de_avaliacao=produto['nota_de_avaliacao'],
                        quantidade = produto['quantidade']
                    ))
                vendedores.append(Vendedor(res['nome'], res['email'], res['descricao'], res['pais_de_origem'], produtos))

            return vendedores
        except Exception as e:
            print(e)
            return None
    
    def alterar_vendedor(self, email:str, novo_nome:str, novo_email:str, nova_descricao:str, novo_pais_de_origem:str):
        try:
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
        
        except Exception as e:
            print(e)

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
        
    # retorna o objeto do vendedor correspondente ao email inserido
    def get_seller_by_email(self, email:str):
        try:
            if not self.check_email(email):
                return False
            seller = self.db.collection.find_one({'email':email})
            produtos = []
            for produto in seller['produtos']:
                produtos.append(Produto(
                    id=produto['id'],
                    nome=produto['nome'],
                    descricao=produto['descricao'],
                    preco=produto['preco'],
                    nota_de_avaliacao=produto['nota_de_avaliacao'],
                    quantidade= produto['quantidade']
                ))
            return Vendedor(
                nome=seller['nome'],
                email=seller['email'],
                descricao=seller['descricao'],
                pais_de_origem=seller['pais_de_origem'],
                produtos=produtos
            )
        except Exception as e:
            print(e)
            return False
        
    def buscar_produto(self, keyword:str, vendedor_id:str):
        try:
            responses = self.db.collection.aggregate([
                # explode o vetor de produtos no documento de vendedores
                {'$unwind':'$produtos'},
                # procura pela keyword no nome dos produtos e encontra o ou os que possuem essa palavra
                {'$match': {'_id': ObjectId(vendedor_id),
                    'produtos.nome': {'$regex': keyword, '$options':'i'}
                }},
                # agrupa os produtos separados por seu respectivo vendedor
                {
                    '$group': {
                        '_id':'$nome',
                        'produtos':{'$push':'$produtos'}
                    }
                },
                
            ])
            
            vendedores = {}
            for seller in responses:
                produtos = []
                for produto in seller['produtos']:
                    produtos.append(
                        Produto(
                            produto['id'],
                            produto['nome'],
                            produto['descricao'],
                            produto['preco'],
                            produto['nota_de_avaliacao'],
                            produto['quantidade']
                        ) 
                    )
                vendedores[seller['_id']] = produtos.copy()
            
            return vendedores
                
        except Exception as e:
            print(e)
            return None
        
    def melhores_produtos(self):
        try:
            responses = self.db.collection.aggregate([
                # explode o vetor de produtos no documento de vendedores
                {'$unwind':'$produtos'},
                # transforma os documentos dentro da lista produtos na raiz
                {'$replaceRoot': {'newRoot':'$produtos'}},
                # organiza os produtos por nota de avaliação
                {'$sort': {'nota_de_avaliacao':-1}}
            ])
            produtos = []
            for produto in responses:
                produtos.append(
                        Produto(
                            produto['id'],
                            produto['nome'],
                            produto['descricao'],
                            produto['preco'],
                            produto['nota_de_avaliacao'],
                            produto['quantidade']
                        ) 
                    )

            return produtos

        except Exception as e:
            print(e)
            return None
    
    def buscar_produto_por_id(self, id:int, vendedor_id:str):
        try:
            produto = self.db.collection.find_one({'_id': ObjectId(vendedor_id),'produtos.id': id},{'produtos.$': 1})
            if produto != None:
                produto = produto['produtos'][0] 
                return Produto(
                    produto['id'],
                    produto['nome'],
                    produto['descricao'],
                    produto['preco'],
                    produto['nota_de_avaliacao'],
                    produto['quantidade']
                )
            return produto
        
        except Exception as e:
            print(e)
            return None
        
    def listar_produtos(self, vendedor:Vendedor):
        try: 
            responses = self.db.collection.aggregate([
                # filtra pelo vendedor logado
                {'$match': {'email':vendedor.email}},
                # explode o vetor de produtos no documento de usuarios
                {'$unwind':'$produtos'},
                # transforma os documentos dentro da lista produtos na raiz
                {'$replaceRoot': {'newRoot':'$produtos'}},
                # organiza os produtos por id
                {'$sort': {'id':1}}
            ])
            
            produtos = []
            for produto in responses:
                produtos.append(Produto(
                    id=produto['id'],
                    nome=produto['nome'],
                    descricao=produto['descricao'],
                    preco=produto['preco'],
                    nota_de_avaliacao=produto['nota_de_avaliacao']
                ))

            return produtos

        except Exception as e:
            print(e)
            return None
    
    # retorna o proximo id disponivel para cadastro de produtos
    def get_next_id(self):
        max_id = list(self.db.collection.aggregate([
            {'$unwind':'$produtos'},
            {'$group': {
                '_id': None,
                'id': {'$max':'$produtos.id'}
            }}
        ]))
        
        maior_id = int(max_id[0]['id']) + 1 if max_id else 0

        return maior_id
    
    def cadastrar_produto(self, produto:Produto, vendedor:Vendedor):
        try: 
            res = self.db.collection.update_one(
                {'email':vendedor.email}, 
                {'$push': {'produtos':produto.to_dict()}}
            )

            if res.modified_count == 0:
                return False

            return True
        except Exception as e:
            print(e)
            return False
    
    def alterar_Qnt_Por_compra(self,vendedor_id:str, id:str, qnt:int):
        try:
            res = self.db.collection.find_one(
            {
            "_id": ObjectId(vendedor_id),
            "produtos.id": id
            },
            {
            "produtos.$": 1  # retorna só o produto correspondente
            })
            quantidade_atual = res["produtos"][0]["quantidade"]
        
            if quantidade_atual is not None and quantidade_atual > 0:
                self.db.collection.update_one(
                {
                    "_id": ObjectId(vendedor_id),
                    "produtos.id": id
                },
                {
                    "$inc": {"produtos.$.quantidade": -qnt}
                }
            )
            print("Quantidade atualizada com sucesso!")
        except Exception as e:
            print(f"Deu pra compra não chefia, deu erro{e}")
            return None

    def alterar_produto(self, id:int, novo_nome:str, nova_descricao:str, novo_preco:str, nova_nota:str, nova_qnt:str, vendedor:Vendedor):
        try:
            produto = self.db.collection.find_one({'produtos.id': id},{'produtos.$': 1})
            if produto == None:
                return False
            produto = produto['produtos'][0]
            res = self.db.collection.update_one(
                {
                    'email':vendedor.email,
                    'produtos.id':id
                },
                {
                    '$set': {
                        'produtos.$.nome': novo_nome if novo_nome != '' else produto['nome'],
                        'produtos.$.descricao': nova_descricao if nova_descricao != '' else produto['descricao'],
                        'produtos.$.preco': float(novo_preco) if novo_preco != '' else produto['preco'],
                        'produtos.$.nota_de_avaliacao': int(nova_nota) if nova_nota != '' else produto['nota_de_avaliacao'],
                        'produtos.$.quantidade':int(nova_qnt) if nova_qnt != '' else produto['quantidade']
                    }
                }
            )

            if res.modified_count == 0:
                return False

            return True
        except Exception as e:
            print(e)
            return False

    def excluir_produto(self, id:int, vendedor:Vendedor):
        try:
            res = self.db.collection.update_one(
                {'email':vendedor.email},
                {'$pull': {'produtos':{'id':id}}}
            )

            if res.modified_count == 0:
                return False

            return True
        except Exception as e:
            print(e)
            return False