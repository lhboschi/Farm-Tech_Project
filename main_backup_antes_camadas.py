import tkinter as tk
from tkinter import messagebox
import math
import os
import subprocess

# =========================
# VETORES DE DADOS
# =========================
culturas = []
areas = []
produtos = []
quantidades_m2 = []
unidades_m2 = []
ruas_lavoura = []
litros_por_rua = []
bases = []
alturas = []
raios = []
# =========================
# TEMAS
# =========================
TEMAS = {
    "Azul": {
        "FUNDO": "#0f172a",
        "FUNDO_CAIXA": "#1e293b",
        "TEXTO": "#93c5fd",
        "BOTAO": "#1e3a8a",
        "BOTAO_TEXTO": "#dbeafe"
    },
    "Verde": {
        "FUNDO": "#022c22",
        "FUNDO_CAIXA": "#064e3b",
        "TEXTO": "#6ee7b7",
        "BOTAO": "#065f46",
        "BOTAO_TEXTO": "#d1fae5"
    },
    "Preto": {
        "FUNDO": "#020617",
        "FUNDO_CAIXA": "#0f172a",
        "TEXTO": "#cbd5f5",
        "BOTAO": "#1e293b",
        "BOTAO_TEXTO": "#e2e8f0"
    }
}

# =========================
# FUNÇÕES
# =========================
def localizar_rscript():
    caminhos = [
        r"C:\Program Files\R\R-4.5.2\bin\Rscript.exe",
        r"C:\Program Files\R\R-4.5.2\bin\x64\Rscript.exe"
    ]
    for caminho in caminhos:
        if os.path.exists(caminho):
            return caminho
    return None


def calcular_area(cultura):
    if cultura == "Milho":
        base = float(entry_medida1.get())
        altura = float(entry_medida2.get())
        area = base * altura
        return area, base, altura, 0
    else:
        raio = float(entry_medida1.get())
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


def limpar():
    entry_medida1.delete(0, tk.END)
    entry_medida2.delete(0, tk.END)
    entry_produto.delete(0, tk.END)
    entry_qtd_m2.delete(0, tk.END)
    entry_ruas.delete(0, tk.END)
    entry_litros_rua.delete(0, tk.END)
    entry_registro.delete(0, tk.END)


def atualizar_labels(*args):
    if cultura_var.get() == "Milho":
        label_medida1.config(text="Base (m)")
        label_medida2.config(text="Altura (m)")
        entry_medida2.config(state="normal")
    else:
        label_medida1.config(text="Raio (m)")
        label_medida2.config(text="Altura (não usar)")
        entry_medida2.delete(0, tk.END)
        entry_medida2.config(state="disabled")


