import matplotlib.pyplot as plt
from main import main

resultados = main()

# Extraia os valores de resultados
performance_v1 = resultados['performance_v1']
lucro_total_v1 = resultados['lucro_total_v1']

performance_v2 = resultados['performance_v2']
lucro_total_v2 = resultados['lucro_total_v2']

performance_v3 = resultados['performance_v3']
lucro_total_v3 = resultados['lucro_total_v3']

# Crie os pontos para o gráfico de dispersão
plt.scatter(performance_v1, lucro_total_v1, label='Resultado 1', marker='o')
plt.scatter(performance_v2, lucro_total_v2, label='Resultado 2', marker='s')
plt.scatter(performance_v3, lucro_total_v3, label='Resultado 3', marker='^')

plt.title('Comparação: Tempo de Execução x Lucro Obtido')
plt.xlabel('Tempo de execução (ms)')
plt.ylabel('Lucro Obtido')
plt.legend()
plt.grid(True)

plt.show()
