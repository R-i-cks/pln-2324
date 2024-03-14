import json, re


file_conceitos = open("conceitos.json")
file_livro = open("/home/utilizador/Uni/4_Ano/2_Semestre/ProLinNat/LIVRO-Doenças-do-Aparelho-Digestivo.txt")
file_conceitos_traducao = open("termos_traduzidos.txt")

texto = file_livro.read()
conceitos = json.load(file_conceitos)
conceitos_en = file_conceitos_traducao.read()
# há palavras problemáticas que podem aparecer com link, podemos criar blacklist

blacklist = ["e","para","de","pelo","os","são","este"]

conceitos_min = {chave.lower(): conceitos[chave] for chave in conceitos}

conceitos_trad = dict(re.findall(r"(.+) @ (.+)",conceitos_en))  # dicionário de traduções
print(conceitos_trad['faringe'])
def etiquetador(matched):
     palavra = matched[0]
     original = palavra
     palavra = palavra.lower()
     if palavra in conceitos and palavra not in blacklist:
        descricao = conceitos[palavra]
        try:
            palavra_trad = conceitos_trad[palavra]
        except:
            palavra_trad="Tradução indisponível"
        etiqueta = f"<a href='' title ='en: {palavra_trad}; descricao pt: {descricao}'>{palavra}</a>"
        return etiqueta
     else:
         return original


expressao = r'[\wáéçãóõéíêâ]+'          # incluir carateres normais e específicos da língua.
texto=re.sub(expressao, etiquetador, texto, flags=re.IGNORECASE)
texto = re.sub(r'\n',r'<br>', texto)
texto = re.sub(r'\f', r'<hr/>',texto)
         


file_out = open("livro.html","w", encoding="UTF-8")

print(texto, file=file_out)
