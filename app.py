from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/avaliar", methods=["POST"])
def avaliar():
    texto = request.form["curriculo"]
    
    # Aqui depois vamos colocar a IA
    resultado = f"O currículo enviado tem {len(texto.split())} palavras."
    
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
