# FarmTech - Sistema de Agricultura Digital

Projeto acadêmico desenvolvido em Python e R para simular uma aplicação de apoio à Agricultura Digital.

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

## Culturas utilizadas

O sistema trabalha com duas culturas:

- **Milho**
- **Café**

## Cálculo de área

### Milho
A área do milho é calculada usando a fórmula do retângulo:

Área = base × altura

### Café
A área do café é calculada usando a fórmula do círculo:

Área = π × raio²

## Manejo de insumos

O sistema calcula o total de insumo de duas formas:

### 1. Total por área
Cálculo:

Total por área = área × quantidade por m²

Esse cálculo depende da unidade escolhida no sistema.

### 2. Total por ruas da lavoura
Cálculo:

Total por ruas = número de ruas × litros por rua

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

## Funcionalidades da interface

A interface foi desenvolvida em **Tkinter** e possui:

- botão **Cadastrar**
- botão **Listar**
- botão **Atualizar**
- botão **Deletar**
- botão **Info**
- botão **Sair**
- troca de tema visual

## Temas disponíveis

O sistema possui três temas:

- **Azul**
- **Verde**
- **Preto**

## Campo Registro

O campo **Registro** é usado para atualizar ou deletar um item salvo.

Exemplo:
- primeiro registro = `0`
- segundo registro = `1`
- terceiro registro = `2`

## Integração com R

O projeto utiliza scripts em **R** para complementar a aplicação em Python.

### `estatistica.R`
Responsável por calcular:

- média
- desvio padrão

### `clima.R`
Responsável por consultar o clima atual de uma cidade utilizando API pública gratuita.

O usuário digita a cidade na interface e o Python envia essa informação para o script em R.

## Consulta meteorológica

A consulta de clima retorna:

- temperatura atual
- umidade relativa
- velocidade do vento
- horário da medição

A cidade é definida pelo usuário no campo:

**Cidade do clima**

## API utilizada

O sistema utiliza a **Open-Meteo API**, uma API meteorológica pública e gratuita.

## Tecnologias utilizadas

- **Python**
- **Tkinter**
- **R**
- **Open-Meteo API**
- **GitHub**

## Estrutura do projeto

```text
Farmtech_project/
├── main.py
├── estatistica.R
├── clima.R
├── README.md
└── .gitignore