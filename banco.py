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

    def salvar_contas(self):from conta import Conta
import json

class Banco:
    def __init__(self):
        self.contas = []
        self.carregar_contas()

    def carregar_contas(self):
        try:
            with open("contas.json", "r") as f:
                contas_data = json.load(f)
                self.contas = [Conta.from_dict(conta) for conta in contas_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contas = []

    def salvar_contas(self):
        with open("contas.json", "w") as f:
            json.dump([conta.to_dict() for conta in self.contas], f, indent=4)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        self.salvar_contas()

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

        contas_data = [conta.to_dict() for conta in self.contas]
        with open('contas.json', 'w') as file:
            json.dump(contas_data, file, indent=4)

    def criar_conta(self, numero, titular):
        conta = Conta(numero, titular)
        self.contas.append(conta)
        self.salvar_contas()
        return conta

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
