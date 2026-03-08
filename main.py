import math

culturas = []
areas = []
produtos = []
quantidades = []

def calcular_area(cultura):
    if cultura == "Milho":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        return base * altura
    else:
        raio = float(input("Raio: "))
        return math.pi * raio ** 2

def cadastrar():
    print("1 - Milho")
    print("2 - Café")
    op = input("Escolha: ")

    if op == "1":
        cultura = "Milho"
    elif op == "2":
        cultura = "Café"
    else:
        print("Opção inválida")
        return

    area = calcular_area(cultura)
    produto = input("Produto: ")
    qtd = float(input("Quantidade por m²: "))

    culturas.append(cultura)
    areas.append(area)
    produtos.append(produto)
    quantidades.append(qtd)

def listar():
    for i in range(len(culturas)):
        print(i, culturas[i], areas[i], produtos[i], quantidades[i])

while True:
    print("\n1-Cadastrar  2-Listar  3-Sair")
    op = input("Opção: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "3":
        break