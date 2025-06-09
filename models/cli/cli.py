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

class ShopeeCLI(SimpleCLI):
    def __init__(self, vendedorDAO, usuarioDAO):
        super().__init__()
        self.vendedorDAO = vendedorDAO
        self.usuarioDAO = usuarioDAO
        '''
            a função login devera requisitar ao usuario o email do usuario
            e então deve abrir para ele funções como listar anuncios, comprar algum item
            e por exemplo fazer algum filtro para buscas de produtos dos vendedores, ou então
            visualizar todas as suas compras ate então
        '''
        self.add_command('login usuario', self.login_usuario)
        self.add_command('cadastrar usuario', self.cadastrar_usuario) # create
        self.add_command('listar usuarios', self.listar_usuarios) # read
        self.add_command('alterar usuario', self.update_usuario) # update
        self.add_command('excluir usuario', self.delete_usuario) # delete
        '''
            a função login devera requisitar ao usuario o email do vendedor
            e então deve abrir para ele funções como listar seus anuncios, editar algum item,
            criar um novo produto ou remover algum outro
        '''
        self.add_command('login vendedor', self.login_vendedor)
        self.add_command('cadastrar vendedor', self.create_vendedor) # create
        self.add_command('listar vendedores', self.listar_usuarios) # read
        self.add_command('alterar vendedor', self.update_usuario) # update
        self.add_command('excluir vendedor', self.delete_usuario) # delete