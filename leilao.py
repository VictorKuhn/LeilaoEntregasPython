def leilao(destinos, conexoes, entregas):
    entregas.sort(key=lambda x: x[2], reverse=True)  # ordena as entregas pelo valor do bônus em ordem decrescente
    sequencia_entregas = []
    lucro_total = 0
    tempo_atual = 0
    local_atual = 'A'

    for entrega in entregas:
        tempo_saida, destino, bonus = entrega
        tempo_viagem = conexoes[destinos.index(local_atual)][destinos.index(destino)]

        if tempo_atual + tempo_viagem <= tempo_saida:  # se a entrega puder ser feita a tempo
            sequencia_entregas.append(entrega)
            lucro_total += bonus
            tempo_atual += tempo_viagem * 2  # considera o tempo de ida e volta

    return sequencia_entregas, lucro_total
