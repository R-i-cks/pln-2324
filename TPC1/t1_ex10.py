# Ex10

# definir filename
file = open("pln-2324/CIH Bilingual Medical Glossary English-Spanish.txt")

text = file.read()

text = text.replace(".", " ")
text = text.replace(",", " ")
text = text.replace("-", " ")
text = text.replace("(", " ")
text = text.replace(")", " ")
text = text.replace("[", " ")
text = text.replace("]", " ")
text = text.replace("{", " ")
text = text.replace("}", " ")
text = text.replace("\"", " ")
text = text.replace("\'", " ")
text = text.replace(":", " ")
text = text.replace(";", " ")


# ...

text = text.lower() 

tokens = text.split()
tokens = list(set(tokens))


def tabAnagrama(lista):
    anagramas= {}
    for pal in lista:
        if len(pal)>2:
            chave = ''.join(sorted(pal))
            if chave in anagramas.keys():
                if pal not in anagramas[chave]:
                    anagramas[chave].append(pal)
            else:
                anagramas[chave] = [pal]
    # Do dicionário aqui gerado não interessa as chaves com apenas uma entrada
    n_anagramas ={}
    for elem in anagramas.keys():
        if len(anagramas[elem])>=2:
            n_anagramas[elem] = anagramas[elem]       
    return n_anagramas



print(tabAnagrama(tokens))