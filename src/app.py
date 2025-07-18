from flask import Flask, request, render_template, jsonify
from pickle import load
import joblib

app = Flask(__name__)

# Cargar la lista de modelos únicos
modelos = joblib.load("./modelos_unicos.pkl")
fabricantes = joblib.load("./Fabricantes_unicos.pkl")
estados = joblib.load("./State_unicos.pkl")

@app.route("/autocomplete/modelos")
def autocomplete_modelos():
    q = request.args.get("q", "").lower()
    sugerencias = [m for m in modelos if q in m.lower()][:10]
    return jsonify(sugerencias)

@app.route("/autocomplete/fabricantes")
def autocomplete_fabricantes():
    q = request.args.get("q", "").lower()
    sugerencias = [f for f in fabricantes if q in f.lower()][:10]
    return jsonify(sugerencias)

@app.route('/autocomplete/estados')
def autocomplete_estados():
    q = request.args.get('q', '').lower()
    sugerencias = [estado for estado in estados if q in estado.lower()]
    return jsonify(sugerencias)




model = load(open("../models/decision_tree_classifier_default_42.sav", "rb"))
class_dict = {
    "0": "Dato 01",
    "1": "Dato 02",
    "2": "Dato 03"
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        modelo = request.form.get("modelo", "")

        yearr = float(request.form["yearr"])
        odometerr = float(request.form["Odometerr"])
        fabricante = request.form["fabricante"]
        modelo = request.form["modelo"]
        condittionn = request.form["condittionn"]
        fuell = request.form["fuell"]
        tituloo = request.form["Tituloo"]
        caja = request.form["Caja"]
        statee = request.form["statee"]
        fechaa = request.form["fechaa"]

        # Puedes imprimir para verificar que llegan bien:
        print(">>> Datos recibidos:")
        print("Año:", yearr)
        print("Odómetro:", odometerr)
        print("Fabricante:", fabricante)
        print("Modelo:", modelo)
        print("Condición:", condittionn)
        print("Combustible:", fuell)
        print("Título:", tituloo)
        print("Caja:", caja)
        print("Estado:", statee)
        print("Fecha:", fechaa)



        data = [[yearr, odometerr, fabricante, modelo, condittionn, fuell, tituloo, caja, statee, fechaa]]

        #print(data)
       # prediction = str(model.predict(data)[0])
       # pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)