# TPC5

Na resolução deste TPC foi reutilizado o ficheiro "etiquetador.py" criado nas aulas práticas.
Para além do ficheiro "conceitos.json", utilizado para construir as descrições, foi utilizado o ficheiro "termos_traduzidos.txt" para construir um dicionário termo-tradução, sendo para isto usado um findall com a expressão regular "(.+) @ (.+)", seguido do operador dict.

Posto isto, caso exista no dicionário, a tradução do termo é colocada na âncora, caso contrário apresenta "tradução indisponível".
