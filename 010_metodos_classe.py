class Impressora:
    @classmethod
    def imprimir_folha(cls):
        print("Folha impressa")

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

print("-----Inicio imprimir_folha-----")
Impressora.imprimir_folha()
print("-----Fim imprimir_folha-----\n")
print("-----Inicio imprimir_livro-----")
Impressora.imprimir_livro(5)
print("-----Fim imprimir_livro-----")

impressora = Impressora()

impressora.imprimir_livro(2)