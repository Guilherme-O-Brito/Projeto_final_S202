from models.DAO.usuarioDAO import UsuarioDAO, Usuario
from models.DAO.vendedorDAO import VendedorDAO, Vendedor
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
    def __init__(self, vendedorDAO:VendedorDAO, usuarioDAO:UsuarioDAO):
        super().__init__()
        self.vendedorDAO = vendedorDAO
        self.usuarioDAO = usuarioDAO
        '''
            a função login devera requisitar ao usuario o email do usuario
            e então deve abrir para ele funções como listar anuncios, comprar algum item
            e por exemplo fazer algum filtro para buscas de produtos dos vendedores, ou então
            visualizar todas as suas compras ate então
        '''
        #self.add_command('login usuario', self.login_usuario)
        self.add_command('cadastrar usuario', self.cadastrar_usuario) # create
        self.add_command('listar usuarios', self.listar_usuarios) # read
        self.add_command('alterar usuario', self.update_usuario) # update
        self.add_command('excluir usuario', self.delete_usuario) # delete
        '''
            a função login devera requisitar ao usuario o email do vendedor
            e então deve abrir para ele funções como listar seus anuncios, editar algum item,
            criar um novo produto ou remover algum outro
        '''
        #self.add_command('login vendedor', self.login_vendedor)
        self.add_command('cadastrar vendedor', self.cadastrar_vendedor) # create
        self.add_command('listar vendedores', self.listar_vendedores) # read
        self.add_command('alterar vendedor', self.update_vendedor) # update
        self.add_command('excluir vendedor', self.delete_vendedor) # delete

    # USUARIO

    def cadastrar_usuario(self):
        nome = input('Digite o nome do novo usuario: ')
        email = input('Digite o email do novo usuario (este sera usado para diferenciar os usuarios): ')
        if self.usuarioDAO.check_email(email):
            print('Email ja cadastrado em outro usuario')
            return

        novo_usuario = Usuario(nome, email)

        self.usuarioDAO.create_usuario(novo_usuario)
        print('Usuario criado com sucesso!')

    def listar_usuarios(self):
        usuarios = self.usuarioDAO.listar_usuarios()
        print('Usuarios Cadastrados: ')
        for usuario in usuarios:
            print(usuario)

    def update_usuario(self):
        original_email = input('Entre com o email do usuario a ser alterado: ')
        if not self.usuarioDAO.check_email(original_email):
            print('Email não encontrado ou não cadastrado')
            return
        novo_nome = input('Digite o novo nome do usuario (caso não queira alterar apenas aperte ENTER):')
        novo_email = input('Digite o novo email do usuario (caso não queira alterar apenas aperte ENTER):')
        self.usuarioDAO.alterar_usuario(original_email, novo_nome, novo_email)
        

    def delete_usuario(self):
        email = input('Digite o email do usuario que sera removido: ')
        if not self.usuarioDAO.check_email(email):
            print('Email não encontrado ou não cadastrado')
            return 
        self.usuarioDAO.delete_usuario(email)
        print('Usuario excluido com sucesso!')
    
    # VENDEDOR

    def cadastrar_vendedor(self):
        nome = input('Digite o nome do novo vendedor: ')
        email = input('Digite o email do novo vendedor (este sera usado para diferenciar os vendedores): ')
        descricao = input('Digite a descrição da loja deste vendedor: ')
        pais_de_origem = input('Digite o pais de origem deste vendedor: ')
        if self.vendedorDAO.check_email(email):
            print('Email ja cadastrado em outro vendedor')
            return

        novo_vendedor = Vendedor(nome, email, descricao, pais_de_origem)

        self.vendedorDAO.create_vendedor(novo_vendedor)
        print('Vendedor criado com sucesso!')

    def listar_vendedores(self):
        vendedores = self.vendedorDAO.listar_vendedores()
        print('Vendedores Cadastrados: ')
        for vendedor in vendedores:
            print(vendedor)

    def update_vendedor(self):
        original_email = input('Entre com o email do vendedor a ser alterado: ')
        if not self.vendedorDAO.check_email(original_email):
            print('Email não encontrado ou não cadastrado')
            return
        novo_nome = input('Digite o novo nome do vendedor (caso não queira alterar apenas aperte ENTER): ')
        novo_email = input('Digite o novo email do vendedor (caso não queira alterar apenas aperte ENTER): ')
        nova_descricao = input('Digite a nova descrição do vendedor (caso não queira alterar apenas aperte ENTER): ')
        novo_pais_de_origem = input('Digite o novo pais de origem do vendedor (caso não queira alterar apenas aperte ENTER):')
        self.vendedorDAO.alterar_vendedor(original_email, novo_nome, novo_email, nova_descricao, novo_pais_de_origem)
        

    def delete_vendedor(self):
        email = input('Digite o email do vendedor que sera removido: ')
        if not self.vendedorDAO.check_email(email):
            print('Email não encontrado ou não cadastrado')
            return
        
        self.vendedorDAO.delete_vendedor(email)
        print('Vendedor excluido com sucesso!')

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