import sqlite3
import random
import time
from datetime import datetime

def criar_tabela():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS sensores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        vibracao REAL,
        temperatura REAL
    )''')
    conn.commit()
    conn.close()

def inserir_dado():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    vibracao = round(random.uniform(5, 20), 2)
    temperatura = round(random.uniform(40, 75), 1)
    cur.execute("INSERT INTO sensores (timestamp, vibracao, temperatura) VALUES (?, ?, ?)",
                (timestamp, vibracao, temperatura))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_tabela()
    while True:
        inserir_dado()
        time.sleep(5)