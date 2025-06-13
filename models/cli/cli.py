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
            command = input("Coloque o q se quer:  ")
            if command == "sair":
                print("Obrigado, o Baratão do Triginho está sempre ao nosso dispor")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Escreveu errado, escreve certo agora")

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
        self.add_command('cadastrar vendedor', self.cadastrar_vendedor) # create
        self.add_command('listar vendedores', self.listar_vendedores) # read
        self.add_command('alterar vendedor', self.update_vendedor) # update
        self.add_command('excluir vendedor', self.delete_vendedor) # delete

    # USUARIO

    def login_usuario(self):
        email = input('Digite o seu email de usuario: ')
        usuario = self.usuarioDAO.get_user_by_email(email)
        if not usuario:
            print('Usuario não encontrado')
            return
        userCLI = UserCLI(self.usuarioDAO, self.vendedorDAO, usuario)
        userCLI.run()

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

    def login_vendedor(self):
        email = input('Digite o seu email de vendedor: ')
        vendedor = self.vendedorDAO.get_seller_by_email(email)
        if not vendedor:
            print('Vendedor não encontrado')
            return
        sellerCLI = SellerCLI(self.vendedorDAO, vendedor)
        sellerCLI.run()

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
        print('Vendedor alterado com sucesso!')
        

    def delete_vendedor(self):
        email = input('Digite o email do vendedor que sera removido: ')
        if not self.vendedorDAO.check_email(email):
            print('Email não encontrado ou não cadastrado')
            return
        
        self.vendedorDAO.delete_vendedor(email)
        print('Vendedor excluido com sucesso!')

class UserCLI(SimpleCLI):
    def __init__(self, usuarioDAO:UsuarioDAO, vendedorDAO:VendedorDAO, usuario:Usuario):
        super().__init__()
        self.usuarioDAO = usuarioDAO
        self.vendedorDAO = vendedorDAO
        self.usuario = usuario
        
        self.add_command('buscar produto', self.buscar_produto) # buscar produtos pelo nome
        self.add_command('melhores produtos', self.melhores_produtos) # mostra todos os produtos disponiveis para compra de todos os vendedores organizados por nota
        self.add_command('comprar produto', self.comprar_produto) # comprar produto pelo id
        self.add_command('listar compras', self.listar_compras) # lista todas as compras do usuario
    
    def run(self):
        print(f'Conectado como: {self.usuario} ao sistema de Usuarios')
        print("Seja Bem vindo a Loja Baratão do Triginho")
        print("O que deseja fazer aqui gurí?")
        print('Caso queira sair deste usuario digite "sair"')
        super().run()
        print(f'Desconectando de {self.usuario}')

    def buscar_produto(self):
        key_word = input('Digite o nome ou palavra que deseja buscar: ')
        vendedores = self.vendedorDAO.buscar_produto(key_word)
        print('Produtos encontrados: ')
        for vendedor, produtos in vendedores.items():
            for produto in produtos:
                print(f'Vendedor: {vendedor}')
                print(produto)
    
    def melhores_produtos(self):
        produtos = self.vendedorDAO.melhores_produtos()
        print('Produtos ordenados por nota de avaliação:')
        for produto in produtos:
            print(produto)
        
    def comprar_produto(self):
        produto = self.vendedorDAO.buscar_produto_por_id(int(input('Digite o id do produto que deseja comprar: ')))

        if produto == None:
            print('Produto não encontrado')
            return 

        if self.usuarioDAO.registrar_compra(produto, self.usuario):
            print('Compra registrada com sucesso!')
        else:
            print('Não foi possivel realizar a compra')

    def listar_compras(self):
        produtos = self.usuarioDAO.listar_compras(self.usuario)
        
        print(f'Compras de {self.usuario}: ')
        for produto in produtos:
            print(produto)
            

class SellerCLI(SimpleCLI):
    def __init__(self, vendedorDAO:VendedorDAO, vendedor:Vendedor):
        super().__init__()
        self.vendedorDAO = vendedorDAO
        self.vendedor = vendedor

        self.add_command('cadastrar produto', self.cadastrar_produto)
        self.add_command('alterar produto', self.alterar_produto)
        self.add_command('listar produtos', self.listar_produtos)
        self.add_command('excluir produto', self.excluir_produto)
    
    def run(self):
        print(f'Conectado como: {self.vendedor} ao sistema de Vendedores')
        print("Seja Bem vindo a Loja Baratão do Triginho")
        print("O que deseja fazer aqui gurí?")
        print('Caso queira sair deste vendedor digite "sair"')
        super().run()
        print(f'Desconectando de {self.vendedor}')

    def cadastrar_produto(self):
        produto = Produto(
            id=self.vendedorDAO.get_next_id(),
            nome=input('Insira o nome do produto: '),
            descricao=input('Insira a descrição do produto: '),
            preco=float(input('Insira o preço do produto: ')),
            nota_de_avaliacao=int(input('Insira a nota de valiação (apenas inteiros):'))
        )

        if produto.preco > 10:
            print("Tá caro ein")

        if self.vendedorDAO.cadastrar_produto(produto, self.vendedor):
            print('Produto cadastrado com sucesso!')
        else:
            print('Não foi possivel cadastrar o produto!')

    def alterar_produto(self):
        id = int(input('Entre com o id do produto que deseja alterar: '))
        novo_nome = input('Digite o novo nome do produto (caso não queira alterar apenas aperte ENTER): ')
        nova_descricao = input('Digite a nova descrição do produto (caso não queira alterar apenas aperte ENTER): ')
        novo_preco = input('Digite o novo preço do produto (caso não queira alterar apenas aperte ENTER): ')
        nova_nota = input('Digite a nova nota do produto (caso não queira alterar apenas aperte ENTER):')
        
        if self.vendedorDAO.alterar_produto(id, novo_nome, nova_descricao, novo_preco, nova_nota, self.vendedor):
            print('Produto alterado com sucesso!')
        else:
            print('Não foi possivel alterar o produto!')

    def listar_produtos(self):
        produtos = self.vendedorDAO.listar_produtos(self.vendedor)
        
        print(f'Produtos de {self.vendedor}: ')
        for produto in produtos:
            print(produto)

    def excluir_produto(self):
        if self.vendedorDAO.excluir_produto(int(input('Digite o id do produto que deseja excluir: ')), self.vendedor):
            print('Produto excluido com sucesso!')
        else:
            print('Não foi possivel excluir o projeto!')

    