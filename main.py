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
    if not culturas:
        print("Nenhum registro")
        return

    for i in range(len(culturas)):
        print(f"\nRegistro: {i}")
        print(f"Cultura: {culturas[i]}")
        print(f"Área: {areas[i]:.2f}")
        print(f"Produto: {produtos[i]}")
        print(f"Qtd por m²: {quantidades[i]:.2f}")

def atualizar():
    listar()
    i = int(input("Registro para atualizar: "))
    if i < 0 or i >= len(culturas):
        print("Registro inválido")
        return

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

    culturas[i] = cultura
    areas[i] = area
    produtos[i] = produto
    quantidades[i] = qtd

def deletar():
    listar()
    i = int(input("Registro para deletar: "))
    if i < 0 or i >= len(culturas):
        print("Registro inválido")
        return

    del culturas[i]
    del areas[i]
    del produtos[i]
    del quantidades[i]

while True:
    print("\n1-Cadastrar  2-Listar  3-Atualizar  4-Deletar  5-Sair")
    op = input("Opção: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "3":
        atualizar()
    elif op == "4":
        deletar()
    elif op == "5":
        break