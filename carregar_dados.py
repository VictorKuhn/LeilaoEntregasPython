def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    n = int(linhas[0])
    destinos = linhas[1].replace(',', '').split()

    conexoes = []
    for i in range(2, 2 + n):
        conexoes.append(list(map(int, linhas[i].split(', '))))

    m = int(linhas[2 + n])
    entregas = []
    for i in range(3 + n, 3 + n + m):
        temp = linhas[i].split(', ')
        entregas.append((int(temp[0]), temp[1], int(temp[2])))

    return destinos, conexoes, entregas