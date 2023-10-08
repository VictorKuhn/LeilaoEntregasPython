import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from time import perf_counter

from leilao import leilao
from leilao_v2 import leilao_v2
from leilao_v3 import leilao_v3


def criar_interface():
    janela = tk.Tk()

    figura = Figure(figsize=(6, 4), dpi=100)
    subfigura = figura.add_subplot(111)

    canvas = FigureCanvasTkAgg(figura, master=janela)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    tk.Label(janela, text="Destinos:").pack()
    entrada_destinos = tk.Entry(janela)
    entrada_destinos.pack()

    tk.Label(janela, text="Conexões:").pack()
    entrada_conexoes = tk.Entry(janela)
    entrada_conexoes.pack()

    tk.Label(janela, text="Entregas:").pack()
    entrada_entregas = tk.Entry(janela)
    entrada_entregas.pack()

    botao = tk.Button(janela, text='Executar simulação',
                      command=lambda: executar_simulacao(entrada_destinos.get(), entrada_conexoes.get(),
                                                         entrada_entregas.get(), subfigura, canvas))
    botao.pack()

    tk.mainloop()


def executar_simulacao(destinos_str, conexoes_str, entregas_str, subfigura, canvas):
    destinos = destinos_str.split(',')
    conexoes = [list(map(int, conexao.split(','))) for conexao in conexoes_str.split(';')]
    entregas = [tuple(int(x) if i != 1 else str(x) for i, x in enumerate(entrega.split(',')))
                for entrega in entregas_str.split(';')]

    inicio = perf_counter()
    sequencia_entregas_v1, lucro_total_v1 = leilao(destinos, conexoes, entregas)
    fim = perf_counter()
    performance_v1 = (fim - inicio) * 1000

    inicio = perf_counter()
    sequencia_entregas_v2, lucro_total_v2 = leilao_v2(destinos, conexoes, entregas)
    fim = perf_counter()
    performance_v2 = (fim - inicio) * 1000

    inicio = perf_counter()
    sequencia_entregas_v3, lucro_total_v3 = leilao_v3(destinos, conexoes, entregas)
    fim = perf_counter()
    performance_v3 = (fim - inicio) * 1000

    resultados = {
        'Versão 1': performance_v1,
        'Versão 2': performance_v2,
        'Versão 3': performance_v3,
    }

    subfigura.clear()

    subfigura.bar(resultados.keys(), resultados.values())

    canvas.draw()


if __name__ == '__main__':
    criar_interface()
