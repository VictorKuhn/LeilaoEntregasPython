import matplotlib.pyplot as plt
from main import main

resultados = main()

x_axis = [0, resultados['performance_v1']]
y_axis = [0, resultados['lucro_total_v1']]

x2_axis = [0, resultados['performance_v2']]
y2_axis = [0, resultados['lucro_total_v2']]

x3_axis = [0, resultados['performance_v3']]
y3_axis = [0, resultados['lucro_total_v3']]

plt.plot(x_axis, y_axis, label='Resultado 1')
plt.plot(x2_axis, y2_axis, label='Resultado 2')
plt.plot(x3_axis, y3_axis, label='Resultado 3')
plt.title('Comparação: Tempo de Execução x Lucro Obtido')
plt.xlabel('Tempo de execução')
plt.ylabel('Lucro Obtido')
plt.legend()
plt.show()
