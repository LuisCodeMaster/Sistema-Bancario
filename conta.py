class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        self.extrato.append(f"Depósito: +{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        self.extrato.append(f"Saque: -{valor}")

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
        self.extrato.append(f"Transferência para {destino.numero}: -{valor}")
        destino.extrato.append(f"Transferência recebida de {self.numero}: +{valor}")

    def exibir_extrato(self):
        return "\n".join(self.extrato)

    def to_dict(self):
        return {
            "numero": self.numero,
            "titular": self.titular,
            "saldo": self.saldo,
            "extrato": self.extrato
        }

    @staticmethod
    def from_dict(data):
        conta = Conta(data["numero"], data["titular"])
        conta.saldo = data.get("saldo", 0)  
        conta.extrato = data.get("extrato", [])  
        return conta

    def __str__(self):
        return f"Número: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}"
