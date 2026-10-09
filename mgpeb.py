# ============================================================
# AURORA SIGER
# Sistema de Gerenciamento de Pouso e Estabilização
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# DADOS DOS MÓDULOS
# ============================================================

# Estrutura em lista:
# [0] Nome | [1] Prioridade | [2] Combustível (%) | [3] Massa (toneladas)
# [4] Criticidade | [5] Chegada | [6] Atmosfera OK | [7] Área Livre | [8] Sensores OK
modulos = [
    ["Habitação", 4, 85, 20, 4, "10:00", True, True, True],
    ["Energia", 5, 92, 15, 5, "10:15", True, True, True],
    ["Suporte à Vida", 5, 80, 10, 5, "10:30", True, False, True],
    ["Científico", 2, 78, 12, 2, "10:45", True, True, True],
    ["Logística", 3, 90, 18, 3, "11:00", True, True, False]
]

# ============================================================
# ESTRUTURAS DE DADOS LINEARES
# ============================================================

# Fila de pouso (Comportamento FIFO - First In, First Out)
fila_pouso = []
for modulo in modulos:
    fila_pouso.append(modulo) # Enfileirando elementos no final da lista

modulos_pousados = []
modulos_alerta = []

# Pilha de eventos (Comportamento LIFO - Last In, First Out)
# Será usada para registrar o histórico de ações do sistema
pilha_eventos = []

# Lista auxiliar copiada para realizar a busca binária posteriormente
modulos_alfabeticos = []
for modulo in modulos:
    modulos_alfabeticos.append(modulo)


# ============================================================
# FUNÇÕES DE EXIBIÇÃO
# ============================================================

def exibir_titulo():
    print("=" * 94)
    print(" " * 38 + "AURORA SIGER")
    print(" " * 17 + "SISTEMA DE GERENCIAMENTO DE POUSO E ESTABILIZAÇÃO")
    print("=" * 94)

def exibir_modulos(modulos):
    print("\n[ 1 ] MÓDULOS REGISTRADOS")
    print("-" * 94)
    print(f"{'Módulo':<20}{'Prioridade':<13}{'Combustível':<15}{'Massa':<12}{'Criticidade':<14}{'Chegada':<12}")
    print("-" * 94)
    for modulo in modulos:
        print(f"{modulo[0]:<20}{modulo[1]:<13}{str(modulo[2]) + '%':<15}{str(modulo[3]) + ' t':<12}{modulo[4]:<14}{modulo[5]:<12}")

def exibir_fila(fila):
    print("\n[ 2 ] FILA DE POUSO POR PRIORIDADE")
    print("-" * 64)
    print(f"{'ORDEM':<10}{'MÓDULO':<30}{'PRIORIDADE':<12}")
    print("-" * 64)
    ordem = 1
    for modulo in fila:
        print(f"{ordem:<10}{modulo[0]:<30}{modulo[1]:<12}")
        ordem += 1

def exibir_resumo(pousados, alertas, fila):
    print("\n[ 4 ] RESUMO DA OPERAÇÃO")
    print("=" * 64)
    print("\nMÓDULOS POUSADOS")
    print("-" * 64)
    if pousados:
        for modulo in pousados:
            print(f"- {modulo[0]}")
    else:
        print("Nenhum módulo pousado.")

    print("\nMÓDULOS EM ALERTA")
    print("-" * 64)
    if alertas:
        for modulo in alertas:
            print(f"- {modulo[0]}")
    else:
        print("Nenhum módulo em alerta.")

    print("\nFILA DE POUSO")
    print("-" * 64)
    print(f"{len(fila)} módulo(s) aguardando.")

def exibir_pilha(pilha):
    print("\n[ 6 ] PILHA DE EVENTOS")
    print("=" * 64)
    print("TOPO DA PILHA — evento mais recente (LIFO)")
    print("-" * 64)
    
    # Lendo a pilha de trás para frente (LIFO - O último a entrar é o primeiro a sair visualmente)
    if pilha:
        for evento in reversed(pilha):
            print(f"- {evento}")
    else:
        print("Nenhum evento registrado.")
    print("-" * 64)
    print("BASE DA PILHA — evento mais antigo")


