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


class LojaCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("vender", self.criarItem)
        self.add_command("buscarid", self.buscaID)
        self.add_command("buscarnome", self.buscaNome)
        self.add_command("buscartipo", self.buscaTipo)
        self.add_command("buscarmarca", self.buscaMarca)
        self.add_command("atualizarnome", self.atualizaNome)
        self.add_command("atualizarqnt", self.atualizaQnt)
        self.add_command("atualizarpreco", self.atualizaPreco)
        self.add_command("atualizardesc",self.atualizaDesc)
        self.add_command("apagar", self.apagaItem)

    def criarItem(self):
        item = input("Qual que é o nome do item: ")
        tipo = input("Insira o tipo deste item: ")
        desc = input("Coloque uma descrição sobre o produto: ")
        marca = input("Qual a marca do item: ")
        quantidade = int(input("Quantos itens vai vender(numeral): "))
        preco = float(input("Qual o valor disso: "))
        print("Tá caro ein")

        self.person_model.cria_item(item, tipo, marca, desc,  quantidade, preco)


    def buscaID(self):
        id = input("Coloque o id do item")
        self.person_model.busca_id(id)

    def buscaNome(self):
       nome = input("Coloque o nome do item")
       self.person_model.busca_nome(nome)

    def buscaTipo(self):
       tipo = input("Coloque o tipo do item")
       self.person_model.busca_tipo(tipo)

    def buscaMarca(self):
       marca = input("Coloque a marca do item")
       self.person_model.busca_marca(marca)


    def atualizaDesc(self):
        id = input("Coloque o id do item: ")
        desc = input("Insira uma nova descrição ai patrão: ")

    def atualizaQnt(self):
        id = input("Coloque o id do item: ")
        qnt = int(input("Qual a nova quantidade do item: "))
        self.person_model.atualiza_qnt(id, qnt)

    def atualizaNome(self):
        id = input("Coloque o id do item: ")
        name = input("Coloque o novo nome do item: ")
        self.person_model.atualiza_nome(id, name)
    
    def atualizaPreco(self):
        id = input("Coloque o id do item: ")
        preco = float(input("Coloque o novo preco do item: "))
        self.person_model.atualiza_preco(id, preco)

    def apagaItem(self):
        id = input("Coloca o id do item ai, faz favor: ")
        self.person_model.apaga_item(id)
        
    def run(self):
        print("Seja Bem vindo a Loja Baratão do Triginho")
        print("O que deseja fazer aqui gurí?")
        print("Quero colocar um item a venda(escreve 'vender'), Quero buscar um item sô(escreva 'buscarid, buscarnome, buscartipo ou buscarmarca' ai), Quero comprar um item(boa, escreve 'tigrin'), Quero atualiza um item rapa(escreve 'atualizar'), QUERO APAGA O ITEM DESGRAMA(Calma calabreso, escreve 'apagar'), Sò encher o saco memo(Sai então desnara, escreve 'sair')")
        super().run()
        