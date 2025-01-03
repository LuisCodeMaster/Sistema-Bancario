Sistema Bancário
Este é um sistema bancário simples desenvolvido em Python, utilizando Orientação a Objetos (OO). O sistema permite criar contas bancárias, realizar depósitos, saques, transferências e consultar extratos. As contas são armazenadas em um arquivo JSON para persistência de dados.

Funcionalidades
Criar Conta Bancária: Permite a criação de uma nova conta com número e titular.
Depositar: Realiza depósitos em uma conta bancária.
Sacar: Permite o saque de valores de uma conta bancária.
Transferir: Realiza transferências entre contas bancárias.
Exibir Extrato: Exibe o extrato de uma conta bancária, com todas as transações realizadas.

Arquivos do Projeto
main.py: Arquivo principal que executa o sistema e interage com o usuário, exibindo o menu de opções e chamando as funcionalidades do banco.
banco.py: Contém a classe Banco, responsável por gerenciar a lista de contas e realizar operações de persistência (salvar e carregar contas de um arquivo JSON).
conta.py: Define a classe Conta, que representa uma conta bancária e possui métodos para manipulação das transações financeiras (depósitos, saques, transferências).
controlador.py: Contém a classe ControladorBanco, que gerencia a interação com o usuário, fornecendo o menu e executando as operações com as contas.
contas.json: Arquivo que armazena os dados das contas bancárias em formato JSON para persistência.


Conceitos de Orientação a Objetos Utilizados

Encapsulamento
O encapsulamento é utilizado para garantir que os dados internos das classes, como o saldo da conta, sejam acessados e modificados apenas por meio de métodos específicos. Por exemplo, a classe Conta possui métodos como depositar() e sacar() para garantir a integridade do saldo.

Exemplo:

O saldo da conta é manipulado apenas pelos métodos depositar() e sacar(), evitando alterações diretas e indevidas.

Abstração
A abstração permite que o usuário interaja com o sistema bancário sem precisar entender todos os detalhes internos. O menu interativo fornece uma interface simples e amigável, enquanto os métodos internos realizam operações complexas, como a validação de dados e a persistência.

Exemplo:

O método transferir() realiza toda a lógica de transferência entre contas, mas o usuário não precisa saber como essa operação é implementada.

Modularidade
O código está dividido em várias classes, cada uma com responsabilidades específicas, o que facilita a manutenção e extensão do sistema. A classe Banco cuida da persistência das contas, enquanto a classe Conta gerencia as transações bancárias de cada conta.

Exemplo:

A classe Banco é responsável por carregar e salvar os dados das contas no arquivo JSON, enquanto a classe Conta manipula o saldo e as transações da conta.
