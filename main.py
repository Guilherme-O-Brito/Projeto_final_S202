from db.database import Database
from models.DAO.usuarioDAO import UsuarioDAO
from models.cli.cli import StoreCLI

if __name__ == '__main__':
    user_db = Database(database='Projeto_final', collection='Users')

    usuarioDAO = UsuarioDAO(user_db)

    cli = StoreCLI('',usuarioDAO,'')

    cli.run()
    