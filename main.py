from db.database import Database
from models.DAO.usuarioDAO import UsuarioDAO
from models.DAO.vendedorDAO import VendedorDAO
from models.cli.cli import StoreCLI

if __name__ == '__main__':
    user_db = Database(database='Projeto_final', collection='Users')
    seller_db = Database(database='Projeto_final', collection='Sellers')

    usuarioDAO = UsuarioDAO(user_db)
    vendedorDAO = VendedorDAO(seller_db)

    cli = StoreCLI(vendedorDAO,usuarioDAO,)

    cli.run()
    