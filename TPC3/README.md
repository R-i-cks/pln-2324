## Ficheiro extract.py

Este TPC consiste no algoritmo desenvolvido na aula, tendo sido acrescentada uma substituição através da expressão regex "\n\f" por "\n\n", antes de retirar "\f", de modo a lidar com as situações em que devido à quebra de página, a palavra-chave não tinha quebra de linha.

Com esta substituição apenas um par chave - significado ficou quebrado pelo facto de ter um quebra de página na descrição.
Deste modo optou-se por uma operação mais cirúrgica para retirar este problema, através da troca re.sub(r"quimiotaxia\n(.+)\n\f(.+)\n",r"quimiotaxia\n\1\n\2\n", doc)

Não se tendo encontrado mais problemas deu-se esta etapa por terminada.

### Ficheiro HTML

Foi acrescentada a boilerplate clássica de HTML ao ficheiro criado no processo, um elemento div de forma a agrupar a palavra-chave e a descrição.

Foi também acrescentado um elemento div de header, contendo o título e descrição do trabalho.

Por último foi criado um ficheiro css para tornar a página criada mais agradável.