from flask import Flask, render_template
from database.db import *

app = Flask(__name__)

@app.route("/")
def home_page():
    connectionSQL()
    return render_template("home.html")
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def registro_mascota():
    id = request.form["id"]
    Numero_de_contacto = request.form["contacnumber"]
    edad_Mascota = request.form["age"]
    Nombre_Mascota = request.form["namepet"]
    print(id, contacnumber, age, namepet)
    return "Ok"

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080'
    app.run(host, port)