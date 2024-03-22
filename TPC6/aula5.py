from flask import Flask, render_template
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
    trad_en = traduzir(designacao,"pt","en")
    conc_en = traduzir(conceitos[designacao],"pt","fr")
    trad_fr = traduzir(designacao,"pt","fr")
    conc_fr = traduzir(conceitos[designacao],"pt","fr")
    return render_template('conc.html',conceito = conceitos[designacao], des = designacao, des_en = trad_en, conc_en=conc_en,des_fr = trad_fr, conc_fr=conc_fr)


@app.route("/counceitos/<designacao>", methods=["PUT"])
def editar_Conceitos(designacao):
    return

app.run(host="localhost", port=4002, debug=True)

