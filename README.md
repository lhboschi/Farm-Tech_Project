# FarmTech - Sistema de Agricultura Digital

Projeto acadêmico desenvolvido em **Python** e **R** para simular uma aplicação de apoio à **Agricultura Digital**.

## Objetivo

O sistema foi criado para atender aos requisitos de um projeto acadêmico envolvendo:

- duas culturas agrícolas
- cálculo de área de plantio
- cálculo de manejo de insumos
- uso de vetores
- operações de cadastro, listagem, atualização e remoção
- estatística básica em R
- consulta climática em R com API gratuita
- versionamento com GitHub
- organização do código em camadas

---

## Culturas utilizadas

O sistema trabalha com duas culturas:

- **Milho**
- **Café**

---

## Cálculo de área

### Milho
A área do milho é calculada usando a fórmula do retângulo:

**Área = base × altura**

### Café
A área do café é calculada usando a fórmula do círculo:

**Área = π × raio²**

---

## Manejo de insumos

O sistema calcula o total de insumo de duas formas:

### 1. Total por área
Cálculo:

**Total por área = área × quantidade por m²**

### 2. Total por ruas da lavoura
Cálculo:

**Total por ruas = número de ruas × litros por rua**

---

## Unidades de aplicação por área

O campo **Quantidade por m²** possui seletor de unidade.

Opções disponíveis:

- **mL/m²**
- **L/m²**
- **g/m²**
- **kg/m²**

### Conversões automáticas
O sistema também apresenta conversões automáticas para facilitar a leitura dos resultados:

- **mL → L**
- **g → kg**

### Exemplos
- Se o usuário informar **500 mL/m²**, o sistema mostra o total em **mL e litros**
- Se o usuário informar **250 g/m²**, o sistema mostra o total em **g e kg**

---

## Funcionalidades da interface

A interface foi desenvolvida em **Tkinter** e possui:

- botão **Cadastrar**
- botão **Listar**
- botão **Carregar**
- botão **Atualizar**
- botão **Deletar**
- botão **Info**
- botão **Sair**
- troca de tema visual

---

## Temas disponíveis

O sistema possui três temas:

- **Azul**
- **Verde**
- **Preto**

---

## Atualização de registros

O sistema permite editar registros sem precisar preencher tudo manualmente de novo.

### Como funciona
1. Digite o número no campo **Registro**
2. Clique em **Carregar**
3. O sistema preenche os campos automaticamente
4. Altere apenas os dados desejados
5. Clique em **Atualizar**

---

## Campo Registro

O campo **Registro** é usado para carregar, atualizar ou deletar um item salvo.

Exemplo:
- primeiro registro = `0`
- segundo registro = `1`
- terceiro registro = `2`

---

## Integração com R

O projeto utiliza scripts em **R** para complementar a aplicação em Python.

### `estatistica.R`
Responsável por calcular:

- média
- desvio padrão

### `clima.R`
Responsável por consultar o clima atual de uma cidade utilizando API pública gratuita.

O usuário digita a cidade na interface e o Python envia essa informação para o script em R.

---

## Consulta meteorológica

A consulta de clima retorna:

- temperatura atual
- umidade relativa
- velocidade do vento
- horário da medição

A cidade é definida pelo usuário no campo:

**Cidade do clima**

---

## API utilizada

O sistema utiliza a **Open-Meteo API**, uma API meteorológica pública e gratuita.

---

## Tecnologias utilizadas

- **Python**
- **Tkinter**
- **R**
- **Open-Meteo API**
- **GitHub**

---

## Arquitetura em camadas

O projeto foi reorganizado em camadas para melhorar a estrutura e a organização do código.

### `dados.py`
Responsável por armazenar os vetores do sistema.

Exemplos:
- culturas
- áreas
- produtos
- quantidades
- unidades
- ruas da lavoura
- litros por rua

### `logica.py`
Responsável pelas regras e cálculos do sistema.

Exemplos:
- cálculo de área
- formatação de totais
- localização do `Rscript`

### `interface.py`
Responsável pela interface gráfica e interação com o usuário.

Exemplos:
- tela principal
- botões
- campos
- eventos de cadastro, atualização, exclusão, clima e estatística

### `main.py`
Responsável apenas por iniciar a aplicação.

---

## Estrutura do projeto

```text
farmtech-project/
├── main.py
├── interface.py
├── logica.py
├── dados.py
├── clima.R
├── estatistica.R
├── README.md
└── .gitignore