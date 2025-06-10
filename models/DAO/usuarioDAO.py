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
    
    def alterar_usuario(self):
        pass

    def delete_usuario(self, email:str):
        try:
            res = self.db.collection.delete_one({'email':email})
            if res.deleted_count == 1:
                print('Usuario excluido com sucesso!')
            else:
                print('Falha ao excluir o usuario, considere conferir o email inserido.')
        except Exception as e:
            print(e)
            return None