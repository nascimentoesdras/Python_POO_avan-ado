# Revisão de POO

"""_summary_

    Uma classe segue um pipeline de execução, 
    onde o primeiro método a ser chamado é o __new__, 
    que é responsável por criar o objeto, 
    e em seguida o __init__, que é responsável por inicializar o objeto.

    embora o __new__ nem sempre apareça, na instanciação de um objeto, ele é chamado antes do __init__.

    __new__ recebe o parâmetro cls, 
    que é a classe que está sendo instanciada, e deve retornar uma instância da classe.

    

"""

"""class Pessoa:
    def __new__(cls):
        print('cirando um objeto')
        return super().__new__(cls)

    def __init__(self):
        print('Inicializando o objeto')"""

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


pessoa = Pessoa("Esdras", "Nascimento")

"""_summary_
    
    O dunder __dict__ é um atributo que retorna um dicionário com os atributos do objeto, 
    onde a chave é o nome do atributo e o valor é o valor do atributo.
"""

#pessoa.profissao = "Programador"

print(pessoa.__dict__)  # {'nome': 'Esdras', 'sobrenome': 'Nascimento'}