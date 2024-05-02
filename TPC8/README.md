# TPC8

## Modelos

Neste tpc testou-se diferentes hiperparâmetros de modo a averiguar quais influenciavam mais, de forma positiva.

Deste modo o melhor modelo verificou-se para aquele cujos hiperparâmetros foram definidos da seguinte forma:

"vector_size= 250, window= 2, min_count= 4, epochs= 12"

Deste trabalho de exploração conclui-se que um maior número de epochs não traduz, necessariamente, melhor desempenho dos modelos, o que se pode dever à dimensão dos dados explorados. 
Ao subir também o número de vezes que uma palavra deve aparecer para ser considerada, verificou-se também uma melhoria qualitativa da informação retornada ( menos advérbios e conjugações verbais, com aumento de nomes).

De modo a averiguar a qualidade do modelo foram implementados alguns métodos "most_similar" e "doesnt_match", tendo-se obtido resultados favoráveis.