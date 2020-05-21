class Veiculo:
    def __init__(self):
        self.cor = "Preto"
        self.velocidade = 0
        self.numero_rodas = 0

    def aumentar_velocidade(self, velocidade):
        self.velocidade += velocidade
        print("Acelerando...")
        print(f"Andando a {self.velocidade} km/h")

    def parar(self):
        self.velocidade = 0
        print("Parando.. parando...")
        print("Parado!!") 
        print(f"velocidade atual é {self.velocidade}")

    def buzinar(self):
        print("BiIiI BiiII")

   
class Bicicleta(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.numero_rodas = 2

    def buzinar(self):
        print("TrIiIm TriIIm")


bike = Bicicleta()
camelo = Bicicleta()

bike.cor = "Amarelo"
print("Bicicleta nome: BIKE")
print(f"Cor: {bike.cor}")
print(f"Velocidade atual {bike.velocidade}\n")

camelo.cor = "Vermelho"
print(f"Cor: {camelo.cor}")
print("Bicicleta nome: CAMELO")
print(f"Velocidade atual é {camelo.velocidade}")
camelo.aumentar_velocidade(20)
print(f"Velocidade atual é {camelo.velocidade}")
camelo.parar()
camelo.buzinar()