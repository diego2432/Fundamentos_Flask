from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def hola_mundo():
    return "¡Hola Mundo desde Flask!"

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
