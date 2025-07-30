# Adicionado render_template na linha de importação
from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Nova rota para a página inicial ('/')
# Esta função será executada quando alguém acessar a URL principal do seu site
@app.route('/')
def home():
    # O render_template procura por um arquivo chamado 'index.html' e o exibe
    return render_template('index.html')

# Sua rota de API para obter os dados continua igual
@app.route('/dados')
def obter_dados():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    # A consulta SQL busca o timestamp, vibração e temperatura dos sensores.
    cur.execute("SELECT timestamp, vibracao, temperatura FROM sensores ORDER BY id DESC LIMIT 20")
    rows = cur.fetchall()
    conn.close()
    rows.reverse()
    # Os dados são formatados em JSON para serem usados pelo gráfico.
    return jsonify({
        "labels": [r[0] for r in rows],
        "vibracao": [r[1] for r in rows],
        "temperatura": [r[2] for r in rows]
    })

# Reativei este bloco para que você possa testar localmente se precisar,
# ele não afeta o deploy no Render.
if __name__ == '__main__':
    app.run(debug=True)