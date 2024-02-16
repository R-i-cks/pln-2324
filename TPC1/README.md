### Primeiro TPC

Ao código desenvolvido na aula foi adicionado mais filtragem com replaces.

Foi também desenvolvida uma função, "tabAnagrama", que tem como argumento uma lista, que serão as palavras filtradas do documento.
Nesta função é criado um dicionário, em que as chaves são as palavras ordenadas alfabeticamente, através do sorted.
Após a criação deste dicionário, retiram-se os pares que para determinada chave só apresentam uma ocorrência, retornando então um dicionário de anagramas cuja chave é a palavra ordenada. 