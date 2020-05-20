class Mamifero:
    def emitir_som(self):
        pass


class Cachorro(Mamifero):
    def emitir_som(self):
        print("Au..Au")


class Gato(Mamifero):
    def emitir_som(self):
        print("MiAu...MiAu")


class Rato(Mamifero):
    def emitir_som(self):
        print("Som.. de Rato")


cachorro = Cachorro()
gato = Gato()
rato = Rato()

mamiferos = [cachorro, gato, rato]

for mamifero in mamiferos:
    mamifero.emitir_som()

