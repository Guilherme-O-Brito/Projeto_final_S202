from db.database import Database
from models.DAO.usuarioDAO import UsuarioDAO
from models.DAO.vendedorDAO import VendedorDAO
from models.cli.cli import StoreCLI

if __name__ == '__main__':
    # Conexão a collection de usuarios
    user_db = Database(database='Projeto_final', collection='Users')
    # Conexão a collection de vendedores
    seller_db = Database(database='Projeto_final', collection='Sellers')

    usuarioDAO = UsuarioDAO(user_db)
    vendedorDAO = VendedorDAO(seller_db)

    cli = StoreCLI(vendedorDAO,usuarioDAO,)

    cli.run()
    