def mostrar_info():
    mensagem = (
        "SISTEMA FARMTECH - AGRICULTURA DIGITAL\n\n"
        "Objetivo:\n"
        "Este sistema simula uma aplicação de apoio à agricultura digital, "
        "integrando Python e R.\n\n"

        "Culturas usadas:\n"
        "- Milho: área calculada por retângulo.\n"
        "- Café: área calculada por círculo.\n\n"

        "Fórmulas:\n"
        "- Milho = base × altura\n"
        "- Café = pi × raio²\n\n"

        "Dose por metro quadrado:\n"
        "O campo 'Quantidade por m²' agora possui unidade selecionável.\n"
        "Opções disponíveis:\n"
        "- mL/m²\n"
        "- L/m²\n"
        "- g/m²\n"
        "- kg/m²\n\n"

        "Interpretação prática:\n"
        "- mL/m² e L/m² podem ser usados para insumos líquidos.\n"
        "- g/m² e kg/m² podem ser usados para insumos sólidos.\n\n"

        "Manejo de insumos:\n"
        "O sistema calcula de duas formas:\n"
        "1. Total por área = área × quantidade por m²\n"
        "2. Total por ruas = ruas da lavoura × litros por rua\n\n"

        "Conversões automáticas:\n"
        "- Se a unidade por área for mL, o sistema também mostra o valor em litros.\n"
        "- Se a unidade por área for g, o sistema também mostra o valor em kg.\n\n"

        "Campos da interface:\n"
        "- Cultura: Milho ou Café.\n"
        "- Base / Altura / Raio: medidas da área.\n"
        "- Produto: nome do insumo.\n"
        "- Quantidade por m²: dose aplicada por metro quadrado.\n"
        "- Unidade por m²: unidade da dose aplicada.\n"
        "- Ruas da lavoura: quantidade de ruas.\n"
        "- Litros por rua: volume aplicado em cada rua.\n"
        "- Registro: número do item salvo, usado para atualizar ou deletar.\n"
        "- Cidade do clima: cidade consultada na API meteorológica.\n\n"

        "Como usar:\n"
        "1. Escolha a cultura.\n"
        "2. Digite as medidas do terreno.\n"
        "3. Informe o produto.\n"
        "4. Digite a quantidade por m².\n"
        "5. Escolha a unidade correta.\n"
        "6. Informe ruas da lavoura e litros por rua.\n"
        "7. Clique em Cadastrar.\n"
        "8. Use Listar para visualizar os registros.\n"
        "9. Use Registro para atualizar ou deletar um item.\n"
        "10. Digite uma cidade e clique em Buscar clima em R.\n"
        "11. Clique em Estatística em R para executar o script estatístico.\n\n"

        "Observação sobre Registro:\n"
        "O primeiro registro é 0, o segundo é 1, o terceiro é 2.\n\n"

        "Integração com R:\n"
        "- estatistica.R calcula média e desvio padrão.\n"
        "- clima.R consulta temperatura, umidade, vento e horário pela API Open-Meteo.\n\n"

        "Temas disponíveis:\n"
        "- Azul\n"
        "- Verde\n"
        "- Preto"
    )
    messagebox.showinfo("Informações do Sistema", mensagem)


def listar():
    texto.delete("1.0", tk.END)

    if not culturas:
        texto.insert(tk.END, "Nenhum registro cadastrado.\n")
        return

    for i in range(len(culturas)):
        total_area = areas[i] * quantidades_m2[i]
        total_ruas = ruas_lavoura[i] * litros_por_rua[i]

        texto.insert(tk.END, f"Registro: {i}\n")
        texto.insert(tk.END, f"Cultura: {culturas[i]}\n")
        texto.insert(tk.END, f"Área: {areas[i]:.2f} m²\n")
        texto.insert(tk.END, f"Produto: {produtos[i]}\n")
        texto.insert(tk.END, f"Dose por m²: {quantidades_m2[i]:.2f} {unidades_m2[i]}\n")
        texto.insert(tk.END, f"Total por área: {formatar_total_area(total_area, unidades_m2[i])}\n")
        texto.insert(tk.END, f"Ruas da lavoura: {ruas_lavoura[i]}\n")
        texto.insert(tk.END, f"Litros por rua: {litros_por_rua[i]:.2f} L\n")
        texto.insert(tk.END, f"Total por ruas: {total_ruas:.2f} L\n")
        texto.insert(tk.END, "-" * 46 + "\n")


def cadastrar():
    try:
        cultura = cultura_var.get()
        area, base, altura, raio = calcular_area(cultura)

        produto = entry_produto.get().strip()
        qtd_m2 = float(entry_qtd_m2.get())
        unidade = unidade_var.get()
        ruas = int(entry_ruas.get())
        litros = float(entry_litros_rua.get())

        if not produto:
            messagebox.showerror("Erro", "Digite o nome do produto.")
            return

        culturas.append(cultura)
        areas.append(area)
        produtos.append(produto)
        quantidades_m2.append(qtd_m2)
        unidades_m2.append(unidade)
        ruas_lavoura.append(ruas)
        litros_por_rua.append(litros)
        bases.append(base)
        alturas.append(altura)
        raios.append(raio)

        limpar()
        listar()
        messagebox.showinfo("Sucesso", "Registro cadastrado com sucesso.")
    except:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")


