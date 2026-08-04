
class Produto:

    def __new__(cls):
        print('Estou criando uma instância da classe Produto')
        return super().__new__(cls)

    def __init__(self):
        print('Estou inicializando a instância da classe Produto')

    def fui_vendido(self):
        print('Fui vendido!')

produto = Produto()

produto.fui_vendido()
Produto.fui_vendido(produto)