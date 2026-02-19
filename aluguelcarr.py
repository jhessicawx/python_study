dias = int(input("Por quantos dias o carro foi aluagado: "))
km = float(input("Por quantos km o carro foi rodado: "))
valorApagar = (dias * 60) + (km * 0.15)
print("O valor total a pagar é de R${}".format (valorApagar))