def atualizar():
    try:
        i = int(entry_registro.get())

        if i < 0 or i >= len(culturas):
            messagebox.showerror("Erro", "Registro inválido.")
            return

        cultura = cultura_var.get()
        area, base, altura, raio = calcular_area(cultura)

        produto = entry_produto.get().strip()
        qtd_m2 = float(entry_qtd_m2.get())
        unidade = unidade_var.get()
        ruas = int(entry_ruas.get())
        litros = float(entry_litros_rua.get())

        if not produto:
            messagebox.showerror("Erro", "Digite o nome do produto.")
            return

        culturas[i] = cultura
        areas[i] = area
        produtos[i] = produto
        quantidades_m2[i] = qtd_m2
        unidades_m2[i] = unidade
        ruas_lavoura[i] = ruas
        litros_por_rua[i] = litros
        bases[i] = base
        alturas[i] = altura
        raios[i] = raio

        limpar()
        listar()
        messagebox.showinfo("Sucesso", "Registro atualizado com sucesso.")
    except:
        messagebox.showerror("Erro", "Confira o número do registro e os dados.")


def deletar():
    try:
        i = int(entry_registro.get())

        if i < 0 or i >= len(culturas):
            messagebox.showerror("Erro", "Registro inválido.")
            return

        del culturas[i]
        del areas[i]
        del produtos[i]
        del quantidades_m2[i]
        del unidades_m2[i]
        del ruas_lavoura[i]
        del litros_por_rua[i]
        del bases[i]
        del alturas[i]
        del raios[i]

        limpar()
        listar()
        messagebox.showinfo("Sucesso", "Registro removido com sucesso.")
    except:
        messagebox.showerror("Erro", "Digite um registro válido.")

def executar_r(arquivo, cidade=None):
    rscript = localizar_rscript()

    if not rscript:
        messagebox.showerror("Erro", "Rscript não encontrado.")
        return

    caminho_arquivo = os.path.join(os.path.dirname(__file__), arquivo)
    comando = [rscript, caminho_arquivo]

    if cidade:
        comando.append(cidade)

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if resultado.returncode == 0:
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, resultado.stdout)
    else:
        messagebox.showerror("Erro no R", resultado.stderr)


def buscar_clima():
    cidade = entry_cidade.get().strip()

    if not cidade:
        messagebox.showerror("Erro", "Digite uma cidade para pesquisar.")
        return

    executar_r("clima.R", cidade)


def estilizar_botao(botao, cores):
    botao.config(
        bg=cores["BOTAO"],
        fg=cores["BOTAO_TEXTO"],
        activebackground=cores["BOTAO"],
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        font=("Segoe UI", 10, "bold"),
        padx=8,
        pady=6
    )


