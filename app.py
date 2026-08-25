from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Sandbox",
        "plataforma": "PC",
        "ano": 2011
    },
    {
        "id": 2,
        "titulo": "Super Mario Odyssey",
        "genero": "Plataforma",
        "plataforma": "Nintendo Switch",
        "ano": 2017
    },
    {
        "id": 3,
        "titulo": "Rocket League",
        "genero": "Esporte",
        "plataforma": "Multiplataforma",
        "ano": 2015
    }
]


# ==========================================
# 1. GET /api/jogos
# ==========================================


# ==========================================
# 2. GET /api/jogos/<id>
# ==========================================


# ==========================================
# 3. POST /api/jogos
# ==========================================


# ==========================================
# 4. PUT /api/jogos/<id>
# ==========================================


# ==========================================
# 5. DELETE /api/jogos/<id>
# ==========================================


if __name__ == "__main__":
    app.run(debug=True)
