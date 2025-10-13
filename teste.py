# SELECIONA-ATIVIDADES-RECURSIVO(inicio, fim, ultima_escolhida, total)
#     proxima ← ultima_escolhida + 1          // começa procurando a atividade logo após a última escolhida
#     enquanto proxima ≤ total e inicio[proxima] < fim[ultima_escolhida] faça
#         proxima ← proxima + 1               // pula atividades que começam antes da última terminar (conflito)
#     se proxima ≤ total então
#         retorne {proxima} ∪ SELECIONA-ATIVIDADES-RECURSIVO(inicio, fim, proxima, total)
#                                             // seleciona 'proxima' e continua recursivamente a partir dela
#     senão
#         retorne ∅


def seleciona_atividades_recursivo(inicio, fim, ultima_escolhida, total):
    proxima = ultima_escolhida + 1

    # encontra a próxima atividade que não conflita
    while proxima <= total and inicio[proxima] < fim[ultima_escolhida]:
        proxima += 1

    if proxima <= total:
        return [proxima] + seleciona_atividades_recursivo(inicio, fim, proxima, total)
    else:
        return []


# tempos de início e fim (índice 0 reservado para facilitar)
inicio = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
fim =    [0, 4, 5, 6, 7, 9, 9,10,11,12,14,16]

# chamada inicial — começa com a "última escolhida" = 0
atividades_escolhidas = seleciona_atividades_recursivo(inicio, fim, 0, len(inicio) - 1)

print("Atividades selecionadas:", atividades_escolhidas)