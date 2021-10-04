from flask import Flask, jsonify
import sqlite3
app = Flask(__name__)

@app.route("/api/v.1.0/movimientos")
def inicio():
    conn = sqlite3.connect("data/movimientos.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movimientos ORDER BY fecha")
    filas = cur.fetchall()
    claves = cur.description

    resultado = []
    for fila in filas:
        d = {}
        for tclave, valor in zip(claves, fila):
            d[tclave[0]] = valor
        resultado.append(d)
    conn.close()

    return jsonify(resultado)