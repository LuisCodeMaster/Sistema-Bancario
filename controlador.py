from banco import Banco
from conta import Conta

class ControladorBanco:
    def __init__(self):
        self.banco = Banco()

    def exibir_menu(self):
        while True:
            print("\n--- Menu do Banco ---")
            print("1. Criar Conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferir")
            print("5. Exibir Contas")
            print("6. Extrato")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_conta()
            elif opcao == "2":
                self.depositar()
            elif opcao == "3":
                self.sacar()
            elif opcao == "4":
                self.transferir()
            elif opcao == "5":
                self.exibir_contas()
            elif opcao == "6":
                self.exibir_extrato()
            elif opcao == "7":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def criar_conta(self):
        numero = input("Número da conta: ")
        
        
        if not numero.strip():
            print("Número da conta não pode ser vazio.")
            return

        
        if any(conta.numero == numero for conta in self.banco.contas):
            print(f"Erro: Já existe uma conta com o número {numero}.")
            return

        titular = input("Nome do titular: ")
        
       
        if not titular.strip():
            print("O nome do titular não pode ser vazio.")
            return

        conta = Conta(numero, titular)
        self.banco.adicionar_conta(conta)
        print(f"Conta criada com sucesso! {conta}")

    def depositar(self):
        numero = input("Número da conta: ")
        conta = self.banco.buscar_conta(numero)
        if conta:
            try:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
                print(f"Depósito realizado com sucesso! Novo saldo: {conta.saldo}")
            except ValueError:
                print("Valor inválido para depósito.")
        else:
            print(f"Conta {numero} não encontrada.")

    def sacar(self):
        numero = input("Número da conta: ")
        conta = self.banco.buscar_conta(numero)
        if conta:
            try:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
                print(f"Saque realizado com sucesso! Novo saldo: {conta.saldo}")
            except ValueError as e:
                print(f"Erro: {e}")
        else:
            print(f"Conta {numero} não encontrada.")

    def transferir(self):
        numero_origem = input("Número da conta de origem: ")
        conta_origem = self.banco.buscar_conta(numero_origem)
        if conta_origem:
            numero_destino = input("Número da conta de destino: ")
            conta_destino = self.banco.buscar_conta(numero_destino)
            if conta_destino:
                try:
                    valor = float(input("Valor da transferência: "))
                    conta_origem.transferir(conta_destino, valor)
                    print(f"Transferência realizada com sucesso! Novo saldo da conta de origem: {conta_origem.saldo}")
                    print(f"Novo saldo da conta de destino: {conta_destino.saldo}")
                except ValueError as e:
                    print(f"Erro: {e}")
            else:
                print(f"Conta de destino {numero_destino} não encontrada.")
        else:
            print(f"Conta de origem {numero_origem} não encontrada.")

    def exibir_contas(self):
        if not self.banco.contas:
            print("Não há contas registradas.")
        else:
            for conta in self.banco.contas:
                print(conta)

    def exibir_extrato(self):
        numero = input("Número da conta: ")
        conta = self.banco.buscar_conta(numero)
        if conta:
            print("\n--- Extrato ---")
            print(conta.exibir_extrato())
        else:
            print(f"Conta {numero} não encontrada.")
