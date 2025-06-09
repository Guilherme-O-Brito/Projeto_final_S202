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