# ============================================================
# MODELAGEM MATEMÁTICA - CONSUMO DE COMBUSTÍVEL
# ============================================================

def calcular_combustivel(combustivel_inicial, taxa_consumo, tempo):
    # Função matemática linear: y = b - a*x
    return combustivel_inicial - taxa_consumo * tempo

def exibir_grafico_combustivel():
    combustivel_inicial = 90
    taxa_consumo = 2
    limite_combustivel = 80

    # Utilizando numpy para gerar o vetor de tempo de 0 a 30 minutos
    tempo = np.linspace(0, 30, 31)
    combustivel = calcular_combustivel(combustivel_inicial, taxa_consumo, tempo)

    print('\n[ 7 ] MODELAGEM MATEMÁTICA')
    print("-" * 64)

    tempo_limite = (combustivel_inicial - limite_combustivel) / taxa_consumo
    print(f'Combustível inicial: {combustivel_inicial}%')
    print(f'Consumo por minuto: {taxa_consumo}%')
    print(f'Limite Mínimo: {limite_combustivel}%')
    print(f'Tempo até atingir o limite: {tempo_limite:.1f} minutos')

    # Utilizando matplotlib para plotagem do gráfico
    plt.plot(tempo, combustivel, label="Combustível restante")
    plt.axhline(y=limite_combustivel, linestyle="--", color="red", label="Limite mínimo de 80%")
    plt.xlabel("Tempo de descida (minutos)")
    plt.ylabel("Combustível restante (%)")
    plt.title("Consumo de Combustível Durante a Descida")
    plt.grid(True)
    plt.legend()
    plt.show()

# ============================================================
# ALGORITMOS DE ORDENAÇÃO
# ============================================================

def selection_sort(fila):
    """
    Algoritmo de Ordenação por Seleção (Selection Sort).
    Ordena a fila de pouso pela prioridade (índice 1) de forma decrescente.
    """
    n = len(fila)
    for i in range(n):
        maior = i
        for j in range(i + 1, n):
            if fila[j][1] > fila[maior][1]:
                maior = j
        # Troca os elementos de posição
        fila[i], fila[maior] = fila[maior], fila[i]

def insertion_sort_nome(lista):
    """
    Algoritmo de Ordenação por Inserção (Insertion Sort).
    Ordena os módulos alfabeticamente pelo nome (índice 0) para preparar a busca binária.
    """
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0].casefold() > atual[0].casefold():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual


# ============================================================
# PROCESSAMENTO DOS POUSOS E LÓGICA BOOLEANA
# ============================================================

def processar_pousos(fila, pousados, alertas, pilha):
    print("\n[ 3 ] PROCESSAMENTO DOS POUSOS")
    print("-" * 64)
    total = len(fila)
    contador = 1

    # Loop de processamento da Fila (Enquanto houver elementos)
    while fila:
        # pop(0) remove e retorna o PRIMEIRO elemento da lista, caracterizando o modelo FIFO
        modulo = fila.pop(0)

        print(f"\n[{contador}/{total}] {modulo[0]}")

        # Extração de variáveis booleanas e relacionais
        combustivel_ok = modulo[2] >= 80
        atmosfera_ok = modulo[6]
        area_disponivel = modulo[7]
        sensores_ok = modulo[8]

        print("  Combustível........ OK" if combustivel_ok else "  Combustível........ INSUFICIENTE")
        print("  Atmosfera.......... OK" if atmosfera_ok else "  Atmosfera.......... INADEQUADA")
        print("  Área de pouso...... OK" if area_disponivel else "  Área de pouso...... INDISPONÍVEL")
        print("  Sensores........... OK" if sensores_ok else "  Sensores........... COMPROMETIDOS")

        # PORTA LÓGICA 'AND': O pouso só é autorizado se TODAS as condições forem True
        if combustivel_ok and atmosfera_ok and area_disponivel and sensores_ok:
            print("  >> POUSO AUTORIZADO")
            pousados.append(modulo)
            
            # Adiciona o evento no TOPO da Pilha (LIFO)
            pilha.append(f"{modulo[0]}: pouso autorizado")
        else:
            print("  >> POUSO NÃO AUTORIZADO")
            if not combustivel_ok: print("  >> ALERTA: Combustível insuficiente")
            if not atmosfera_ok: print("  >> ALERTA: Condições atmosféricas inadequadas")
            if not area_disponivel: print("  >> ALERTA: Área de pouso indisponível")
            if not sensores_ok: print("  >> ALERTA: Integridade dos sensores comprometida")
            
            alertas.append(modulo)
            # Adiciona o evento de falha no TOPO da Pilha (LIFO)
            pilha.append(f"{modulo[0]}: pouso não autorizado")

        contador += 1


