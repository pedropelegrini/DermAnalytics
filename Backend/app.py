from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def conectar():
    return sqlite3.connect("database.db")

# Criar tabela
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS casos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idade INTEGER,
            sexo TEXT,
            tipo_lesao TEXT,
            regiao TEXT,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

criar_tabela()

# Rota para cadastrar
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.json
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO casos (idade, sexo, tipo_lesao, regiao, data)
        VALUES (?, ?, ?, ?, ?)
    """, (
        dados["idade"],
        dados["sexo"],
        dados["tipo_lesao"],
        dados["regiao"],
        dados["data"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cadastro realizado!"})

# Rota para listar
@app.route("/dados", methods=["GET"])
def dados():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT tipo_lesao, COUNT(*) FROM casos GROUP BY tipo_lesao")
    resultado = cursor.fetchall()

    conn.close()

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)