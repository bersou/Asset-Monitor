from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/dados')
def obter_dados():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT timestamp, vibracao, temperatura FROM sensores ORDER BY id DESC LIMIT 20")
    rows = cur.fetchall()
    conn.close()
    rows.reverse()
    return jsonify({
        "labels": [r[0] for r in rows],
        "vibracao": [r[1] for r in rows],
        "temperatura": [r[2] for r in rows]
    })

# if __name__ == '__main__':
#     app.run(debug=True)