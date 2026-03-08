import math
import os

def localizar_rscript():
    caminhos = [
        r"C:\Program Files\R\R-4.5.2\bin\Rscript.exe",
        r"C:\Program Files\R\R-4.5.2\bin\x64\Rscript.exe"
    ]
    for caminho in caminhos:
        if os.path.exists(caminho):
            return caminho
    return None

def calcular_area(cultura, medida1, medida2=None):
    if cultura == "Milho":
        base = float(medida1)
        altura = float(medida2)
        area = base * altura
        return area, base, altura, 0
    else:
        raio = float(medida1)
        area = math.pi * raio ** 2
        return area, 0, 0, raio

def formatar_total_area(valor, unidade):
    if unidade == "mL/m²":
        litros = valor / 1000
        return f"{valor:.2f} mL | {litros:.2f} L"
    if unidade == "g/m²":
        quilos = valor / 1000
        return f"{valor:.2f} g | {quilos:.2f} kg"
    if unidade == "L/m²":
        return f"{valor:.2f} L"
    if unidade == "kg/m²":
        return f"{valor:.2f} kg"
    return f"{valor:.2f}"