for i in range(10):
    print(i)

convidados = ["Dede", "Ana", "Luara"]

for convidado in convidados:
    print(convidado + " esta convidado")

for i in range(len(convidados)):
    convidado = convidados[i]
    print(convidado + " esta convidado")

saida = True
contador = 0

while saida:
    contador = contador + 1
    if contador == 10:
        saida = False
    print("contador: " + str(contador))

print("-------PROXIMO WHILE------")
contador = 0
while contador < 10:
    contador = contador + 1
    print("contador: " + str(contador))

print("-------PROXIMO WHILE------")
contador = 10
while contador >= 1:
    print("contador: " + str(contador))
    contador = contador - 1