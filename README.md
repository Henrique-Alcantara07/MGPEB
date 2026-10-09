# 🚀 Aurora SIGER

**Sistema de Gerenciamento de Pouso e Estabilização**

> 🎓 **Atividade acadêmica da FIAP**, desenvolvida para o curso de **Ciência da Computação**.
> Tema: *A Aurora Ajusta a Trajetória na Aproximação a Marte* (**MGPEB**).

Simulação em Python do controle de pouso de módulos espaciais em uma base. O projeto aplica, em um cenário único, estruturas de dados lineares, algoritmos de ordenação e busca, lógica booleana e modelagem matemática.

---

## 📋 Sobre o projeto

O sistema recebe cinco módulos (Habitação, Energia, Suporte à Vida, Científico e Logística), cada um com prioridade, combustível, massa, criticidade, horário de chegada e condições de pouso. A partir disso ele:

1. Organiza a **fila de pouso** por prioridade;
2. Verifica as condições de segurança de cada módulo e **autoriza ou bloqueia** o pouso;
3. Registra todos os eventos em uma **pilha de histórico**;
4. Permite **buscar módulos** pelo nome;
5. Modela o **consumo de combustível** durante a descida e exibe um gráfico.

## 🧠 Conceitos aplicados

| Conceito | Aplicação no projeto | Complexidade |
|---|---|---|
| Fila (FIFO) | Ordem em que os pousos são processados | — |
| Pilha (LIFO) | Histórico de eventos, com o mais recente no topo | — |
| Selection Sort | Ordena a fila por prioridade (decrescente) | O(n²) |
| Insertion Sort | Ordena os módulos por nome (A → Z) | O(n²) pior caso |
| Busca linear | Localiza módulo na lista original | O(n) |
| Busca binária | Localiza módulo na lista ordenada | O(log n) |
| Lógica booleana (AND) | O pouso só é autorizado se **todas** as condições forem verdadeiras | — |
| Função linear | C(t) = C₀ − a·t, consumo de combustível | — |
| NumPy e Matplotlib | Cálculo vetorizado e gráfico | — |

## ✅ Regras de autorização de pouso

Um módulo só pousa se atender **às quatro condições** ao mesmo tempo:

- Combustível **≥ 80%**
- Atmosfera adequada
- Área de pouso disponível
- Sensores íntegros

Se qualquer uma falhar, o módulo vai para a lista de **alertas** e o motivo é exibido.

## 📁 Estrutura do repositório

```
.
├── mgpeb.py             # Versão em script Python
├── mgpeb.ipynb   # Versão em notebook, com explicações passo a passo
└── README.md
```

## ⚙️ Requisitos

- Python 3.8 ou superior
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- Jupyter (apenas para usar o notebook)

Instalação das dependências:

```bash
pip install numpy matplotlib jupyter
```

## ▶️ Como executar

**Script:**

```bash
python mgpeb.py
```

**Notebook:**

```bash
jupyter notebook aurora_siger.ipynb
```

Execute as células em ordem. Na etapa de busca, o programa pede o nome de um módulo (por exemplo, `energia`). A busca ignora diferenças entre maiúsculas e minúsculas.

## 🖥️ Resultado esperado

Com os dados de exemplo, o processamento segue a fila ordenada por prioridade:

| Módulo | Resultado | Motivo |
|---|---|---|
| Energia | ✅ Pouso autorizado | Todas as condições atendidas |
| Suporte à Vida | ⚠️ Alerta | Área de pouso indisponível |
| Habitação | ✅ Pouso autorizado | Todas as condições atendidas |
| Logística | ⚠️ Alerta | Sensores comprometidos |
| Científico | ⚠️ Alerta | Combustível de 78% (abaixo de 80%) |

O gráfico final mostra o combustível caindo de 90% a 2% por minuto e cruzando o limite mínimo de 80% aos **5 minutos** de descida.

## 🔧 Possíveis melhorias

- Ordenar por mais de um critério (prioridade e depois criticidade)
- Permitir o cadastro de novos módulos pelo usuário
- Simular o consumo de combustível individual de cada módulo
- Contar comparações dos algoritmos e plotar o crescimento da complexidade
- Separar o código em módulos (`ordenacao.py`, `busca.py`, etc.)

## 👤 Autores

Desenvolvido pelos integrantes:
- Henrique Floriano Alcantara - RM 575651
