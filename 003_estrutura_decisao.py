idade = 18

if idade < 18:
    print ("Menor de idade")
else:
    print ("Maior de idade")

veiculo = {"tipo": "moto2", "marca": "Honda", "potencia_motor": 140} 

if veiculo ["tipo"] == "moto" and veiculo ["marca"] == "Honda": #e se for moto mas de outra marca?
    print ("O veiculo é uma moto")
else:
    print ("O veiculo não é uma carro") #Certeza ?

if veiculo ["tipo"] == "moto2" or veiculo ["potencia_motor"] > 120:
    print ("Você tem um veiculo muito rapido")
else:
    print("Seu veiculo não rápido") #mesmo ? não tem carro rapido ?

if ["tipo"] == "moto2" and veiculo ["potencia_motor"] >120 or veiculo ["marca"] == "Honda":
    print ("O seu veiculo é muito bom")

if veiculo ["tipo"] == "moto":
    print ("moto")
elif veiculo ["tipo"] == "carro":
    print ("carro")
elif veiculo ["tipo"] == "moto1":
    print ("moto2")

nome = "verdadeiro"

if nome:
    print ("verdadeiro")
else:
    print ("falso")

nome = "verdadeiro"

condicao = 1

if nome:
    print ("verdadeiro")
else:
    print ("falso")