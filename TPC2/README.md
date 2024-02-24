## TPC2

### Descrição Breve

Nesta ficha pus em prática diferentes conceitos associados a expressões regulares.

### Aspetos da Resolução

Em alguns dos exercícios foi necessário considerar a existência de maiúsculas e minúsculas, contudo quando esta diferença não era relevante utilizou-se a flag "re.IGNORECASE".

No exercício 2 foi utilizada a expressão "por favor([?\.!:;]|(\.\.\.))$" para capturar os diferentes tipos de pontos, não funcionando para sinais inválidos("..","...."," ", etc...)

No exercicio 7 foi utilizada a função "re.fullmatch" para garantir que todos os carateres da palavra cumpriam os requisitos, tendo sido a expressão "[a-zA-Z]\w*".

No exercício 8 para capturar os números inteiros positivos e negativos foi utilizada a expressão "-?\d+", não lidando esta com o separador decimal, e deste modo caso haja 34,56 irá representar 34 e 56 separadamente.

No exercício 9 utilizou-se o split, separando cada palavra numa lista e o join com '_'.

Por último no exercício 10 procedi ao split pelo '-' a cada código, e juntei cada lado num tuplo, retornando uma lista de tuplos.