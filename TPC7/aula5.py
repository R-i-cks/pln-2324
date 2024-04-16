from flask import Flask, render_template, request
import json
from deep_translator import GoogleTranslator
app = Flask(__name__)

file = open("conceitos.json")
conceitos = json.load(file)

def traduzir(des,s,t):
    traducao = GoogleTranslator(source=s, target=t).translate(des)
    return traducao


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/conceitos")
def listar_Conceitos():
    return render_template("conceitos.html", conceitos = conceitos)

@app.route("/conceitos/<designacao>")
def consultar_Conceitos(designacao):
    if designacao in conceitos:
        trad_en = traduzir(designacao,"pt","en")
        conc_en = traduzir(conceitos[designacao],"pt","en")
        trad_fr = traduzir(designacao,"pt","fr")
        conc_fr = traduzir(conceitos[designacao],"pt","fr")
        print(trad_en,conc_en,trad_fr, conc_fr)
        return render_template('conc.html',conceito = conceitos[designacao], des = designacao, des_en = trad_en, conc_en=conc_en,des_fr = trad_fr, conc_fr=conc_fr)
    else:
        return render_template("erro.html", erro= "Conceito não existe na nossa base de dados.")

@app.route("/conceitos", methods=["POST"])
def adicionar_conceitos():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    print(designacao, descricao)
    conceitos[designacao] = descricao
    return render_template("conceitos.html", conceitos = conceitos)

@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceitos(designacao):
    file_out = open("conceitos.json","w")
    del conceitos[designacao]
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    return render_template("conceitos.html", conceitos = conceitos)


@app.route("/table")
def table():
    return render_template("datatable.html", conceitos = conceitos)



@app.route("/procurar")
def procurar():
    return render_template("procura.html", resultados = conceitos)

app.run(host="localhost", port=4002, debug=True)
