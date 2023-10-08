# LeilaoEntregasPython - N1 Inteligência Artificial

Projeto de desenvolvimento de um programa com conceitos de IA e grafos para a disciplina de Inteligência Artificial.

## Descrição

Este projeto visa a implementação de diferentes versões de um leilão de entregas utilizando conceitos de inteligência artificial e grafos. Os detalhes dos arquivos e suas funções principais são os seguintes:

- **dados.txt**: Arquivo utilizado para armazenar os dados que serão processados pela aplicação.
- **carregar_dados.py**: Extrai dados do arquivo `dados.txt` e os trata, armazenando-os em três variáveis distintas: `destinos`, `conexoes` e `entregas`.
- **leilao.py, leilao_v2.py, leilao_v3.py**: São três diferentes versões do leilão de entregas, cada uma com um nível de complexidade crescente. `leilao.py` é uma implementação básica, `leilao_v2.py` utiliza programação dinâmica e `leilao_v3.py` utiliza um método de busca de profundidade com poda para otimização.
- **main.py**: Extrai os resultados das três versões diferentes do leilão e os formata para exibição. Cria variáveis como `sequencia_entregas_v1`, `lucro_total_v1`, `performance_v1` (em milissegundos), e assim por diante, para cada versão do leilão, e junta-os em uma variável chamada `resultados`.
- **grafico_performance.py** e **grafico_performance_grid.py**: São responsáveis por extrair os `resultados` de `main.py` e apresentá-los visualmente em dois tipos diferentes de gráficos para comparar o tempo de execução (em milissegundos) pelo lucro obtido nas três versões.
- **grafico_interativo.py**: Gera um gráfico interativo com inputs para que o usuário possa interagir e ajustar parâmetros, como a definição de destinos, tempos de conexão e entregas.



---

Feito por:

 - Davi Prudente [See LinkedIn](https://www.linkedin.com/in/daviprudente/)
 - Marcos Jr [See LinkedIn](https://www.linkedin.com/in/marcos-gon%C3%A7alves-bbb17a1b5)
 - Victor Hugo [See LinkedIn](https://www.linkedin.com/in/victorbkuhn/)
 - Wesley Sardi [See LinkedIn](https://www.linkedin.com/in/wesleysardi/)