def aplicar_tema(nome_tema):
    cores = TEMAS[nome_tema]

    janela.configure(bg=cores["FUNDO"])
    barra_topo.configure(bg=cores["FUNDO"])
    frame.configure(bg=cores["FUNDO"])
    botoes.configure(bg=cores["FUNDO"])

    titulo.config(bg=cores["FUNDO"], fg=cores["TEXTO"])

    labels = [
        label_cultura, label_medida1, label_medida2, label_produto,
        label_qtd_m2, label_unidade, label_ruas, label_litros_rua,
        label_registro, label_cidade
    ]

    for lbl in labels:
        lbl.config(bg=cores["FUNDO"], fg=cores["TEXTO"])

    entradas = [
        entry_medida1, entry_medida2, entry_produto, entry_qtd_m2,
        entry_ruas, entry_litros_rua, entry_registro, entry_cidade
    ]

    for ent in entradas:
        ent.config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"],
            insertbackground=cores["TEXTO"],
            relief="flat"
        )

    texto.config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"],
        insertbackground=cores["TEXTO"],
        relief="flat"
    )

    menu_cultura.config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"],
        activebackground=cores["BOTAO"],
        activeforeground=cores["BOTAO_TEXTO"],
        highlightthickness=0,
        relief="flat"
    )
    menu_cultura["menu"].config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"]
    )

    menu_unidade.config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"],
        activebackground=cores["BOTAO"],
        activeforeground=cores["BOTAO_TEXTO"],
        highlightthickness=0,
        relief="flat"
    )
    menu_unidade["menu"].config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"]
    )

    menu_tema.config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"],
        activebackground=cores["BOTAO"],
        activeforeground=cores["BOTAO_TEXTO"],
        highlightthickness=0,
        relief="flat"
    )
    menu_tema["menu"].config(
        bg=cores["FUNDO_CAIXA"],
        fg=cores["TEXTO"]
    )

    for botao in [
        botao_sair, botao_cadastrar, botao_listar, botao_atualizar,
        botao_deletar, botao_info, botao_estatistica, botao_clima, botao_carregar
    ]:
        estilizar_botao(botao, cores)

def carregar_registro():
    try:
        i = int(entry_registro.get())

        if i < 0 or i >= len(culturas):
            messagebox.showerror("Erro", "Registro inválido.")
            return

        cultura_var.set(culturas[i])

        entry_medida1.delete(0, tk.END)
        entry_medida2.delete(0, tk.END)
        entry_produto.delete(0, tk.END)
        entry_qtd_m2.delete(0, tk.END)
        entry_ruas.delete(0, tk.END)
        entry_litros_rua.delete(0, tk.END)

        if culturas[i] == "Milho":
            entry_medida1.insert(0, str(bases[i]))
            entry_medida2.config(state="normal")
            entry_medida2.insert(0, str(alturas[i]))
        else:
            entry_medida1.insert(0, str(raios[i]))
            entry_medida2.delete(0, tk.END)
            entry_medida2.config(state="disabled")

        entry_produto.insert(0, produtos[i])
        entry_qtd_m2.insert(0, str(quantidades_m2[i]))
        unidade_var.set(unidades_m2[i])
        entry_ruas.insert(0, str(ruas_lavoura[i]))
        entry_litros_rua.insert(0, str(litros_por_rua[i]))

        messagebox.showinfo("Sucesso", f"Registro {i} carregado para edição.")
    except:
        messagebox.showerror("Erro", "Digite um número de registro válido.")

# =========================
# INTERFACE
# =========================
janela = tk.Tk()
janela.title("FarmTech")
janela.geometry("930x800")

barra_topo = tk.Frame(janela)
barra_topo.pack(fill="x", padx=10, pady=10)

botao_sair = tk.Button(barra_topo, text="Sair", width=10, command=janela.destroy)
botao_sair.pack(side="left", padx=5)

tema_var = tk.StringVar(value="Azul")
menu_tema = tk.OptionMenu(barra_topo, tema_var, "Azul", "Verde", "Preto", command=aplicar_tema)
menu_tema.pack(side="left", padx=5)

