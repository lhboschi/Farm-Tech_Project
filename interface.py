import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import csv
import dados
from logica import calcular_area, formatar_total_area, localizar_rscript


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


class FarmTechApp:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("FarmTech")
        self.janela.geometry("930x820")

        self.criar_interface()
        self.aplicar_tema("Azul")
        self.atualizar_labels()

    def limpar(self):
        self.entry_medida1.delete(0, tk.END)
        self.entry_medida2.delete(0, tk.END)
        self.entry_produto.delete(0, tk.END)
        self.entry_qtd_m2.delete(0, tk.END)
        self.entry_ruas.delete(0, tk.END)
        self.entry_litros_rua.delete(0, tk.END)
        self.entry_registro.delete(0, tk.END)

    def salvar_csv(self):
        with open("dados_farmtech.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow([
                "cultura",
                "area",
                "produto",
                "quantidade_m2",
                "unidade_m2",
                "ruas_lavoura",
                "litros_por_rua",
                "base",
                "altura",
                "raio"
            ])

            for i in range(len(dados.culturas)):
                escritor.writerow([
                  dados.culturas[i],
                  dados.areas[i],
                  dados.produtos[i],
                  dados.quantidades_m2[i],
                  dados.unidades_m2[i],
                  dados.ruas_lavoura[i],
                  dados.litros_por_rua[i],
                  dados.bases[i],
                  dados.alturas[i],
                  dados.raios[i]
            ])
                
    def atualizar_labels(self, *args):
        if self.cultura_var.get() == "Milho":
            self.label_medida1.config(text="Base (m)")
            self.label_medida2.config(text="Altura (m)")
            self.entry_medida2.config(state="normal")
        else:
            self.label_medida1.config(text="Raio (m)")
            self.label_medida2.config(text="Altura (não usar)")
            self.entry_medida2.delete(0, tk.END)
            self.entry_medida2.config(state="disabled")

    def mostrar_info(self):
        mensagem = (
            "FarmTech - Instruções de uso\n\n"

            "1. Escolha a cultura.\n"
            "   - Milho: usa Base e Altura.\n"
            "   - Café: usa apenas Raio.\n\n"

            "2. Preencha as medidas do terreno.\n"
            "   - Milho: Área = Base × Altura\n"
            "   - Café: Área = π × raio²\n\n"

            "3. Digite o Produto/insumo.\n\n"

            "4. Informe a Quantidade por m² e escolha a unidade.\n"
            "   Unidades disponíveis:\n"
            "   - mL/m²\n"
            "   - L/m²\n"
            "   - g/m²\n"
            "   - kg/m²\n\n"

            "5. Informe as Ruas da lavoura e os Litros por rua.\n"
            "   O sistema calcula:\n"
            "   - Total por área = área × quantidade por m²\n"
            "   - Total por ruas = ruas × litros por rua\n\n"

            "6. Clique em Cadastrar para salvar um novo registro.\n"
            "7. Clique em Listar para visualizar os registros cadastrados.\n\n"

            "8. Para editar um registro:\n"
            "   - Digite o número no campo Registro\n"
            "   - Clique em Carregar\n"
            "   - Altere um ou mais campos\n"
            "   - Clique em Atualizar\n\n"

            "9. Para excluir, digite o número no campo Registro e clique em Deletar.\n\n"

            "10. Para consultar o clima:\n"
            "    - Digite uma cidade no campo Cidade do clima\n"
            "    - Clique em Buscar clima em R\n\n"

            "11. Para análise estatística:\n"
            "    - Clique em Estatística em R\n"
            "    - O sistema usa os dados reais cadastrados no arquivo CSV\n"
            "    - Mostra quantidade de registros, média, desvio padrão,\n"
            "      menor área e maior área\n\n"

            "12. Temas visuais disponíveis:\n"
            "    - Azul\n"
            "    - Verde\n"
            "    - Preto\n\n"

            "Observações:\n"
            " - O campo Registro começa em 0.\n"
            " - Exemplo: primeiro registro = 0, segundo = 1.\n"
            " - Se existir apenas 1 registro, o desvio padrão não é calculado.\n"
        )
        messagebox.showinfo("Informações do Sistema", mensagem)
    
    def listar(self):
        self.texto.delete("1.0", tk.END)

        if not dados.culturas:
            self.texto.insert(tk.END, "Nenhum registro cadastrado.\n")
            return

        for i in range(len(dados.culturas)):
            total_area = dados.areas[i] * dados.quantidades_m2[i]
            total_ruas = dados.ruas_lavoura[i] * dados.litros_por_rua[i]

            self.texto.insert(tk.END, f"Registro: {i}\n")
            self.texto.insert(tk.END, f"Cultura: {dados.culturas[i]}\n")
            self.texto.insert(tk.END, f"Área: {dados.areas[i]:.2f} m²\n")
            self.texto.insert(tk.END, f"Produto: {dados.produtos[i]}\n")
            self.texto.insert(
                tk.END,
                f"Dose por m²: {dados.quantidades_m2[i]:.2f} {dados.unidades_m2[i]}\n"
            )
            self.texto.insert(
                tk.END,
                f"Total por área: {formatar_total_area(total_area, dados.unidades_m2[i])}\n"
            )
            self.texto.insert(tk.END, f"Ruas da lavoura: {dados.ruas_lavoura[i]}\n")
            self.texto.insert(tk.END, f"Litros por rua: {dados.litros_por_rua[i]:.2f} L\n")
            self.texto.insert(tk.END, f"Total por ruas: {total_ruas:.2f} L\n")
            self.texto.insert(tk.END, "-" * 46 + "\n")

    def cadastrar(self):
        try:
            cultura = self.cultura_var.get()
            area, base, altura, raio = calcular_area(
                cultura,
                self.entry_medida1.get(),
                self.entry_medida2.get() if cultura == "Milho" else None
            )

            produto = self.entry_produto.get().strip()
            qtd_m2 = float(self.entry_qtd_m2.get())
            unidade = self.unidade_var.get()
            ruas = int(self.entry_ruas.get())
            litros = float(self.entry_litros_rua.get())

            if not produto:
                messagebox.showerror("Erro", "Digite o nome do produto.")
                return

            dados.culturas.append(cultura)
            dados.areas.append(area)
            dados.produtos.append(produto)
            dados.quantidades_m2.append(qtd_m2)
            dados.unidades_m2.append(unidade)
            dados.ruas_lavoura.append(ruas)
            dados.litros_por_rua.append(litros)
            dados.bases.append(base)
            dados.alturas.append(altura)
            dados.raios.append(raio)

            self.limpar()
            self.listar()
            self.salvar_csv()
            messagebox.showinfo("Sucesso", "Registro cadastrado com sucesso.")
        except:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

    def carregar_registro(self):
        try:
            i = int(self.entry_registro.get())

            if i < 0 or i >= len(dados.culturas):
                messagebox.showerror("Erro", "Registro inválido.")
                return

            self.cultura_var.set(dados.culturas[i])

            self.entry_medida1.delete(0, tk.END)
            self.entry_medida2.delete(0, tk.END)
            self.entry_produto.delete(0, tk.END)
            self.entry_qtd_m2.delete(0, tk.END)
            self.entry_ruas.delete(0, tk.END)
            self.entry_litros_rua.delete(0, tk.END)

            if dados.culturas[i] == "Milho":
                self.entry_medida1.insert(0, str(dados.bases[i]))
                self.entry_medida2.config(state="normal")
                self.entry_medida2.insert(0, str(dados.alturas[i]))
            else:
                self.entry_medida1.insert(0, str(dados.raios[i]))
                self.entry_medida2.delete(0, tk.END)
                self.entry_medida2.config(state="disabled")

            self.entry_produto.insert(0, dados.produtos[i])
            self.entry_qtd_m2.insert(0, str(dados.quantidades_m2[i]))
            self.unidade_var.set(dados.unidades_m2[i])
            self.entry_ruas.insert(0, str(dados.ruas_lavoura[i]))
            self.entry_litros_rua.insert(0, str(dados.litros_por_rua[i]))

            messagebox.showinfo("Sucesso", f"Registro {i} carregado para edição.")
        except:
            messagebox.showerror("Erro", "Digite um número de registro válido.")

    def atualizar(self):
        try:
            i = int(self.entry_registro.get())

            if i < 0 or i >= len(dados.culturas):
                messagebox.showerror("Erro", "Registro inválido.")
                return

            cultura = self.cultura_var.get()
            area, base, altura, raio = calcular_area(
                cultura,
                self.entry_medida1.get(),
                self.entry_medida2.get() if cultura == "Milho" else None
            )

            produto = self.entry_produto.get().strip()
            qtd_m2 = float(self.entry_qtd_m2.get())
            unidade = self.unidade_var.get()
            ruas = int(self.entry_ruas.get())
            litros = float(self.entry_litros_rua.get())

            if not produto:
                messagebox.showerror("Erro", "Digite o nome do produto.")
                return

            dados.culturas[i] = cultura
            dados.areas[i] = area
            dados.produtos[i] = produto
            dados.quantidades_m2[i] = qtd_m2
            dados.unidades_m2[i] = unidade
            dados.ruas_lavoura[i] = ruas
            dados.litros_por_rua[i] = litros
            dados.bases[i] = base
            dados.alturas[i] = altura
            dados.raios[i] = raio

            self.limpar()
            self.listar()
            self.salvar_csv()
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso.")
        except:
            messagebox.showerror("Erro", "Confira o número do registro e os dados.")

    def deletar(self):
        try:
            i = int(self.entry_registro.get())

            if i < 0 or i >= len(dados.culturas):
                messagebox.showerror("Erro", "Registro inválido.")
                return

            del dados.culturas[i]
            del dados.areas[i]
            del dados.produtos[i]
            del dados.quantidades_m2[i]
            del dados.unidades_m2[i]
            del dados.ruas_lavoura[i]
            del dados.litros_por_rua[i]
            del dados.bases[i]
            del dados.alturas[i]
            del dados.raios[i]

            self.limpar()
            self.listar()
            self.salvar_csv()
            messagebox.showinfo("Sucesso", "Registro removido com sucesso.")
        except:
            messagebox.showerror("Erro", "Digite um registro válido.")

    def executar_r(self, arquivo, cidade=None):
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
            self.texto.delete("1.0", tk.END)
            self.texto.insert(tk.END, resultado.stdout)
        else:
            messagebox.showerror("Erro no R", resultado.stderr)

    def buscar_clima(self):
        cidade = self.entry_cidade.get().strip()

        if not cidade:
            messagebox.showerror("Erro", "Digite uma cidade para pesquisar.")
            return

        self.executar_r("clima.R", cidade)

    def estilizar_botao(self, botao, cores):
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

    def aplicar_tema(self, nome_tema):
        cores = TEMAS[nome_tema]

        self.janela.configure(bg=cores["FUNDO"])
        self.barra_topo.configure(bg=cores["FUNDO"])
        self.frame.configure(bg=cores["FUNDO"])
        self.botoes.configure(bg=cores["FUNDO"])

        self.titulo.config(bg=cores["FUNDO"], fg=cores["TEXTO"])

        labels = [
            self.label_cultura, self.label_medida1, self.label_medida2,
            self.label_produto, self.label_qtd_m2, self.label_unidade,
            self.label_ruas, self.label_litros_rua, self.label_registro,
            self.label_cidade
        ]

        for lbl in labels:
            lbl.config(bg=cores["FUNDO"], fg=cores["TEXTO"])

        entradas = [
            self.entry_medida1, self.entry_medida2, self.entry_produto,
            self.entry_qtd_m2, self.entry_ruas, self.entry_litros_rua,
            self.entry_registro, self.entry_cidade
        ]

        for ent in entradas:
            ent.config(
                bg=cores["FUNDO_CAIXA"],
                fg=cores["TEXTO"],
                insertbackground=cores["TEXTO"],
                relief="flat"
            )

        self.texto.config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"],
            insertbackground=cores["TEXTO"],
            relief="flat"
        )

        self.menu_cultura.config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"],
            activebackground=cores["BOTAO"],
            activeforeground=cores["BOTAO_TEXTO"],
            highlightthickness=0,
            relief="flat"
        )
        self.menu_cultura["menu"].config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"]
        )

        self.menu_unidade.config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"],
            activebackground=cores["BOTAO"],
            activeforeground=cores["BOTAO_TEXTO"],
            highlightthickness=0,
            relief="flat"
        )
        self.menu_unidade["menu"].config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"]
        )

        self.menu_tema.config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"],
            activebackground=cores["BOTAO"],
            activeforeground=cores["BOTAO_TEXTO"],
            highlightthickness=0,
            relief="flat"
        )
        self.menu_tema["menu"].config(
            bg=cores["FUNDO_CAIXA"],
            fg=cores["TEXTO"]
        )

        for botao in [
            self.botao_sair, self.botao_cadastrar, self.botao_listar,
            self.botao_carregar, self.botao_atualizar, self.botao_deletar,
            self.botao_info, self.botao_estatistica, self.botao_clima
        ]:
            self.estilizar_botao(botao, cores)

    def criar_interface(self):
        self.barra_topo = tk.Frame(self.janela)
        self.barra_topo.pack(fill="x", padx=10, pady=10)

        self.botao_sair = tk.Button(self.barra_topo, text="Sair", width=10, command=self.janela.destroy)
        self.botao_sair.pack(side="left", padx=5)

        self.tema_var = tk.StringVar(value="Azul")
        self.menu_tema = tk.OptionMenu(self.barra_topo, self.tema_var, "Azul", "Verde", "Preto", command=self.aplicar_tema)
        self.menu_tema.pack(side="left", padx=5)

        self.titulo = tk.Label(self.janela, text="FarmTech - Agricultura Digital", font=("Arial", 18, "bold"))
        self.titulo.pack(pady=10)

        self.frame = tk.Frame(self.janela)
        self.frame.pack(pady=5)

        self.cultura_var = tk.StringVar(value="Milho")
        self.cultura_var.trace_add("write", self.atualizar_labels)

        self.label_cultura = tk.Label(self.frame, text="Cultura")
        self.label_cultura.grid(row=0, column=0, sticky="w", padx=6, pady=4)

        self.menu_cultura = tk.OptionMenu(self.frame, self.cultura_var, "Milho", "Café")
        self.menu_cultura.grid(row=0, column=1, padx=6, pady=4)

        self.label_medida1 = tk.Label(self.frame, text="Base (m)")
        self.label_medida1.grid(row=1, column=0, sticky="w", padx=6, pady=4)

        self.entry_medida1 = tk.Entry(self.frame)
        self.entry_medida1.grid(row=1, column=1, padx=6, pady=4)

        self.label_medida2 = tk.Label(self.frame, text="Altura (m)")
        self.label_medida2.grid(row=2, column=0, sticky="w", padx=6, pady=4)

        self.entry_medida2 = tk.Entry(self.frame)
        self.entry_medida2.grid(row=2, column=1, padx=6, pady=4)

        self.label_produto = tk.Label(self.frame, text="Produto")
        self.label_produto.grid(row=3, column=0, sticky="w", padx=6, pady=4)

        self.entry_produto = tk.Entry(self.frame)
        self.entry_produto.grid(row=3, column=1, padx=6, pady=4)

        self.label_qtd_m2 = tk.Label(self.frame, text="Quantidade por m²")
        self.label_qtd_m2.grid(row=4, column=0, sticky="w", padx=6, pady=4)

        self.entry_qtd_m2 = tk.Entry(self.frame)
        self.entry_qtd_m2.grid(row=4, column=1, padx=6, pady=4)

        self.label_unidade = tk.Label(self.frame, text="Unidade por m²")
        self.label_unidade.grid(row=5, column=0, sticky="w", padx=6, pady=4)

        self.unidade_var = tk.StringVar(value="mL/m²")
        self.menu_unidade = tk.OptionMenu(self.frame, self.unidade_var, "mL/m²", "L/m²", "g/m²", "kg/m²")
        self.menu_unidade.grid(row=5, column=1, padx=6, pady=4)

        self.label_ruas = tk.Label(self.frame, text="Ruas da lavoura")
        self.label_ruas.grid(row=6, column=0, sticky="w", padx=6, pady=4)

        self.entry_ruas = tk.Entry(self.frame)
        self.entry_ruas.grid(row=6, column=1, padx=6, pady=4)

        self.label_litros_rua = tk.Label(self.frame, text="Litros por rua")
        self.label_litros_rua.grid(row=7, column=0, sticky="w", padx=6, pady=4)

        self.entry_litros_rua = tk.Entry(self.frame)
        self.entry_litros_rua.grid(row=7, column=1, padx=6, pady=4)

        self.label_registro = tk.Label(self.frame, text="Registro")
        self.label_registro.grid(row=8, column=0, sticky="w", padx=6, pady=4)

        self.entry_registro = tk.Entry(self.frame)
        self.entry_registro.grid(row=8, column=1, padx=6, pady=4)

        self.label_cidade = tk.Label(self.frame, text="Cidade do clima")
        self.label_cidade.grid(row=9, column=0, sticky="w", padx=6, pady=4)

        self.entry_cidade = tk.Entry(self.frame)
        self.entry_cidade.grid(row=9, column=1, padx=6, pady=4)

        self.botoes = tk.Frame(self.janela)
        self.botoes.pack(pady=12)

        self.botao_cadastrar = tk.Button(self.botoes, text="Cadastrar", width=14, command=self.cadastrar)
        self.botao_cadastrar.grid(row=0, column=0, padx=6, pady=6)

        self.botao_listar = tk.Button(self.botoes, text="Listar", width=14, command=self.listar)
        self.botao_listar.grid(row=0, column=1, padx=6, pady=6)

        self.botao_carregar = tk.Button(self.botoes, text="Carregar", width=14, command=self.carregar_registro)
        self.botao_carregar.grid(row=0, column=2, padx=6, pady=6)

        self.botao_atualizar = tk.Button(self.botoes, text="Atualizar", width=14, command=self.atualizar)
        self.botao_atualizar.grid(row=0, column=3, padx=6, pady=6)

        self.botao_deletar = tk.Button(self.botoes, text="Deletar", width=14, command=self.deletar)
        self.botao_deletar.grid(row=0, column=4, padx=6, pady=6)

        self.botao_info = tk.Button(self.botoes, text="Info", width=14, command=self.mostrar_info)
        self.botao_info.grid(row=0, column=5, padx=6, pady=6)

        self.botao_estatistica = tk.Button(
            self.janela,
            text="Estatística em R",
            width=20,
            command=lambda: self.executar_r("estatistica.R")
        )
        self.botao_estatistica.pack(pady=4)

        self.botao_clima = tk.Button(
            self.janela,
            text="Buscar clima em R",
            width=20,
            command=self.buscar_clima
        )
        self.botao_clima.pack(pady=4)

        self.texto = tk.Text(self.janela, width=102, height=20)
        self.texto.pack(pady=10)

    def executar(self):
        self.janela.mainloop()