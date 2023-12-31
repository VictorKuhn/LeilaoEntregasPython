def leilao_v2(destinos, conexoes, entregas):
    entregas.sort(key=lambda x: x[0])
    n = len(entregas)

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        tempo_saida_i, destino_i, bonus_i = entregas[i - 1]
        tempo_viagem_i = conexoes[destinos.index('A')][destinos.index(destino_i)]

        j = i - 1
        while j >= 0:
            tempo_saida_j, destino_j, bonus_j = entregas[j]
            tempo_viagem_j = conexoes[destinos.index('A')][destinos.index(destino_j)]

            if tempo_saida_j + tempo_viagem_j * 2 <= tempo_saida_i:
                break

            j -= 1

        if j == -1:
            dp[i] = max(bonus_i, dp[i - 1])
        else:
            dp[i] = max(bonus_i + dp[j + 1], dp[i - 1])

    sequencia_entregas = []
    i = n
    while i > 0:
        if i == 1 or dp[i - 1] != dp[i]:
            sequencia_entregas.append(entregas[i - 1])

        i -= 1

    sequencia_entregas.reverse()

    return sequencia_entregas, dp[n]
