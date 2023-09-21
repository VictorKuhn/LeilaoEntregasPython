from time import perf_counter

from carregar_dados import carregar_dados
from leilao import leilao
from leilao_v2 import leilao_v2
from leilao_v3 import leilao_v3

def main():
    destinos, conexoes, entregas = carregar_dados('dados.txt')

    inicio = perf_counter()  # chama a função time diretamente
    sequencia_entregas_v1, lucro_total_v1 = leilao(destinos, conexoes, entregas)
    fim = perf_counter()
    print('Versão 1:')
    print('Sequência de entregas:', sequencia_entregas_v1)
    print('Lucro total:', lucro_total_v1)
    print('Tempo de execução:', (fim - inicio) * 1000, 'ms')

    inicio = perf_counter()
    sequencia_entregas_v2, lucro_total_v2 = leilao_v2(destinos, conexoes, entregas)
    fim = perf_counter()
    print('Versão 2:')
    print('Sequência de entregas:', sequencia_entregas_v2)
    print('Lucro total:', lucro_total_v2)
    print('Tempo de execução:', (fim - inicio) * 1000, 'ms')

    inicio = perf_counter()
    sequencia_entregas_v3, lucro_total_v3 = leilao_v3(destinos, conexoes, entregas)
    fim = perf_counter()
    print('Versão 3:')
    print('Sequência de entregas:', sequencia_entregas_v3)
    print('Lucro total:', lucro_total_v3)
    print('Tempo de execução:', (fim - inicio) * 1000, 'ms')


if __name__ == '__main__':
    main()