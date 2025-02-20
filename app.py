from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None  # Variable para almacenar el resultado

    if request.method == "POST":
        try:
            peso = float(request.form.get("peso", 0))
            estatura = float(request.form.get("estatura", 0))
            if peso <= 0 or estatura <= 0: #Validar que sean positivos
                result = "No se aceptan números negativos."
            else:
                result = peso / (estatura ** 2)
                if result==30 or result>30:
                    result= "Obesidad", result
                elif result<18.5:
                    result= "Bajo peso", result
                elif result==18.5 or result<25:
                    result= "Peso normal", result
                elif result==25 or result<30:
                    result= "Sobrepeso", result            
        except ValueError:
            result = "Por favor, ingrese valores numéricos válidos."

    return render_template("index.html", result=result)
