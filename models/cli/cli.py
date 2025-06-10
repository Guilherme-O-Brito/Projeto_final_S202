from models.DAO.usuarioDAO import UsuarioDAO, Usuario
from models.DAO.produto import Produto

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Encerrando!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando Invalido!")

class StoreCLI(SimpleCLI):
    def __init__(self, vendedorDAO, usuarioDAO:UsuarioDAO, produtoDAO):
        super().__init__()
        self.vendedorDAO = vendedorDAO
        self.usuarioDAO = usuarioDAO
        self.produtoDAO = produtoDAO
        '''
            a função login devera requisitar ao usuario o email do usuario
            e então deve abrir para ele funções como listar anuncios, comprar algum item
            e por exemplo fazer algum filtro para buscas de produtos dos vendedores, ou então
            visualizar todas as suas compras ate então
        '''
        #self.add_command('login usuario', self.login_usuario)
        self.add_command('cadastrar usuario', self.cadastrar_usuario) # create
        self.add_command('listar usuarios', self.listar_usuarios) # read
        #self.add_command('alterar usuario', self.update_usuario) # update
        self.add_command('excluir usuario', self.delete_usuario) # delete
        '''
            a função login devera requisitar ao usuario o email do vendedor
            e então deve abrir para ele funções como listar seus anuncios, editar algum item,
            criar um novo produto ou remover algum outro
        '''
        #self.add_command('login vendedor', self.login_vendedor)
        #self.add_command('cadastrar vendedor', self.create_vendedor) # create
        #self.add_command('listar vendedores', self.listar_usuarios) # read
        #self.add_command('alterar vendedor', self.update_usuario) # update
        #self.add_command('excluir vendedor', self.delete_usuario) # delete

    def cadastrar_usuario(self):
        novo_usuario = Usuario(
            nome=input('Digite o nome do novo usuario: '),
            email=input('Digite o email do novo usuario (este sera usado para diferenciar os usuarios): '),
        )

        self.usuarioDAO.create_usuario(novo_usuario)
        print('Usuario criado com sucesso!')

    def listar_usuarios(self):
        usuarios = self.usuarioDAO.listar_usuarios()
        print('Usuarios Cadastrados: ')
        for usuario in usuarios:
            print(usuario)

    def delete_usuario(self):
        self.usuarioDAO.delete_usuario(input('Digite o email do usuario que sera removido: '))
    
    
    '''
        compras=[
                Produto(
                    1,
                    'Drone DJI MAVIC PRO',
                    'Drone de controle remoto profissional com camera 4K',
                    10000,
                    5
                ),
                Produto(
                    2,
                    'Chaveiro do Omen Valorant',
                    'Chaveiro de colecionador do Valorant',
                    7.5,
                    3
                ),
                Produto(
                    3,
                    'Pendrive 2TB',
                    'Pendrive com 2TB de armazenamento',
                    55.67,
                    2
                )
            ]
    '''