titulo = tk.Label(janela, text="FarmTech - Agricultura Digital", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

frame = tk.Frame(janela)
frame.pack(pady=5)

cultura_var = tk.StringVar(value="Milho")
cultura_var.trace_add("write", atualizar_labels)

label_cultura = tk.Label(frame, text="Cultura")
label_cultura.grid(row=0, column=0, sticky="w", padx=6, pady=4)

menu_cultura = tk.OptionMenu(frame, cultura_var, "Milho", "Café")
menu_cultura.grid(row=0, column=1, padx=6, pady=4)

label_medida1 = tk.Label(frame, text="Base (m)")
label_medida1.grid(row=1, column=0, sticky="w", padx=6, pady=4)

entry_medida1 = tk.Entry(frame)
entry_medida1.grid(row=1, column=1, padx=6, pady=4)

label_medida2 = tk.Label(frame, text="Altura (m)")
label_medida2.grid(row=2, column=0, sticky="w", padx=6, pady=4)

entry_medida2 = tk.Entry(frame)
entry_medida2.grid(row=2, column=1, padx=6, pady=4)

label_produto = tk.Label(frame, text="Produto")
label_produto.grid(row=3, column=0, sticky="w", padx=6, pady=4)

entry_produto = tk.Entry(frame)
entry_produto.grid(row=3, column=1, padx=6, pady=4)

label_qtd_m2 = tk.Label(frame, text="Quantidade por m²")
label_qtd_m2.grid(row=4, column=0, sticky="w", padx=6, pady=4)

entry_qtd_m2 = tk.Entry(frame)
entry_qtd_m2.grid(row=4, column=1, padx=6, pady=4)

label_unidade = tk.Label(frame, text="Unidade por m²")
label_unidade.grid(row=5, column=0, sticky="w", padx=6, pady=4)

unidade_var = tk.StringVar(value="mL/m²")
menu_unidade = tk.OptionMenu(frame, unidade_var, "mL/m²", "L/m²", "g/m²", "kg/m²")
menu_unidade.grid(row=5, column=1, padx=6, pady=4)

label_ruas = tk.Label(frame, text="Ruas da lavoura")
label_ruas.grid(row=6, column=0, sticky="w", padx=6, pady=4)

entry_ruas = tk.Entry(frame)
entry_ruas.grid(row=6, column=1, padx=6, pady=4)

label_litros_rua = tk.Label(frame, text="Litros por rua")
label_litros_rua.grid(row=7, column=0, sticky="w", padx=6, pady=4)

entry_litros_rua = tk.Entry(frame)
entry_litros_rua.grid(row=7, column=1, padx=6, pady=4)

label_registro = tk.Label(frame, text="Registro")
label_registro.grid(row=8, column=0, sticky="w", padx=6, pady=4)

entry_registro = tk.Entry(frame)
entry_registro.grid(row=8, column=1, padx=6, pady=4)

label_cidade = tk.Label(frame, text="Cidade do clima")
label_cidade.grid(row=9, column=0, sticky="w", padx=6, pady=4)

entry_cidade = tk.Entry(frame)
entry_cidade.grid(row=9, column=1, padx=6, pady=4)

botoes = tk.Frame(janela)
botoes.pack(pady=12)

botao_cadastrar = tk.Button(botoes, text="Cadastrar", width=14, command=cadastrar)
botao_cadastrar.grid(row=0, column=0, padx=6, pady=6)

botao_listar = tk.Button(botoes, text="Listar", width=14, command=listar)
botao_listar.grid(row=0, column=1, padx=6, pady=6)

botao_carregar = tk.Button(botoes, text="Carregar", width=14, command=carregar_registro)
botao_carregar.grid(row=0, column=2, padx=6, pady=6)

botao_atualizar = tk.Button(botoes, text="Atualizar", width=14, command=atualizar)
botao_atualizar.grid(row=0, column=3, padx=6, pady=6)

botao_deletar = tk.Button(botoes, text="Deletar", width=14, command=deletar)
botao_deletar.grid(row=0, column=4, padx=6, pady=6)

botao_info = tk.Button(botoes, text="Info", width=14, command=mostrar_info)
botao_info.grid(row=0, column=5, padx=6, pady=6)


botao_estatistica = tk.Button(
    janela,
    text="Estatística em R",
    width=20,
    command=lambda: executar_r("estatistica.R")
)
botao_estatistica.pack(pady=4)

botao_clima = tk.Button(
    janela,
    text="Buscar clima em R",
    width=20,
    command=buscar_clima
)
botao_clima.pack(pady=4)

texto = tk.Text(janela, width=102, height=20)
texto.pack(pady=10)

aplicar_tema("Azul")
atualizar_labels()
janela.mainloop()