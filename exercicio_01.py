
class Carro:

    rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

Carro.rodas = 5

print(carro1.__dict__)

print(carro2.marca)
print(carro2.modelo)
print(carro2.rodas) 

