class Animal:
    def fazer_barulho(self):
        print("Barulho de animal")


class Domestico:
    def esta_dormindo(self):
        return True


class Mamifero(Animal):
    pass


class Cachorro(Mamifero, Domestico):
    def fazer_barulho(self):
        print("Au..Au")

    def enterrar_osso(self):
        print("O osso foi enterrado")

        if cachorro.esta_dormindo():
            print("Dormindo")
        else:
            print("Acordado")


class Gato(Mamifero):
    def fazer_barulho(self):
        print("Miau...MiAu")


gato = Gato()
cachorro = Cachorro()

gato.fazer_barulho()
cachorro.fazer_barulho()
cachorro.enterrar_osso()
cachorro.esta_dormindo()