# ============================================================
# ALGORITMOS DE BUSCA
# ============================================================

def busca_linear(modulos, nome):
    """
    Busca Linear: Percorre a lista elemento por elemento.
    Ideal para listas não ordenadas.
    """
    for modulo in modulos:
        if modulo[0].casefold() == nome.casefold():
            return modulo
    return None

def busca_binaria(modulos, nome):
    """
    Busca Binária: Divide a lista ao meio a cada iteração.
    Obrigatório que a lista 'modulos' esteja previamente ordenada alfabeticamente.
    """
    inicio = 0
    fim = len(modulos) - 1
    nome_busca = nome.casefold()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = modulos[meio][0].casefold()

        if nome_meio == nome_busca:
            return modulos[meio]
        elif nome_busca > nome_meio:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

def realizar_busca(modulos):
    print("\n[ 5 ] BUSCA DE MÓDULO")
    print("=" * 64)
    nome_busca = input("Digite o nome do módulo que deseja procurar: ").strip()

    # Executando Busca Linear na lista original
    resultado_linear = busca_linear(modulos, nome_busca)
    print("\nRESULTADO DA BUSCA LINEAR")
    print("-" * 64)
    if resultado_linear is not None:
        print(f"Encontrado: {resultado_linear[0]} (Prioridade: {resultado_linear[1]} | Combustível: {resultado_linear[2]}%)")
    else:
        print("Módulo não encontrado.")

    # Executando Busca Binária na lista previamente ordenada pelo Insertion Sort
    resultado_binario = busca_binaria(modulos_alfabeticos, nome_busca)
    print("\nRESULTADO DA BUSCA BINÁRIA")
    print("-" * 64)
    if resultado_binario is not None:
        print(f"Encontrado: {resultado_binario[0]} (Prioridade: {resultado_binario[1]} | Combustível: {resultado_binario[2]}%)")
    else:
        print("Módulo não encontrado.")


# ============================================================
# EXECUÇÃO PRINCIPAL DO SISTEMA
# ============================================================

exibir_titulo()
exibir_modulos(modulos)

# 1. Ordena a fila de pouso por prioridade
selection_sort(fila_pouso)
exibir_fila(fila_pouso)

# 2. Ordena a lista auxiliar alfabeticamente para permitir a busca binária
insertion_sort_nome(modulos_alfabeticos)

# 3. Processa a fila (FIFO) e alimenta a pilha de eventos (LIFO)
processar_pousos(fila_pouso, modulos_pousados, modulos_alerta, pilha_eventos)

# 4. Exibe os resultados organizados
exibir_resumo(modulos_pousados, modulos_alerta, fila_pouso)
exibir_pilha(pilha_eventos)
realizar_busca(modulos)

# 5. Exibe a modelagem matemática usando matplotlib e numpy
exibir_grafico_combustivel()

print("\n" + "=" * 94)
print(" " * 39 + "FIM DA OPERAÇÃO")
print("=" * 94)