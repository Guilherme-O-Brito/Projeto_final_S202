from pymongo import MongoClient
from bson.objectid import ObjectId

class produtos:
    def __init__(self, database):
        self.db = database

    def cria_item(self, nome:str, tipo:str,desc:str, marca:str, quantidade:int, preco:float):
        try:
            res = self.db.collection.insert_one({"nome":nome,"tipo":tipo,"desc":desc, "marca":marca,"quantidade":quantidade, "preco": preco})
            print(f"Item criado no catalogo. O Id é esse: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Uai, deu erro criando o item na loja: {e}")
            return None

    def busca_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": id})
            print(f"Achamo o item: {res}")
            return res
        except Exception as e:
            print(f"Uai, deu erro procurando o item na loja: {e}")
            return None
    
    def busca_nome(self, nome: str):
        try:
            res = self.db.collection.find_one({"nome": {"$regex": nome, "$options": "i" }})
            print(f"Achamo o item: {res}")
            return res
        except Exception as e:
            print(f"Uai, deu erro procurando o item na loja: {e}")
            return None
        
    def busca_tipo(self, tipo: str):
        try:
            res = self.db.collection.find_one({"tipo": {"$regex": tipo, "$options": "i" }})
            print(f"Achamo o item: {res}")
            return res
        except Exception as e:
            print(f"Uai, deu erro procurando o item na loja: {e}")
            return None
        
    def busca_marca(self, marca: str):
        try:
            res = self.db.collection.find_one({"marca": {"$regex": marca, "$options": "i" }})
            print(f"Achamo o item: {res}")
            return res
        except Exception as e:
            print(f"Uai, deu erro procurando o item na loja: {e}")
            return None

    def atualiza_desc(self, id: str, desc:str):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {"descricao": desc}})
            print("Alterado a descrição do item meu chefe")
            return res.modified_count
        except Exception as e:
            print(f"Deu pra muda nao chefia")
            return None

    def atualiza_nome(self, id: str, nome:str):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {"nome": nome}})
            print("Alterado o nome do item meu chefe")
            return res.modified_count
        except Exception as e:
            print(f"Deu pra muda nao chefia")
            return None

    def atualiza_preco(self, id: str, preco:float):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": { "preco": preco}})
            print(f"Alterado o preco do item meu chefe")
            return res.modified_count
        except Exception as e:
            print(f"Deu pra muda nao chefia")
            return None
        
    def atualiza_qnt(self, id: str, qnt:float):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": { "quantidade": qnt}})
            print(f"Alterada a quantidade do item meu chefe")
            return res.modified_count
        except Exception as e:
            print(f"Deu pra muda nao chefia")
            return None
        

    def apaga_item(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": id})
            print("Item deletado meu patrão")
            return res.deleted_count
        except Exception as e:
            print(f"Deu pra apaga não KKKKKKK")
            return None