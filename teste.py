
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():
    nome = request.form.get('nome')
    return render_template('resultado.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
