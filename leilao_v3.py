def dfs(destinos, conexoes, entregas, entrega_atual, tempo_atual, lucro_atual, lucro_maximo, sequencia_maxima):
    if entrega_atual == len(entregas):
        if lucro_atual > lucro_maximo:
            return sequencia_maxima[::-1], lucro_atual  # inverte a sequência de entregas
        else:
            return sequencia_maxima[::-1], lucro_maximo  # inverte a sequência de entregas

    tempo_saida_i, destino_i, bonus_i = entregas[entrega_atual]
    tempo_viagem_i = conexoes[destinos.index('A')][destinos.index(destino_i)]

    if tempo_atual + tempo_viagem_i <= tempo_saida_i:  # se a entrega i pode ser feita a tempo
        # Calcula o bônus máximo restante
        bonus_maximo_restante = sum(entrega[2] for entrega in entregas[entrega_atual+1:])

        if lucro_atual + bonus_i + bonus_maximo_restante > lucro_maximo:  # se vale a pena explorar esse ramo
            # Faz a entrega i
            nova_sequencia_maxima, novo_lucro_maximo = dfs(destinos, conexoes, entregas, entrega_atual+1, tempo_atual+tempo_viagem_i*2, lucro_atual+bonus_i, lucro_maximo, [entregas[entrega_atual]]+sequencia_maxima)
            if novo_lucro_maximo > lucro_maximo:
                lucro_maximo = novo_lucro_maximo
                sequencia_maxima = nova_sequencia_maxima

    # Não faz a entrega i
    nova_sequencia_maxima, novo_lucro_maximo = dfs(destinos, conexoes, entregas, entrega_atual+1, tempo_atual, lucro_atual, lucro_maximo, sequencia_maxima)
    if novo_lucro_maximo > lucro_maximo:
        lucro_maximo = novo_lucro_maximo
        sequencia_maxima = nova_sequencia_maxima

    return sequencia_maxima[::-1], lucro_maximo  # inverte a sequência de entregas

def leilao_v3(destinos, conexoes, entregas):
    entregas.sort(key=lambda x: x[0])  # ordena as entregas pelo tempo de saída em ordem crescente
    return dfs(destinos, conexoes, entregas, 0, 0, 0, 0, [])