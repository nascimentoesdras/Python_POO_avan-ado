# Encapsulamento teoria

"""
    Encapusulamento consiste em proteger os estados internos de um objeto,
    controlando como seus atributos e métodos são acessados e modificados.

    O objetivo não é 'esconder' dados, mas sim garantir que o objeto permaneça consistente.

    imagine que você tem um objeto que representa uma conta bancária. Você não quer 
    que o saldo da conta seja alterado diretamente, pois isso poderia levar a inconsistências. 
    Em vez disso, você fornece métodos públicos para depositar e sacar dinheiro, 
    garantindo que todas as operações sejam válidas e mantendo o saldo correto.

"""

# Classe com atributos e métodos públicos.

class Conta:

    banco = "Banco Python"
    saldo = 0

    def __init__(self, titular:str):
        self.titular = titular

    def depositar(self, valor:float):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

cliente1 = Conta("Esdras Nascimento")

"""
cliente1.depositar(100)
cliente1.mostrar_saldo() #Saldo atualizado pelo método depositar
cliente1.saldo = 1000
cliente1.mostrar_saldo() #Saldo atualizado diretamente, compromentendo a consistência do objeto.
"""

# Esse tipo de possibilidade de alteração direta de um atributo ao método
# de uma classe pode levar a inconsistências e erros no programa e, por isso, são indesejadas.

# property -  encapsulamento verdadeiro de atributos e métodos.

class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome):
        if nome != "Esdras":
            raise ValueError("Nome não permitido.")
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self.__idade = idade

pessoa1 = Pessoa("Esdras", 30)

print(pessoa1.nome)
print(pessoa1.idade)

pessoa1.nome = "João"
print(pessoa1.nome)