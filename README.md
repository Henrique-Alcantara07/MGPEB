# 🚀 Aurora SIGER

<div align="center">

### Sistema de Gerenciamento de Pouso e Estabilização

*Simulação em Python do controle de pouso de módulos espaciais em uma base marciana.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![FIAP](https://img.shields.io/badge/FIAP-Ci%C3%AAncia%20da%20Computa%C3%A7%C3%A3o-ED145B)

</div>

> 🎓 **Atividade acadêmica da FIAP**, desenvolvida para o curso de **Ciência da Computação**.  
> Tema: *A Aurora Ajusta a Trajetória na Aproximação a Marte* (**MGPEB**).

---

## 📑 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Como o sistema funciona](#-como-o-sistema-funciona)
- [Conceitos aplicados](#-conceitos-aplicados)
- [Dados de entrada](#-dados-de-entrada)
- [Regras de autorização de pouso](#-regras-de-autorização-de-pouso)
- [Modelagem matemática](#-modelagem-matemática)
- [Estrutura do repositório](#-estrutura-do-repositório)
- [Requisitos](#️-requisitos)
- [Como executar](#️-como-executar)
- [Resultado esperado](#️-resultado-esperado)
- [Galeria do projeto](#️-galeria-do-projeto)
- [Autores](#-autores)

---

## 📋 Sobre o projeto

Imagine que a nave **Aurora** está se aproximando de Marte e precisa pousar cinco módulos em uma base. Os módulos não podem descer todos de uma vez, e nem todos estão em condições seguras de pouso. O **SIGER** decide **quem desce primeiro e quem precisa esperar**, além de manter um histórico de tudo o que aconteceu.

O projeto reúne, em um único cenário, estruturas de dados lineares, algoritmos de ordenação e busca, lógica booleana e modelagem matemática.

**O que o sistema faz:**

1. 📥 Cadastra os módulos: Habitação, Energia, Suporte à Vida, Científico e Logística;
2. 🔢 Organiza a **fila de pouso** por prioridade;
3. 🛡️ Verifica as condições de segurança e **autoriza ou bloqueia** cada pouso;
4. 📜 Registra as decisões em uma **pilha de eventos**;
5. 🔎 Permite **buscar módulos** pelo nome;
6. 📉 Modela o **consumo de combustível** durante a descida e exibe um gráfico.

---

## 🔄 Como o sistema funciona

```mermaid
flowchart TD
    A[📥 Cadastro dos módulos] --> B[🔢 Selection Sort<br/>Fila ordenada por prioridade]
    A --> C[🔤 Insertion Sort<br/>Lista ordenada por nome]
    B --> D{🛡️ Verificação<br/>Combustível AND atmosfera<br/>AND área AND sensores}
    D -- Tudo OK --> E[✅ Pouso autorizado<br/>Vai para pousados]
    D -- Alguma falha --> F[⚠️ Pouso bloqueado<br/>Vai para alertas]
    E --> G[📜 Pilha de eventos]
    F --> G
    C --> H[🔎 Busca linear e binária]
    G --> I[📊 Resumo da operação]
    H --> I
    I --> J[📉 Gráfico de combustível]
```

### Etapas do processamento

| Etapa | O que acontece | Estrutura ou algoritmo |
|:---:|---|---|
| **1** | Os módulos são exibidos em uma tabela | Lista de listas (matriz) |
| **2** | A fila é reordenada, da maior para a menor prioridade | Selection Sort |
| **3** | O sistema processa a fila e decide cada pouso | Fila (FIFO) + lógica AND |
| **4** | Pousados, alertas e fila restante são resumidos | Listas |
| **5** | A pilha mostra o histórico, do evento mais recente ao mais antigo | Pilha (LIFO) |
| **6** | O usuário digita um nome e o módulo é localizado | Busca linear e binária |
| **7** | O consumo de combustível é calculado e plotado | NumPy + Matplotlib |

---

## 🧠 Conceitos aplicados

| Conceito | Aplicação no projeto | Complexidade |
|---|---|---|
| **Fila (FIFO)** | Ordem em que os pousos são processados (`append` para entrar, `pop(0)` para sair) | — |
| **Pilha (LIFO)** | Histórico de eventos, com o mais recente no topo (`append` para empilhar, leitura com `reversed`) | — |
| **Selection Sort** | Ordena a fila por prioridade, de forma decrescente | O(n²) |
| **Insertion Sort** | Ordena os módulos por nome (A → Z), preparando a busca binária | O(n²) no pior caso |
| **Busca linear** | Localiza um módulo na lista original, elemento por elemento | O(n) |
| **Busca binária** | Localiza um módulo na lista ordenada, descartando metade a cada passo | O(log n) |
| **Lógica booleana (AND)** | O pouso só é autorizado se todas as condições forem verdadeiras | — |
| **Função linear** | \(C(t) = C_0 - a \cdot t\), consumo de combustível | — |
| **NumPy e Matplotlib** | Cálculo vetorizado e geração do gráfico | — |

---

## 📦 Dados de entrada

Cada módulo é representado por uma **lista dentro de uma lista maior**. Cada posição guarda um campo fixo:

| Índice | Campo | Tipo |
|:---:|---|---|
| 0 | Nome | Texto |
| 1 | Prioridade (1 a 5) | Inteiro |
| 2 | Combustível (%) | Inteiro |
| 3 | Massa (toneladas) | Inteiro |
| 4 | Criticidade | Inteiro |
| 5 | Horário de chegada | Texto |
| 6 | Atmosfera OK | Booleano |
| 7 | Área livre | Booleano |
| 8 | Sensores OK | Booleano |

### Dados dos cinco módulos

| Módulo | Prioridade | Combustível | Massa | Criticidade | Chegada | Atmosfera | Área livre | Sensores |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Habitação | 4 | 85% | 20 t | 4 | 10:00 | ✅ | ✅ | ✅ |
| Energia | 5 | 92% | 15 t | 5 | 10:15 | ✅ | ✅ | ✅ |
| Suporte à Vida | 5 | 80% | 10 t | 5 | 10:30 | ✅ | ❌ | ✅ |
| Científico | 2 | 78% | 12 t | 2 | 10:45 | ✅ | ✅ | ✅ |
| Logística | 3 | 90% | 18 t | 3 | 11:00 | ✅ | ✅ | ❌ |

---

## ✅ Regras de autorização de pouso

Um módulo só pousa se atender **às quatro condições ao mesmo tempo**, representadas pela porta lógica **AND**.

| Nº | Condição | Critério |
|:---:|---|---|
| 1 | ⛽ Combustível | **≥ 80%** |
| 2 | 🌫️ Atmosfera | Adequada |
| 3 | 🛬 Área de pouso | Disponível |
| 4 | 📡 Sensores | Íntegros |

Basta **uma condição falhar** para o resultado final ser negativo. Nesse caso, o módulo vai para a lista de **alertas**, e o sistema apresenta o motivo de cada falha.

---

## 📉 Modelagem matemática

O combustível durante a descida é modelado por uma **função afim decrescente**:

\[
C(t) = C_0 - a \cdot t
\]

| Símbolo | Significado | Valor no projeto |
|---|---|:---:|
| \(C_0\) | Combustível inicial | 90% |
| \(a\) | Taxa de consumo | 2% por minuto |
| \(t\) | Tempo de descida | 0 a 30 minutos |
| \(C_{\min}\) | Limite mínimo de segurança | 80% |

O tempo até atingir o limite é calculado isolando \(t\):

```text
t_limite = (C₀ − C_min) / a
t_limite = (90 − 80) / 2
t_limite = 5 minutos
```

O `np.linspace(0, 30, 31)` gera 31 pontos de tempo (0, 1, 2, ..., 30). A função é aplicada a todos os pontos de uma só vez, sem precisar de um laço.

O gráfico mostra a reta cruzando a linha tracejada do limite de 80% aos **5 minutos**.

---

## 📁 Estrutura do repositório

```text
.
├── assets/
│   ├── screenshots/
│   │   ├── [1]_modulos_registrados.png
│   │   ├── [2]_selection_sort.png
│   │   ├── insertion_sort.png
│   │   ├── [3]_processamento_pousos.png
│   │   ├── [4]_[5]_resumo_pilha.png
│   │   ├── [6]_busca.png
│   │   └── [7]_modelagem_matematica.png
│   └── logic-gates/
│       └── portas_logicas.png
├── mgpeb.py
├── mgpeb.ipynb
├── README.md
├── Relatorio_Tecnico_MGPEB_Aurora_Siger.pdf
└── .gitignore
```

As duas versões têm a **mesma lógica e produzem os mesmos resultados**. O notebook acrescenta explicações passo a passo, tabelas de conceitos e uma célula que exibe a lista em ordem alfabética após o Insertion Sort.

---

## ⚙️ Requisitos

- Python 3.8 ou superior
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

No **Google Colab**, NumPy e Matplotlib já vêm instalados, então não é necessário instalar nada.

Para executar o script localmente:

```bash
pip install numpy matplotlib
```

---

## ▶️ Como executar

### Opção 1: Script Python (terminal)

```bash
python mgpeb.py
```

> 💡 O programa pede o nome de um módulo na etapa de busca. Ao final, abre uma janela com o gráfico e só termina depois que ela for fechada.

### Opção 2: Notebook (Google Colab)

1. Acesse [Google Colab](https://colab.research.google.com/).
2. Vá em **Arquivo → Fazer upload de notebook** e selecione `mgpeb.ipynb`.
3. Execute as células em ordem (`Shift + Enter`).

### Opção 3: Notebook (local)

```bash
pip install jupyter numpy matplotlib
jupyter notebook mgpeb.ipynb
```

### 🔎 Dicas para a etapa de busca

A busca ignora diferenças entre maiúsculas e minúsculas. Exemplos:

| Digite | Resultado |
|---|---|
| `energia` | ✅ Encontra Energia |
| `LOGÍSTICA` | ✅ Encontra Logística |
| `suporte à vida` | ✅ Encontra Suporte à Vida |
| `xyz` | ❌ Módulo não encontrado |

> ⚠️ A busca considera os **acentos**. Digitar `logistica` (sem acento) não encontra `Logística`.

---

## 🖥️ Resultado esperado

Com os dados de exemplo, a fila fica ordenada por prioridade e o processamento segue essa ordem:

| Ordem | Módulo | Prioridade | Resultado | Motivo |
|:---:|---|:---:|---|---|
| 1 | Energia | 5 | ✅ Pouso autorizado | Todas as condições atendidas |
| 2 | Suporte à Vida | 5 | ⚠️ Alerta | Área de pouso indisponível |
| 3 | Habitação | 4 | ✅ Pouso autorizado | Todas as condições atendidas |
| 4 | Logística | 3 | ⚠️ Alerta | Sensores comprometidos |
| 5 | Científico | 2 | ⚠️ Alerta | Combustível de 78% (abaixo de 80%) |

**Resumo:** 2 módulos pousam (Energia e Habitação), 3 ficam em alerta (Suporte à Vida, Logística e Científico) e a fila termina vazia.

### 📚 Histórico de eventos (LIFO)

A pilha de eventos mantém o histórico das decisões, com o evento mais recente no topo.

```text
TOPO  → Científico: pouso não autorizado
        Logística: pouso não autorizado
        Habitação: pouso autorizado
        Suporte à Vida: pouso não autorizado
BASE  → Energia: pouso autorizado
```

<details>
<summary><strong>📺 Ver exemplo de saída no terminal (trecho)</strong></summary>

```text
[ 3 ] PROCESSAMENTO DOS POUSOS
----------------------------------------------------------------

[2/5] Suporte à Vida
  Combustível........ OK
  Atmosfera.......... OK
  Área de pouso...... INDISPONÍVEL
  Sensores........... OK
  >> POUSO NÃO AUTORIZADO
  >> ALERTA: Área de pouso indisponível

[5/5] Científico
  Combustível........ INSUFICIENTE
  Atmosfera.......... OK
  Área de pouso...... OK
  Sensores........... OK
  >> POUSO NÃO AUTORIZADO
  >> ALERTA: Combustível insuficiente

[ 7 ] MODELAGEM MATEMÁTICA
----------------------------------------------------------------
Combustível inicial: 90%
Consumo por minuto: 2%
Limite mínimo: 80%
Tempo até atingir o limite: 5.0 minutos
```

</details>

---

## 🧩 Decisões de projeto

Algumas escolhas que valem ser explicadas:

- **Por que o Selection Sort não é estável?** Energia e Suporte à Vida têm a mesma prioridade (5). Como o algoritmo faz trocas entre posições diferentes, a ordem entre elementos iguais pode mudar. Neste projeto, ambos continuam nas duas primeiras posições, e o resultado final não é afetado.
- **Por que duas listas (`fila_pouso` e `modulos_alfabeticos`)?** A fila precisa estar ordenada por **prioridade**, enquanto a busca binária exige uma lista ordenada por **nome**. Cada estrutura mantém sua própria ordenação.
- **Por que `casefold()` em vez de `lower()`?** `casefold()` realiza uma normalização mais completa para comparações sem distinção entre maiúsculas e minúsculas, inclusive em alguns casos especiais de texto.
- **Por que `pop(0)` para a fila?** Remove e devolve o primeiro elemento, reproduzindo o comportamento FIFO. É simples e adequado para cinco módulos. Em um sistema maior, `collections.deque` seria mais eficiente para remover elementos do início.

---

## 🖼️ Galeria do projeto

Esta seção reúne capturas de tela das principais funcionalidades do Aurora SIGER, incluindo o cadastro dos módulos, o processamento da fila de pouso, as estruturas de dados utilizadas e a modelagem matemática.

### 📥 Cadastro dos módulos

![Cadastro dos módulos](assets/screenshots/[1]_modulos_registrados.png)

### 🔢 Fila de pouso

![Fila de pouso ordenada por prioridade](assets/screenshots/[2]_selection_sort.png)
![Fila de pouso ordenada por ordem alfabética](assets/screenshots/insertion_sort.png)

### 🛬 Processamento dos pousos

![Processamento dos pousos](assets/screenshots/[3]_processamento_pousos.png)

### 📊 Resumo da operação e Pilha

![Resumo da operação e Pilha](assets/screenshots/[4]_[5]_resumo_pilha.png)

### 🔎 Busca de módulos

![Busca de módulos](assets/screenshots/[6]_busca.png)

### 📈 Gráfico de consumo de combustível

![Gráfico de consumo de combustível](assets/screenshots/[7]_modelagem_matematica.png)

### 🔌 Portas lógicas AND e NOT

![Representação da porta lógica AND](assets/logic-gates/portas_logicas.png)

---

## 👤 Autores

Desenvolvido pelos integrantes:

| Nome | RM |
|---|---:|
| Henrique Floriano Alcantara | 575651 |
| Katia Regina Bispo | 576044 |
| João Pedro Candido Souza | 575884 |
| Nicolas Klai de de França | 575343 |
| Yago Souza Araujo | 575200 |

---

<div align="center">

*Feito com 🐍 Python e muito café, rumo a Marte 🔴*

</div>
