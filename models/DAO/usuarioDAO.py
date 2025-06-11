from models.DAO.usuario import Usuario
from models.DAO.produto import Produto
from db.database import Database

class UsuarioDAO:
    def __init__(self, database:Database):
        self.db = database

    def create_usuario(self, usuario:Usuario):
        try:
            res = self.db.collection.insert_one(usuario.to_dict())
            return res
        except Exception as e:
            print(e)
            return None
        
    def listar_usuarios(self):
        try:
            usuarios = []
            responses = self.db.collection.find()

            for res in responses:
                compras = []
                for produto in res['compras']:
                    compras.append(Produto(
                        id=produto['id'],
                        nome=produto['nome'],
                        descricao=produto['descricao'],
                        preco=produto['preco'],
                        nota_de_avaliacao=produto['nota_de_avaliacao']
                    ))
                usuarios.append(Usuario(res['nome'], res['email'], compras))

            return usuarios
        except Exception as e:
            print(e)
            return None
    
    def alterar_usuario(self, email:str, novo_nome:str, novo_email:str):
        usuario = self.db.collection.find_one({'email':email})
        self.db.collection.update_one(
                {'email':email}, 
                {'$set':
                    {
                        'nome':novo_nome if novo_nome != '' else usuario['nome'], 
                        'email':novo_email if novo_email != '' else usuario['email']
                    }
                }
            )
        print('Usuario alterado com sucesso!')
    def delete_usuario(self, email:str):
        try:
            res = self.db.collection.delete_one({'email':email})
            print('Usuario excluido com sucesso!')
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