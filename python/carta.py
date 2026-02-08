html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>San Valentín 💖</title>
    <style>
        body {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .carta {
            background: white;
            padding: 30px;
            border-radius: 20px;
            width: 350px;
            text-align: center;
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        }

        h1 {
            color: #e63946;
        }

        p {
            font-size: 18px;
            color: #333;
        }

        button {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 10px;
            background: #e63946;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #d62828;
        }

        /* CORAZÓN LATIENDO */
        .corazon {
            font-size: 40px;
            display: inline-block;
            animation: latido 1s infinite;
        }

        @keyframes latido {
            0% { transform: scale(1); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>

<div class="carta">
    <div class="corazon">❤️</div>
    <h1>Feliz San Valentín</h1>
    <p id="mensaje">
        Tengo algo importante que preguntarte...
    </p>
    <button onclick="mostrarMensaje()">💌 Presiona aquí</button>
</div>

<script>
function mostrarMensaje() {
    document.getElementById("mensaje").innerHTML =
    "¿Quieres ser mi San Valentín? 💕🥰";
}
</script>

</body>
</html>
"""

with open("../html/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✨ Proyecto actualizado. Abre html/index.html")
