import re

doc_text_path ="dicionario_medico.txt"

doc_t = open(doc_text_path,'r', encoding="utf-8")

doc = doc_t.read()

# data cleaning

doc = re.sub(r"\n\f","\n\n", doc)  # colocar uma linha em branco nas quebras de pagina
doc = re.sub(r"\f","", doc)


# marcar designações

print(doc)

doc = re.sub(r"\n\n(.+)", r"\n\n@\1", doc)

doc = re.sub(r"@(.+)\n\n@", r"@\1\n", doc)

#extrair termos
termos = re.findall(r"@(.+)\n",doc)

conj = re.findall(r"@(.+)\n([^@]+)",doc)   # daqui sai um tuplo

#print(termos[0:50])
#print(conj)


# uma alternativa seria 

# extrair termos

conceitos = re.split(r"\n{2,}",doc)

#termos = [tuple(conceito.split("\n",maxsplit=1)) for conceito in conceitos]

#print(termos)


# formar o HTML
body =""

titulo = "<h2> Dicionário Médico </h2>"
descricao = '<p class="title"> Este é um dicionário médico desenvolvido na disciplina de SPLEB </p>'

for termo in conj:
    body+='<div class="elemento">'
    body+= f"<h5>{termo[0]} </h5>"
    body += f"<p> {termo[1]} </p>"
    body+="</div>"
body+= "</body></html>"

html ="""<!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="convertido.css" />
        <title>TPC3</title>
    </head>
    <body>
    <div class="header">""" +titulo + descricao+'</div>' + body

file_out = open("index.html","w")
file_out.write(html)
file_out.close()

