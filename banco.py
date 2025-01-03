import json
from conta import Conta

class Banco:
    def __init__(self):
        self.contas = []
        self.carregar_contas()

    def carregar_contas(self):
        try:
            with open('contas.json', 'r') as file:
                contas_data = json.load(file)
                self.contas = [Conta.from_dict(conta) for conta in contas_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contas = []

    def salvar_contas(self):
        with open('contas.json', 'w') as file:
            json.dump([conta.to_dict() for conta in self.contas], file, indent=4)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        self.salvar_contas()

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def criar_conta(self, numero, titular):
        conta = Conta(numero, titular)
        self.adicionar_conta(conta)
        return conta
