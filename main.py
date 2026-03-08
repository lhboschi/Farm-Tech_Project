import tkinter as tk
from tkinter import messagebox
import math

culturas = []
areas = []
produtos = []
quantidades = []

def calcular_area():
    cultura = cultura_var.get()
    if cultura == "Milho":
        return float(entry1.get()) * float(entry2.get())
    return math.pi * float(entry1.get()) ** 2

def cadastrar():
    try:
        cultura = cultura_var.get()
        area = calcular_area()
        produto = entry_produto.get()
        qtd = float(entry_qtd.get())

        culturas.append(cultura)
        areas.append(area)
        produtos.append(produto)
        quantidades.append(qtd)

        listar()
    except:
        messagebox.showerror("Erro", "Preencha os campos corretamente")

def listar():
    texto.delete("1.0", tk.END)
    for i in range(len(culturas)):
        total = areas[i] * quantidades[i]
        texto.insert(tk.END, f"Registro: {i}\n")
        texto.insert(tk.END, f"Cultura: {culturas[i]}\n")
        texto.insert(tk.END, f"Área: {areas[i]:.2f}\n")
        texto.insert(tk.END, f"Produto: {produtos[i]}\n")
        texto.insert(tk.END, f"Total: {total:.2f}\n")
        texto.insert(tk.END, "-" * 30 + "\n")

janela = tk.Tk()
janela.title("FarmTech")
janela.geometry("700x500")

cultura_var = tk.StringVar(value="Milho")

tk.Label(janela, text="Cultura").pack()
tk.OptionMenu(janela, cultura_var, "Milho", "Café").pack()

tk.Label(janela, text="Base/Raio").pack()
entry1 = tk.Entry(janela)
entry1.pack()

tk.Label(janela, text="Altura").pack()
entry2 = tk.Entry(janela)
entry2.pack()

tk.Label(janela, text="Produto").pack()
entry_produto = tk.Entry(janela)
entry_produto.pack()

tk.Label(janela, text="Quantidade por m²").pack()
entry_qtd = tk.Entry(janela)
entry_qtd.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)

texto = tk.Text(janela, width=70, height=15)
texto.pack(pady=10)

janela.mainloop()